import React, { useState, useEffect } from "react";
import axios from "axios";
import "./MyRadevou.css"; // Αν έχεις CSS για styling

const MyRadevou = () => {
    const [appointments, setAppointments] = useState([]);

    useEffect(() => {
        const token = localStorage.getItem("token");
        if (!token) {
            window.location.href = "/login"; // Ανακατεύθυνση αν ο χρήστης δεν είναι συνδεδεμένος
            return;
        }

        // GET request για να πάρεις τα δεδομένα των ραντεβού
        axios.get("http://127.0.0.1:8000/api/appointments/", {
            headers: { "Authorization": `Token ${token}` }
        })
        .then((res) => {
            setAppointments(res.data); // Αποθήκευση των δεδομένων στο state
        })
        .catch((err) => {
            console.error("Error fetching appointments:", err);
            alert("Πρόβλημα κατά την φόρτωση των ραντεβού.");
        });
    }, []); // Το κενό array σημαίνει ότι το useEffect θα τρέξει μόνο μια φορά, κατά το πρώτο render

    return (
        <div className="container">
            <h1>My Appointments</h1>

            <div className="appointment-list">
                {appointments.length > 0 ? (
                    appointments.map((appointment) => (
                        <div key={appointment.id} className="appointment-item">
                            <div className="appointment-time">Start Time: {appointment.start_time}</div>
                            <div className="appointment-time">End Time: {appointment.end_time}</div>
                            <div className="appointment-notes">Notes: {appointment.notes}</div>
                            <div className="appointment-dogs">Dogs: {appointment.dogs}</div>
                            <div className="appointment-type">Type: {appointment.type}</div>
                        </div>
                    ))
                ) : (
                    <p>No appointments found.</p>
                )}
            </div>
        </div>
    );
};

export default MyRadevou;