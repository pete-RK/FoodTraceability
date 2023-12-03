import Header from './components/layout/Header';
import Footer from './components/layout/Footer';
import React, { useState } from 'react';

import './App.css';
import MyComponent from './components/MyComponent';

function App() {

  return (
    <div className="App">
    <Header />
    <MyComponent />           
    <Footer />
  </div>
  );
}

export default App;
