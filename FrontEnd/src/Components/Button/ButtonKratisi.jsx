import React from 'react';
import './ButtonKratisi.css';

function ButtonKratisi(props) {
    return (
        <button className={`button-kratisi ${props.className}`}>
            Κάνε Κράτηση!
        </button>
    );
}

export default ButtonKratisi;
