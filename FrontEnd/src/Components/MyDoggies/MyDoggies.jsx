import React, { useState, useEffect } from "react";
import "./MyDoggies.css";

function MyDoggies() {
    const [doggies, setDoggies] = useState([]);

    // Φόρτωση σκύλων από το Django backend
    useEffect(() => {
        fetch("http://localhost:8000/api/dogs/", {
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("token")}` // Χρειάζεται authentication
            }
        })
            .then(response => response.json())
            .then(data => setDoggies(data))
            .catch(error => console.error("Error fetching dogs:", error));
    }, []);

    // Προσθήκη νέου σκύλου
    const addDoggie = async () => {
        const dog_name = prompt("Enter dog's name:");
        const breed = prompt("Enter dog's breed:");
        const age = prompt("Enter dog's age:");

        if (dog_name && breed && age) {
            try {
                const response = await fetch("http://localhost:8000/api/dogs/", {
                    method: "POST",
                    headers: { 
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${localStorage.getItem("token")}`
                    },
                    body: JSON.stringify({ dog_name, breed, age }),
                });

                if (response.ok) {
                    const newDog = await response.json();
                    setDoggies([...doggies, newDog]); // Προσθήκη στο state
                } else {
                    console.error("Failed to add dog");
                }
            } catch (error) {
                console.error("Error adding dog:", error);
            }
        }
    };

    return (
        <div>
            <h1>My Doggies</h1>
            <ul>
                {doggies.map((dog) => (
                    <li key={dog.id}>
                        <strong>{dog.dog_name}</strong> ({dog.breed}, {dog.age} years old)
                    </li>
                ))}
            </ul>
            <button onClick={addDoggie}>Add Doggie</button>
        </div>
    );
}

export default MyDoggies;
