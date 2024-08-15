import React, { useState } from 'react'
import axios from 'axios';

function LookupApp() {
  const [input, setInput] = useState([]);

  const handleChange = (e) => {
    const query = e.target.value;
    // axios post
  }

  return (
    <div>
      <input
        type="text"
        placeholder="Enter Chinese Text"
        onChange={handleChange}
      />
    </div>
  )
}

export default LookupApp;