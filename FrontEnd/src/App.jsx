import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './Pages/HomePage';
import LoginPage from './Pages/LoginPage';
import RandevouPage from './Pages/RandevouPage';
import MyDoggiesPage from './Pages/MyDoggiesPage';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/randevou" element={<RandevouPage />} />
                <Route path="/mydoggies" element={<MyDoggiesPage/>} />
            </Routes>
        </Router>
    );
}

export default App;
