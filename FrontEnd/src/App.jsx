import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './Pages/HomePage';
import LoginPage from './Pages/LoginPage';
import RandevouPage from './Pages/RandevouPage';
import MyDoggiesPage from './Pages/MyDoggiesPage';
import MyRadevouPage from './Pages/MyRadevouPage';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/randevou" element={<RandevouPage />} />
                <Route path="/mydoggies" element={<MyDoggiesPage/>} />
                <Route path="/myradevou" element={<MyRadevouPage/>}/>
            </Routes>
        </Router>
    );
}

export default App;
