import React from 'react';
import './CardService.css';
import ButtonKratisi from  '../Button/ButtonKratisi.jsx';

function CardService(props) {
    return (
        <div className="CardService">
            <img className="ImageService" src={props.image} alt="Service" />
            <div className="TextContainer">
                <h2>{props.service}</h2>
                <p className="TextService">{props.details}</p>
                <ButtonKratisi className = "Button"></ButtonKratisi>
            </div>
            
        </div>
    );
}

export default CardService;
