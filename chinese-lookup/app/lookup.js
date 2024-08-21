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
      axios.get(`http://127.0.0.1:8000/lookup/api/lookup-entry/?query=${encodeURIComponent(query)}`)
        .then((response) => {
          setResult(response.data);
        })
        .catch((error) => {
          console.error('Error fetching data:', error);
          setResult({ error: 'Error retrieving data.' });
        });
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
            <>
              <p>English: {result.english}</p>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default LookupApp;