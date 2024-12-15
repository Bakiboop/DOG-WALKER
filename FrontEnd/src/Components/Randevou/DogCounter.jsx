import React, { useState } from 'react';

function DogCounter() {
    const [dogCount, setDogCount] = useState(1); // Αρχικοποίηση του counter με την τιμή 1
    const [dogWeights, setDogWeights] = useState(['']); // Κρατάμε τα βάρη για κάθε σκύλο

    const handleCountChange = (e) => {
        const value = Math.max(1, parseInt(e.target.value) || 1); // Ελάχιστη τιμή το 1
        setDogCount(value);

        // Προσαρμόζουμε τον πίνακα με τα βάρη ανάλογα με τον αριθμό των σκύλων
        if (value > dogWeights.length) {
            setDogWeights([...dogWeights, ...Array(value - dogWeights.length).fill('')]);
        } else {
            setDogWeights(dogWeights.slice(0, value));
        }
    };

    const handleWeightChange = (index, value) => {
        const updatedWeights = [...dogWeights];
        updatedWeights[index] = value;
        setDogWeights(updatedWeights); // Ενημέρωση του array με τα βάρη
    };

    return (
        <div>
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

            {/* Input boxes για τα βάρη των σκύλων */}
            <div>
                {dogWeights.map((weight, index) => (
                    <div key={index} style={{ marginBottom: '10px' }}>
                        <label>Βάρος {index + 1}ου σκυλάκου:</label>
                        <input
                            type="number"
                            placeholder="Εισάγετε βάρος (κιλά)"
                            value={weight}
                            onChange={(e) => handleWeightChange(index, e.target.value)}
                            style={{ marginLeft: '10px' }}
                        />
                    </div>
                ))}
            </div>
        </div>
    );
}

export default DogCounter;
