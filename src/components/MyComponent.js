import React, { useState } from 'react';
import axios from 'axios';
import MyTableComponent from './MyTableComponent'; // Import the table component

const MyComponent = () => {
    const [fetchDataResult, setFetchDataResult] = useState([]);

    const fetchData = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:5000/dummy', {
                // Request body
            });
            console.log(response);
            setFetchDataResult(response.data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const handleFetchData = () => {
        fetchData();
    };

    return (
        <div>
            <div>
                <button onClick={handleFetchData}>Fetch Data</button>
            </div>
            {fetchDataResult && fetchDataResult.length > 0 ? (
                <MyTableComponent data={fetchDataResult} />
            ) : (
                <div>No data to display</div>
            )}
        </div>
    );
};

export default MyComponent;
