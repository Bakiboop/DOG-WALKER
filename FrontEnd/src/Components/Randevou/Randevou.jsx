import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import DogCounter from './DogCounter';
import './Randevou.css'; 
import './DatePicker.css';

function Randevou(){

    const services = [ "Dog Walking","Pet Sitting My Home","Pet Sitting Your Home", "Pet Taxi","Άλλο"];
    const [selectedDates, setSelectedDates] = useState([null,null]);
    const listServices = services.map(service => <li>{service}</li>);
    const [selectedService, setSelectedService] = useState(null);

    const handleServiceChange = (e) => {
        setSelectedService(e.target.value);
    };


    
    return(
        <>
        <div className="Stoixeia-Epikoinonias">

       
        <div>
        <h3>Ενδιαφέρομαι για:</h3>
        <select value={selectedService} onChange={handleServiceChange}>
        <option value="">--Επιλέξτε Υπηρεσία--</option>
                        {services.map(service => (
                            <option key={service} value={service}>{service}</option>
                        ))}
                    </select>



                    



        <h2>Επιλέξτε Ημερομηνίες Υπηρεσίας</h2>
                    <DatePicker
                        selected={selectedDates[0]}
                        onChange={(dates) => setSelectedDates(dates)}
                        startDate={selectedDates[0]}
                        endDate={selectedDates[1]}
                        selectsRange
                        dateFormat="dd/MM/yyyy"
                        minDate={new Date()}
                        inline
                        placeholderText="Επιλέξτε Εύρος Ημερομηνιών"
                        isClearable
                    />
                    {selectedDates[0] && selectedDates[1] && (
                        <p>
                            Εύρος Ημερομηνιών: {selectedDates[0].toLocaleDateString()} - {selectedDates[1].toLocaleDateString()}
                        </p>
                    )}
            </div>
            <div className ='Message'>
                <h2>Μήνυμα:</h2>
                <textarea></textarea>
            </div>
    </div>

    <button className='loginbutton'>Κλείσε Ραντεβού</button>
    </>
    );
}

export default Randevou;