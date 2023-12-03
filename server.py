from flask import Flask, jsonify
import stardog
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Setting up the connection 
connection_details = {
    'endpoint': 'https://sd-f16ca7f0.stardog.cloud:5820',
    'username': 'peterohan.k11@gmail.com',
    'password': 'Mystardog@2020'
}

@app.route('/dummy', methods=['POST'])
def dummy():
    try:
        query1 = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX FoodTraceability: <http://www.semanticweb.org/sairithvikvaikuntam/ontologies/2023/11/FoodTraceability#>

        SELECT ?targetContainerLoad
        WHERE {
            ?targetContainerLoad rdf:type FoodTraceability:TargetLoad .
            ?targetContainerLoad FoodTraceability:hasTargetContainerEventID ?event .
            ?event FoodTraceability:hasSourceLoad ?sourceLoad .
            ?targetContainerLoad FoodTraceability:hasSourceContainerEventID ?sourceEvent .
            
        }
        LIMIT 20
        """
        # Use a connection context manager
        with stardog.Connection('FoodTraceability', **connection_details) as conn:
            valueDict = {}
            results = conn.select(query1)
            for result in results['results']['bindings']:
                for k, v in result.items():
                    if k in valueDict.keys():
                        valList = valueDict[k]
                        if '#' in v['value']:
                            valList.append(v['value'].split('#', 1)[1])
                        else:
                            valList.append(v['value'])
                    else:
                        if '#' in v['value']: 
                            valueDict[k] = [v['value'].split('#', 1)[1]]
                        else:
                            valueDict[k] = [v['value']]

        # creating new list to hold columnNames and columnValues as dictionaries
        jsonValuesPairs = []

        for i, j in valueDict.items():
            dict = {}
            dict["columnName"] = i
            dict["columnValue"] = j
            jsonValuesPairs.append(dict)

        return jsonify(jsonValuesPairs)
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
