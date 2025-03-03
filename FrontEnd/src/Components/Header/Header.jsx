import React, { useState, useEffect } from 'react';
import './Header.css';
import { Link, useNavigate } from 'react-router-dom';
import ButtonKratisi from '../Button/ButtonKratisi.jsx';
import profilePic from '../../images/favicon.png';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faInstagram, faFacebookF } from '@fortawesome/free-brands-svg-icons';
import { faPhone } from '@fortawesome/free-solid-svg-icons';

function Header() {
    const [userEmail, setUserEmail] = useState(localStorage.getItem('userEmail') || '');
    const navigate = useNavigate();

    useEffect(() => {
        setUserEmail(localStorage.getItem('userEmail') || '');
    }, []);

    const handleLogout = () => {
        localStorage.removeItem('token');
        localStorage.removeItem('userEmail');
        setUserEmail('');
        navigate('/login'); // Μεταφορά στη σελίδα Login
    };

    return (
        <header>
            <div className="first-row">
                <div className="phone-number">
                    <FontAwesomeIcon icon={faPhone} shake style={{color: "#B197FC"}} /> 6949470504
                    <div className="social-icons">
                        <p>Dog Walker Fwteinh</p>
                        <a href="https://www.instagram.com/dogwalker.fwteinh/" className="social-icon">
                            <FontAwesomeIcon icon={faInstagram} size="2xl" style={{ color: "#aa5dac" }} />
                        </a>
                        <a href="https://www.facebook.com/profile.php?id=61561162122957" className="social-icon">
                            <FontAwesomeIcon icon={faFacebookF} size="2xl" style={{ color: "#aa5dac" }} />
                        </a>
                    </div>
                </div>
                <div>
                    <Link to="/"><img className="HeaderImage" src={profilePic} alt="profile picture" /></Link>
                </div>
                <Link to="/randevou"><ButtonKratisi/></Link>
            </div>

            <nav className="navbar">
                <ul>
                    <li><Link to="/mydoggies">Τα Σκυλάκια μου</Link></li>

                    {/* Αν υπάρχει χρήστης, δείξε το email του και το κουμπί logout */}
                    {userEmail ? (
                        <>
                            <li className="user-info">Συνδεδεμένος ως: {userEmail}  </li>
                            <li><button className="logout-button" onClick={handleLogout}>Αποσύνδεση</button></li>
                        </>
                    ) : (
                        <li><Link to="/login">Σύνδεση/Εγγραφή</Link></li>
                    )}
                </ul>
            </nav>
        </header>
    );
}

export default Header;
