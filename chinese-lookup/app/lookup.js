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
          console.log(response.data);
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
    }, 3000);

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
          <ul>
            {displayResults.map((entry, index) => (
              <li key={index}>
                {entry.pinyin}, {entry.simplified}, {entry.id}, {entry.english}
              </li>
            ))}
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