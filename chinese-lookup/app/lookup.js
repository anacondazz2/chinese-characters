import React, { useState } from 'react'

function LookupApp() {
  const [mInput, setMinput] = useState({});

  const handleChange = (e) => {
    console.log(1);
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