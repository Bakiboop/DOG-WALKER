import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import axios from 'axios';
import './Randevou.css';
import './DatePicker.css';

function Randevou() {
    const services = ["DG", "PM", "PY", "PT", "AL"];
    const [selectedDates, setSelectedDates] = useState([null, null]);
    const [selectedService, setSelectedService] = useState(null);
    const [dogCount, setDogCount] = useState(1);
    const [message, setMessage] = useState('');

    const handleServiceChange = (e) => {
        setSelectedService(e.target.value);
    };

    const handleCountChange = (e) => {
        const count = parseInt(e.target.value, 10);
        if (count >= 1) {
            setDogCount(count);
        }
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        // Έλεγχος ότι όλα τα απαραίτητα πεδία έχουν συμπληρωθεί
        if (!selectedService || !selectedDates[0] || !selectedDates[1] || !dogCount) {
            alert('Παρακαλώ συμπληρώστε όλα τα απαραίτητα πεδία.');
            return;
        }

        // Δημιουργία του αντικειμένου δεδομένων για το backend
        const appointmentData = {
            start_time: selectedDates[0].toISOString(), // Μετατροπή σε ISO string
            end_time: selectedDates[1].toISOString(),  // Μετατροπή σε ISO string
            notes: message,                            // Το μήνυμα του χρήστη
            dogs: dogCount,                            // Ο αριθμός των σκύλων
            type: selectedService,                     // Η επιλεγμένη υπηρεσία
        };
        console.log(appointmentData)
        const token = localStorage.getItem('token'); // Assuming the token is stored with the key 'token'
        try {
            // Αποστολή δεδομένων στο backend
            const response = await axios.post('http://127.0.0.1:8000/api/appointments/', appointmentData, {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                },
            });

            if (response.status === 201) {
                alert('Το ραντεβού σας καταχωρήθηκε με επιτυχία!');
                // Εκκαθάριση των πεδίων μετά την επιτυχή υποβολή
                setSelectedService(null);
                setSelectedDates([null, null]);
                setDogCount(1);
                setMessage('');
            } else {
                alert('Κάτι πήγε στραβά κατά την υποβολή του ραντεβού.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Υπήρξε πρόβλημα κατά την υποβολή του ραντεβού.');
        }
    };

    return (
        <>
            <div className="Stoixeia-Epikoinonias">
                <div>
                    <h3>Ενδιαφέρομαι για:</h3>
                    <select value={selectedService} onChange={handleServiceChange}>
                        <option value="">--Επιλέξτε Υπηρεσία--</option>
                        {services.map((service) => (
                            <option key={service} value={service}>
                                {service}
                            </option>
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
                <div className="Message">
                    <h2>Μήνυμα:</h2>
                    <textarea value={message} onChange={(e) => setMessage(e.target.value)}></textarea>
                </div>

                <h3>Για Πόσα Σκυλάκια;</h3>
                <div style={{ marginBottom: '20px' }}>
                    <input
                        type="number"
                        min="1"
                        value={dogCount}
                        onChange={handleCountChange}
                        style={{ width: '50px', textAlign: 'center' }}
                    />
                </div>
            </div>

            <button className="loginbutton" onClick={handleSubmit}>Κλείσε Ραντεβού</button>
        </>
    );
}

export default Randevou;