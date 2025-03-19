import React, { useState, useEffect } from "react";
import axios from "axios";
import "./MyRadevou.css"; // Import your CSS for styling

const MyRadevou = () => {
    const [appointments, setAppointments] = useState([]);
    const [editingAppointment, setEditingAppointment] = useState(null); // For editing an appointment
    const [updatedNotes, setUpdatedNotes] = useState(""); // For updating the notes

    // Fetch appointments when the component mounts
    useEffect(() => {
        fetchAppointments();
    }, []);

    // Fetch appointments from the backend
    const fetchAppointments = () => {
        const token = localStorage.getItem("token");
        if (!token) {
            window.location.href = "/login"; // Redirect if the user is not logged in
            return;
        }

        // GET request to fetch appointments
        axios.get("http://127.0.0.1:8000/api/appointments/", {
            headers: { "Authorization": `Token ${token}` }
        })
        .then((res) => {
            setAppointments(res.data); // Save the fetched data in state
            
        })
        .catch((err) => {
            console.error("Error fetching appointments:", err);
            alert("Πρόβλημα κατά την φόρτωση των ραντεβού.");
        });
    };

    // Handle deleting an appointment
    const handleDelete = (appointment) => {
        const token = localStorage.getItem("token");
        if (!token) {
            window.location.href = "/login";
            return;
        }

        // Include start_time and type in the request body
        const deleteData = {
            start_time: appointment.start_time,
            type: appointment.type,
        };

        // DELETE request to delete the appointment
        axios.delete(`http://127.0.0.1:8000/api/appointments/`, {
            headers: { "Authorization": `Token ${token}` },
            data: deleteData, // Send data in the request body
        })
        .then(() => {
            alert("Το ραντεβού διαγράφηκε επιτυχώς.");
            // Update the appointments list after deletion
            setAppointments(appointments.filter(a => a.id !== appointment.id));
            fetchAppointments();
        })
        .catch((err) => {
            console.error("Error deleting appointment:", err);
            alert("Πρόβλημα κατά τη διαγραφή του ραντεβού.");
        });
    };

    // Handle clicking the "Update" button
    const handleUpdateClick = (appointment) => {
        // Set the appointment being edited and initialize the notes field
        setEditingAppointment(appointment);
        setUpdatedNotes(appointment.notes);
    };

    // Handle submitting the updated appointment
    const handleUpdateSubmit = () => {
        const token = localStorage.getItem("token");
        if (!token) {
            window.location.href = "/login";
            return;
        }

        // Include start_time and type in the updated data
        const updatedAppointment = {
            ...editingAppointment,
            notes: updatedNotes,
            start_time: editingAppointment.start_time, // Include start_time
            type: editingAppointment.type, // Include type
        };

        // PUT request to update the appointment
        axios.put(`http://127.0.0.1:8000/api/appointments/`, updatedAppointment, {
            headers: { "Authorization": `Token ${token}` }
        })
        .then(() => {
            alert("Το ραντεβού ενημερώθηκε επιτυχώς.");
            // Update the appointments list after the update
            setAppointments(appointments.map(appointment =>
                appointment.id === editingAppointment.id ? updatedAppointment : appointment
            ));
            fetchAppointments();
            setEditingAppointment(null); // Close the edit modal
        })
        .catch((err) => {
            console.error("Error updating appointment:", err);
            alert("Πρόβλημα κατά την ενημέρωση του ραντεβού.");
        });
    };

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
                            <button onClick={() => handleUpdateClick(appointment)}>Update</button>
                            <button onClick={() => handleDelete(appointment)}>Delete</button>
                        </div>
                    ))
                ) : (
                    <p>No appointments found.</p>
                )}
            </div>

            {/* Edit modal for updating an appointment */}
            {editingAppointment && (
                <div className="edit-modal">
                    <h2>Edit Appointment</h2>
                    <div>
                        <label>Notes:</label>
                        <textarea
                            value={updatedNotes}
                            onChange={(e) => setUpdatedNotes(e.target.value)}
                        />
                    </div>
                    <button onClick={handleUpdateSubmit}>Save Changes</button>
                    <button onClick={() => setEditingAppointment(null)}>Cancel</button>
                </div>
            )}
        </div>
    );
};

export default MyRadevou;