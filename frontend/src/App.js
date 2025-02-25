import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './components/HomePage';
import LoginPage from './components/LoginPage';
import CustomerWorkflow from './components/CustomerWorkflow';
import PharmacistWorkflow from './components/PharmacistWorkflow';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/customer" element={<CustomerWorkflow />} />
        <Route path="/pharmacist" element={<PharmacistWorkflow />} />
      </Routes>
    </Router>
  );
}

export default App;
