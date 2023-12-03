import React from 'react';
import '../styles/TableStyles.css';

const MyTableComponent = ({ data }) => {
  // Extract column headers
  const columnHeaders = data.map(item => item.columnName);

  // Calculate the maximum number of rows
  const maxRows = Math.max(...data.map(item => item.values.length));

  // Create rows data
  const rowsData = Array.from({ length: maxRows }).map((_, rowIndex) => {
    return data.map(column => column.values[rowIndex] || '');
  });

  return (
    <table className="data-table">
      <thead>
        <tr>
          {columnHeaders.map((header, index) => (
            <th key={index}>{header}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {rowsData.map((row, rowIndex) => (
          <tr key={rowIndex}>
            {row.map((cell, cellIndex) => (
              <td key={cellIndex}>{cell}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default MyTableComponent;
