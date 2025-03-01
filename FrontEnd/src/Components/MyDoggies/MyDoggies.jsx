import React from "react";
import axios from "axios";
import "./MyDoggies.css";

export default class MyDoggies extends React.Component {
    state = {
        doggies: []
    };

    componentDidMount() {
        // Φέρνουμε τα σκυλιά του χρήστη όταν φορτώνεται η σελίδα
        axios.get("http://127.0.0.1:8000/app/dogs/", {
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            }
        })
        .then((res) => {
            this.setState({ doggies: res.data });
        })
        .catch((err) => {
            console.error("Error fetching dogs:", err);
            alert("Πρόβλημα κατά την φόρτωση των σκύλων.");
        });
    }

    render() {
        return (
            <div className="container">
                <h1>My Doggies</h1>
                <ul className="dog-list">
                    {this.state.doggies.length > 0 ? (
                        this.state.doggies.map((dog) => (
                            <li key={dog.id} className="dog-item">
                                <div className="dog-name">{dog.dog_name}</div>
                                <div className="dog-details">Breed: {dog.breed}</div>
                                <div className="dog-details">Age: {dog.age} years old</div>
                                <div className="dog-details">Owner: {dog.owner_name}</div>
                            </li>
                        ))
                    ) : (
                        <p>No dogs found.</p>
                    )}
                </ul>
                <button onClick={() => alert("Add dog functionality coming soon!")}>Add Doggie</button>
            </div>
        );
    }
}
