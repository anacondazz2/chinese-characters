'use client'

import React from 'react';
import LookupApp from './components/LookupApp';
import Navbar from './components/Navbar';

export default function Home() {
  return (
    <div>
      <div>
        <LookupApp /> 
        <Navbar />
      </div>
    </div>
  );
}
