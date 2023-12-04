import React, { useState } from 'react';
import axios from 'axios';
import MyTableComponent from './MyTableComponent';
import '../styles/MyComponent.css';

const MyComponent = () => {
    const [inputValue, setInputValue] = useState('');
    const [radioValue, setRadioValue] = useState('option1'); // Default to 'option1'
    const [fetchDataResult, setFetchDataResult] = useState([]);

    const fetchData = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:5000/TruckDetails', {
                // Include inputValue and radioValue in the request body if needed
                inputValue,
                radioValue
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
        <div className='Container_details'>
            <div>
                <input
                    type="text"
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    placeholder="e.g., Truck_1, Combine_1, Cart_1" 
                />
                <div>
                    <label>
                        <input
                            type="radio"
                            value="option1"
                            checked={radioValue === 'option1'}
                            onChange={(e) => setRadioValue(e.target.value)}
                        />
                        Container Details
                    </label>
                    <label>
                        <input
                            type="radio"
                            value="option2"
                            checked={radioValue === 'option2'}
                            onChange={(e) => setRadioValue(e.target.value)}
                        />
                        Transfor Details
                    </label>
                    <label>
                        <input
                            type="radio"
                            value="option3"
                            checked={radioValue === 'option3'}
                            onChange={(e) => setRadioValue(e.target.value)}
                        />
                        Container Load Details
                    </label>
                </div>
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
