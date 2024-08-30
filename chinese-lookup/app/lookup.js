import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Debounce function to delay API calls
const debounce = (func, delay) => {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => func(...args), delay);
  };
};

function LookupApp() {
  const [query, setQuery] = useState('');
  const [result, setResult] = useState([]);
  const [showMore, setShowMore] = useState(false);

  const fetchResult = () => {
    if (query) {
      axios.get(`http://127.0.0.1:8000/api/lookup-entry/?query=${encodeURIComponent(query)}`)
        .then((response) => {
          setResult(response.data);
          // console.log(response.data);
          setShowMore(false); // Reset showMore state on new query
        })
        .catch((error) => {
          console.error('Error fetching data:', error);
          setResult([]);
        });
    } else {
      setResult([]);
    }
  }

  useEffect(() => {
    const id = setTimeout(() => {
      fetchResult();
    }, 1000);

    return () => clearTimeout(id);
  }, [query]);

  const handleChange = (e) => {
    const newQuery = e.target.value;
    setQuery(newQuery); // Update the query state which triggers the effect
  };

  const handleShowMore = () => {
    setShowMore(true);
  };

  const displayResults = showMore ? result : result.slice(0, 50);

  return (
    <div>
      <input
        type="text"
        placeholder="Enter Chinese Text"
        onChange={handleChange}
      />
      {result.length > 0 && (
        <div>
          <h3>Lookup Result:</h3>
          <h3>{displayResults.length} Results found.</h3>
          <ul>
            {displayResults.map((entry, index) => {
              let jsonString = entry.english.replace(/(?<=[:,\[])\s*'|'\s*(?=[:,\]])/g, '"');
              jsonString = jsonString.replace(/;/g, '');
              let englishArray;
              try {
                englishArray = JSON.parse(jsonString);
                console.log(englishArray);
              } catch (error) {
                console.error("Failed to parse JSON:", error.message);
                console.log("Problematic JSON string:", jsonString);
              }
              return (
                <li key={index}>
                  {entry.simplified} {entry.pinyin}
                  <br />
                  {englishArray.map((en, idx) => (
                    <span key={idx}>
                      <strong>{idx + 1}</strong> {en}&nbsp;&nbsp;&nbsp;
                    </span>
                  ))}
                  <br />
                  <button className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4">Add</button>
                </li>
              );
            })}
          </ul>
          {!showMore && result.length > 50 && (
            <button onClick={handleShowMore}>
              Show More
            </button>
          )}
        </div>
      )}
    </div>
  );
}

export default LookupApp;