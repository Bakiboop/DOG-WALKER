import React, { useState, useEffect } from "react";
import axios from "axios";
import "./MyDoggies.css";

const MyDoggies = () => {
    const [doggies, setDoggies] = useState([]);
    const [newDog, setNewDog] = useState({ dog_name: "", breed: "", age: "", owner: "" });
    const [editingDog, setEditingDog] = useState(null);
    const [showForm, setShowForm] = useState(false);

    useEffect(() => {
        const token = localStorage.getItem("token");
        if (!token) {
            window.location.href = "/login";
            return;
        }

<<<<<<< HEAD
        axios.get("http://127.0.0.1:8000/api/dogs/", {
            headers: { "Authorization": `Bearer ${token}` }
=======
    componentDidMount() {
        // Φέρνουμε τα σκυλιά του χρήστη όταν φορτώνεται η σελίδα
        axios.get("http://127.0.0.1:8000/app/dogs/", {
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            }
>>>>>>> cc406b219452401a1a2921f13dd4b26ae18f5d81
        })
        .then((res) => {
            setDoggies(res.data);
        })
        .catch((err) => {
            console.error("Error fetching dogs:", err);
            alert("Πρόβλημα κατά την φόρτωση των σκύλων.");
        });
    }, []);

    const handleChange = (e) => {
        setNewDog({ ...newDog, [e.target.name]: e.target.value });
    };

    const addDog = () => {
        const token = localStorage.getItem("token");
        if (!newDog.dog_name || !newDog.breed || !newDog.age) {
            alert("Συμπληρώστε όλα τα πεδία!");
            return;
        }

        axios.post("http://127.0.0.1:8000/api/dogs/", newDog, {
            headers: { "Authorization": `Bearer ${token}`, "Content-Type": "application/json" }
        })
        .then((res) => {
            setDoggies([...doggies, res.data]);
            setNewDog({ dog_name: "", breed: "", age: "", owner: "" });
            setShowForm(false);
        })
        .catch((err) => {
            console.error("Error adding dog:", err);
            alert("Πρόβλημα κατά την προσθήκη του σκύλου.");
        });
    };

    const deleteDog = (id) => {
        const token = localStorage.getItem("token");
        if (window.confirm("Are you sure you want to delete this dog?")) {
            axios.delete(`http://127.0.0.1:8000/api/dogs/${id}/`, {
                headers: { "Authorization": `Bearer ${token}` }
            })
            .then(() => {
                setDoggies(doggies.filter(dog => dog.id !== id));
                alert("Dog deleted successfully!");
            })
            .catch((err) => {
                console.error("Error deleting dog:", err);
                alert("Πρόβλημα κατά τη διαγραφή του σκύλου.");
            });
        }
    };

    const handleEdit = (dog) => {
        setEditingDog(dog);
        setShowForm(true);
    };

    const updateDog = () => {
        const token = localStorage.getItem("token");
        if (!editingDog.dog_name || !editingDog.breed || !editingDog.age) {
            alert("Συμπληρώστε όλα τα πεδία!");
            return;
        }

        axios.put(`http://127.0.0.1:8000/api/dogs/${editingDog.id}/`, editingDog, {
            headers: { "Authorization": `Bearer ${token}`, "Content-Type": "application/json" }
        })
        .then((res) => {
            setDoggies(doggies.map(dog => dog.id === editingDog.id ? res.data : dog));
            setEditingDog(null);
            setShowForm(false);
            alert("Dog updated successfully!");
        })
        .catch((err) => {
            console.error("Error updating dog:", err);
            alert("Πρόβλημα κατά την ενημέρωση του σκύλου.");
        });
    };

    return (
        <div className="container">
            <h1>My Doggies</h1>

            <div className="dog-list">
                {doggies.length > 0 ? (
                    doggies.map((dog) => (
                        <div key={dog.id} className="dog-item">
                            <div className="dog-name">{dog.dog_name}</div>
                            <div className="dog-details">Breed: {dog.breed}</div>
                            <div className="dog-details">Age: {dog.age} years old</div>
                            <div className="dog-details">Owner: {dog.owner}</div>
                            <button className="edit-dog-btn" onClick={() => handleEdit(dog)}>Edit</button>
                            <button className="delete-dog-btn" onClick={() => deleteDog(dog.id)}>Delete</button>
                        </div>
                    ))
                ) : (
                    <p>No dogs found.</p>
                )}
            </div>

            <button className="add-dog-btn" onClick={() => { setEditingDog(null); setShowForm(!showForm); }}>
                {showForm ? "Cancel" : "Add Doggie"}
            </button>

            {showForm && (
                <div className="dog-form">
                    <input
                        type="text"
                        name="dog_name"
                        placeholder="Dog Name"
                        value={editingDog ? editingDog.dog_name : newDog.dog_name}
                        onChange={(e) => editingDog ? setEditingDog({ ...editingDog, dog_name: e.target.value }) : handleChange(e)}
                    />
                    <input
                        type="text"
                        name="breed"
                        placeholder="Breed"
                        value={editingDog ? editingDog.breed : newDog.breed}
                        onChange={(e) => editingDog ? setEditingDog({ ...editingDog, breed: e.target.value }) : handleChange(e)}
                    />
                    <input
                        type="number"
                        name="age"
                        placeholder="Age"
                        value={editingDog ? editingDog.age : newDog.age}
                        onChange={(e) => editingDog ? setEditingDog({ ...editingDog, age: e.target.value }) : handleChange(e)}
                    />
                    <input
                        type="text"
                        name="owner"
                        placeholder="Owner"
                        value={editingDog ? editingDog.owner : newDog.owner}
                        onChange={(e) => editingDog ? setEditingDog({ ...editingDog, owner: e.target.value }) : handleChange(e)}
                    />
                    <button className="submit-dog-btn" onClick={editingDog ? updateDog : addDog}>
                        {editingDog ? "Update" : "Submit"}
                    </button>
                </div>
            )}
        </div>
    );
};

export default MyDoggies;