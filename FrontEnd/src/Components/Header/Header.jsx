import React from 'react';
import './Header.css';
import { Link } from 'react-router-dom';

import ButtonKratisi from  '../Button/ButtonKratisi.jsx';
import profilePic from '../../images/favicon.png';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faInstagram } from '@fortawesome/free-brands-svg-icons';
import { faFacebookF } from '@fortawesome/free-brands-svg-icons';
import { faPhone } from '@fortawesome/free-solid-svg-icons';






function Header(){

    return(
        <header>
           

            
            <div className="first-row">
            <div className="phone-number" > <FontAwesomeIcon icon={faPhone} shake style={{color: "#B197FC",}} />  6949470504
            <div className="social-icons">
            <p>Dog Walker Fwteinh</p><a href="https://www.instagram.com/dogwalker.fwteinh/" className="social-icon"><FontAwesomeIcon icon={faInstagram} size="2xl" style={{ color: "#aa5dac" }} /></a>
            <a href="https://www.facebook.com/profile.php?id=61561162122957" className="social-icon"><FontAwesomeIcon icon={faFacebookF} size="2xl" style={{ color: "#aa5dac" }} /></a>
            </div></div>
            <div><Link to="/"><img className="HeaderImage" src={profilePic} alt="profile picture" /></Link></div>
            <Link to ="/randevou"><ButtonKratisi/></Link>
            </div>


            <nav className="navbar">
                <ul>
                    <li><Link to ="/">Φόρμα Επικοινωνίας</Link></li>
                    <li><Link to ="/login">Σύνδεση/Εγγραφή</Link></li>
                    <li><Link to = "/mydoggies">Τα Σκυλάκια μου</Link></li>
                    
                    


                </ul>


            </nav>

        </header>

    );
}

export default Header