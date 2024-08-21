import React, { useState } from 'react';
import axios from 'axios';

function LookupApp() {
  const [input, setInput] = useState('');
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    const query = e.target.value;
    setInput(query);

    if (query) {
      // Make sure to make request to backend server.
      axios.get(`http://127.0.0.1:8000/api/lookup-entry/?query=${encodeURIComponent(query)}`)
        .then((response) => {
          console.log("Lookup request successful.");
          setResult(response.data);
          console.log(response.data);
        })
        .catch((error) => {
          console.error('Error fetching data:', error);
          setResult({ error: 'Error retrieving data.' });
        });
    } else {
      setResult(null);
    }
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Enter Chinese Text"
        value={input}
        onChange={handleChange}
      />
      {result && (
        <div>
          <h3>Lookup Result:</h3>
          {result.error ? (
            <p>{result.error}</p>
          ) : (
            <ul>
              {result.map((entry, index) => (
                <li key={index}>
                  {entry.pinyin}
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  );
}

export default LookupApp;