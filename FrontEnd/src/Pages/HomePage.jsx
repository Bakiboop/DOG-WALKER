

import DogWalking from '../images/Dog Walking_2.jpg';
import PetSitting from '../images/PetSitting_2.jpg';
import Filoksenia from '../images/Filoksenia.jpg';
import PetTaxi from '../images/PetTaxi.jpg';

import Header from '../Components/Header/Header.jsx'
import Footer from '../Components/Footer'
import CardService from '../Components/CardService/CardService.jsx'

function HomePage() {


  return (
    <>
        <Header />
        <hr></hr>
        <h1 style={{ textAlign: 'center' }}>Υπηρεσίες</h1>
        <CardService image={DogWalking} service="Dog Walking - Βόλτα Σκύλου" details = "ΒΓΑΖΩ ΤΟΝ ΣΚΥΛΟ ΣΑΣ ΒΟΛΤΑ" />
        <CardService image={Filoksenia} service="Pet Boarding - Φιλοξενεία στο Χώρο του Κατοικιδίου" details = "Κρατώ τον Σκύλο σας στον χώρο σας" />
        <CardService image={PetSitting} service="Pet Sitting - Φιλοξενία στο Χώρο μου" details = "Φιλοξενώ τον σκύλο σας στον χώρο μου" />
        <CardService image={PetTaxi} service="Pet Taxi - Ταξί για τον σκύλο σας" details = "Ταξί για όλα τα κατοικίδιά σας" />
        <Footer />
        </>
  );
}

export default HomePage;