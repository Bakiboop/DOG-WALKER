import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import DogCounter from './DogCounter';

function Randevou(){

    const services = [ "Dog Walking","Pet Sitting My Home","Pet Sitting Your Home", "Pet Taxi"];
    const [selectedDates, setSelectedDates] = useState([null,null]);
    const listServices = services.map(service => <li>{service}</li>);
    const [selectedService, setSelectedService] = useState(null);

    const handleServiceChange = (e) => {
        setSelectedService(e.target.value);
    };


    
    return(
        <>
        <div className="Stoixeia Epikoinonias">
            <h2>Στοιχεία Επικοινωνίας</h2>
        <form>


            <input className= "randevouInput" type="text" name="txt" placeholder="Ονοματεπώνυμο"  required />
            <input className= "randevouInput" type="text" name="broj" placeholder="Τηλέφωνο" required />
            <input className= "randevouInput" type="text" name="txt" placeholder="Διεύθυνση"  required />
            <input className= "randevouInput" type="text" name="txt" placeholder="Περιοχή" required />
        </form>
        <div>
        <h3>Ενδιαφέρομαι για:</h3>
        <select value={selectedService} onChange={handleServiceChange}>
        <option value="">--Επιλέξτε Υπηρεσία--</option>
                        {services.map(service => (
                            <option key={service} value={service}>{service}</option>
                        ))}
                    </select>
        {selectedService === "Dog Walking" && (
            
            <div>
                <h3>Πότε θέλετε τις βόλτες;</h3>
                <label>Πρωί</label>
                <input type = "checkbox"/>
                <label>Μεσημέρι</label>
                <input type = "checkbox"/>
                <label>Βράδυ</label>
                <input type = "checkbox"/>
            </div>
            
        )}

        {selectedService === "Pet Taxi" && (
            <>
            <div>
                <label>Παραλαβή:</label>
                <input></input>
                <label>Προς:</label>
                <input></input>
                <label>Ώρα παραλαβής:</label>
                <input></input>
            </div>

            <div>
                <label>Θέλετε μόλις φτάσουμε να σας περιμένω;</label>
                <input type ="checkbox"></input>
            </div>
            </>
            
                
        )}
                    

                    <DogCounter />
        </div>
        <div>
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
                <div>
                    <h2>Μήνυμα:</h2>
                    <input></input>
                </div>
    </div>

    <button className='loginbutton'>Sign up</button>
    </>
    );
}

export default Randevou;