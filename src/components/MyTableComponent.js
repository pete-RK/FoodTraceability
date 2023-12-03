import React from 'react';
import '../styles/TableStyles.css'; 

const MyTableComponent = ({ data }) => {
  return (
    <table className="data-table">
      <thead>
        <tr>
          <th>Container Load URI</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item, index) => (
          <tr key={index}>
            <td>{item}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};


{
        {
            columnName:column1,
          Values : []
        },
        {
        columnName:column4,
          Values : []
        },
        {
         columnName:column3,
          Values : []
        }
    }



export default MyTableComponent;
