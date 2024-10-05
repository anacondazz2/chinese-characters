import React, { useState, useEffect } from 'react';
import Link from 'next/link';

export default function Navbar() {
  return (
    <div>
      <Link href="../collection">Collection</Link> <br />
      <Link href="../account">Account</Link>
    </div>
  )
}