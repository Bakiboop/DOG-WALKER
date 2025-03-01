import React from 'react';
import './Login.css'; 
import axios from 'axios';



export default class Login extends React.Component {
    state = {
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        phone_number: '',
        address: ''
    };



    handleChange = (event) => {
        const { name, value } = event.target; 
        this.setState({ [name]: value }); 
    };

    handleSubmitLogin = (event) => {
        event.preventDefault();
        const { email, password } = this.state; // Χρήση του state
        const user = { email, password }; // Δημιουργία του user
        axios.post('http://127.0.0.1:8000/user/login/', user, {
            headers:{
                'Content-Type': 'application/json'
            }
        })
        .then((res) => { 
            if (res.data.token) {
                localStorage.setItem('token', res.data.token);
                alert('Η Σύνδεση ήταν επιτυχής!');
                this.setState({
                    email: '',
                    password: '',
                });
            } else {
                alert('Δεν ελήφθη token από τον server.');
            }
        })
        .catch((err) => {
            console.error('Error:', err);
            alert('Υπήρξε πρόβλημα κατά την σύνδεση.');
        });
    }

    handleSubmit = (event) => {
        event.preventDefault();

        const { first_name, last_name, email, phone_number, address, password } = this.state;
        const user = { first_name, last_name, email, phone_number, address, password };

        console.log(user);
        axios.post('http://127.0.0.1:8000/user/signup/', user, {
            headers:{
                'Content-Type': 'application/json'
            }
        })
            .then((res) => { 
                console.log('Response:', res);
                console.log('Data:', res.data);
                alert('Η εγγραφή ήταν επιτυχής!');
                this.setState({
                    first_name: '',
                    last_name: '',
                    email: '',
                    password: '',
                    phone_number: '',
                    address: ''
                });
            })
            .catch((err) => {
                console.error('Error:', err);
                alert('Υπήρξε πρόβλημα κατά την εγγραφή.');
            });
    };




render() {
    return (
        <div className="loginWrapper">
        <div className="main">
            <input className= "loginInput" type="checkbox" id="chk" aria-hidden="true" />
        
            <div className="signup">
                <form onSubmit={this.handleSubmit}>
                    <label className='loginlabel' htmlFor="chk" aria-hidden="true">Sign up</label>

                    <input className= "loginInput" type="text" name="first_name" placeholder="First Name" value={this.state.first_name} onChange ={this.handleChange}  required />
                    <input className= "loginInput" type="text" name="last_name" placeholder="Last Name" value={this.state.last_name} onChange ={this.handleChange}  required />
                    <input className= "loginInput" type="email" name="email" placeholder="Email" value={this.state.email} onChange ={this.handleChange} required />
                    <input className= "loginInput" type="text" name="phone_number" placeholder="Τηλέφωνο" value={this.state.phone_number} onChange ={this.handleChange} required />
                    <input className= "loginInput" type="text" name="address" placeholder="Διεύθυνση"  value={this.state.address} onChange ={this.handleChange} required />
                    <input className= "loginInput" type="password" name="password" placeholder="Password" value={this.state.password} onChange ={this.handleChange} required />
                    <button className='loginbutton' type='submit' >Sign up</button>
                </form>
            </div>
        
            <div className="login">
                <form onSubmit={this.handleSubmitLogin}>
                    <label className='loginlabel' htmlFor="chk" aria-hidden="true">Login</label>
                    <input className= "loginInput" type="email" name="email" placeholder="Email" required value={this.state.email} onChange={this.handleChange}/>
                    <input className= "loginInput" type="password" name="password" placeholder="Password" required  value={this.state.password} onChange={this.handleChange}/>
                    <button className='loginbutton'>Login</button>
                </form>
            </div>
        </div>
        </div>
    );
}
}