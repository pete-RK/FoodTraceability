from flask import Flask, jsonify, request
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




@app.route('/TruckDetails', methods=['POST'])
def truckDetails():
    try: 
        #storing input value
        req = request.json
        val = req.get('inputValue', '')
        option = req.get('radioValue', '')

    # Define queries in a dictionary
        queries = {
            'option1': f"""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX FoodTraceability: <http://www.semanticweb.org/sairithvikvaikuntam/ontologies/2023/11/FoodTraceability#>

                SELECT ?eventID ?conatinerID ?startTime ?sourceCotainerLocation ?endTime ?targetContainerLocation ?sourceContainerLoad
                WHERE {{
                    ?sourceContainerLoad rdf:type FoodTraceability:SourceLoad.
                    ?sourceContainerLoad FoodTraceability:hasSourceContainerEventID ?eventID.
                    ?eventID FoodTraceability:hasStartTime ?startTime.
                    ?eventID FoodTraceability:hasEndTime ?endTime.
                    ?eventID FoodTraceability:hasSourceContainerLocation ?sourceCotainerLocation.
                    ?sourceContainerLoad FoodTraceability:loadedFrom ?conatinerID.
                    ?conatinerID FoodTraceability:hasContainerID ?id.
                    FILTER(?id = "{val}")
                    OPTIONAL{{
                        ?eventID FoodTraceability:hasTargetContainerLocation ?targetContainerLocation.
                    }}
                }}
                """,
        'option2': f"""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX FoodTraceability: <http://www.semanticweb.org/sairithvikvaikuntam/ontologies/2023/11/FoodTraceability#>

                SELECT DISTINCT ?sourceContainerID ?targetContainerID
                WHERE {{
                    ?targetContainerLoad rdf:type FoodTraceability:TargetLoad.
                    ?targetContainerLoad FoodTraceability:loadedTo ?targetContainer.
                    ?targetContainer FoodTraceability:hasContainerID ?targetContainerID.
                    ?targetContainerLoad FoodTraceability:hasTargetContainerEventID ?eventID.
                    ?eventID FoodTraceability:hasSourceLoad ?sourceContainerLoad.
                    ?sourceContainerLoad FoodTraceability:loadedFrom ?sourceContainer.
                    ?sourceContainer FoodTraceability:hasContainerID ?sourceContainerID.
                    FILTER(?targetContainerID = "{val}" && ?sourceContainer != ?targetContainer)
                    }}
                """,
        'option3' : f"""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX FoodTraceability: <http://www.semanticweb.org/sairithvikvaikuntam/ontologies/2023/11/FoodTraceability#>

                SELECT ?sourceContainerLoad (SUM(xsd:float(?loadAmount)) AS ?totalTransported)
                WHERE {{
                ?sourceContainerLoad rdf:type FoodTraceability:SourceLoad.
                ?sourceContainerLoad FoodTraceability:loadedFrom ?container.
                ?container FoodTraceability:hasContainerID ?containerID.
                ?sourceContainerLoad FoodTraceability:hasSourceContainerEventID ?sourceEventID.
                ?sourceEventID FoodTraceability:hasTargetLoad ?targetContainerLoad.
                ?sourceEventID FoodTraceability:hasMaterialAmount ?loadAmount.
                FILTER(?containerID = "{val}" && ?targetContainerLoad != ?sourceContainerLoad)
                }}
                GROUP BY ?sourceContainerLoad
                """}
           # Select the appropriate query based on radioValue
        selected_query = queries.get(option)

        # Use a connection context manager
        with stardog.Connection('FoodTraceability_2', **connection_details) as conn:
            valueDict = {}
            results = conn.select(selected_query)
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
