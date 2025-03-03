import React from 'react';
import './CardService.css';
import ButtonKratisi from  '../Button/ButtonKratisi.jsx';
import { Link } from 'react-router-dom';

function CardService(props) {
    return (
        <div className="CardService">
            <img className="ImageService" src={props.image} alt="Service" />
            <div className="TextContainer">
                <h2>{props.service}</h2>
                <p className="TextService">{props.details}</p>
                <Link to="/randevou"><ButtonKratisi className = "Button"/></Link>
            </div>
            
        </div>
    );
}

export default CardService;
