'use client'

import React from 'react';
import LookupApp from './components/LookupApp';
import Link from 'next/link';

export default function Home() {
  return (
    <div>
      <div>
        <LookupApp /> 
        <Link href="/collection">Collection</Link>
      </div>
    </div>
  );
}
