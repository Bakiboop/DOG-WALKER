import React from 'react';

import './Login.css'; 


function Login() {
    return (
        <div className="loginWrapper">
        <div className="main">
            <input className= "loginInput" type="checkbox" id="chk" aria-hidden="true" />
        
            <div className="signup">
                <form>
                    <label className='loginlabel' htmlFor="chk" aria-hidden="true">Sign up</label>

                    <input className= "loginInput" type="text" name="txt" placeholder="First Name"  required />
                    <input className= "loginInput" type="text" name="txt" placeholder="Last Name"  required />
                    <input className= "loginInput" type="email" name="email" placeholder="Email" required />
                    <input className= "loginInput" type="text" name="broj" placeholder="Τηλέφωνο" required />
                    <input className= "loginInput" type="text" name="txt" placeholder="Διεύθυνση"  required />
                    <input className= "loginInput" type="password" name="pswd" placeholder="Password" required />
                    <button className='loginbutton'>Sign up</button>
                </form>
            </div>
        
            <div className="login">
                <form>
                    <label className='loginlabel' htmlFor="chk" aria-hidden="true">Login</label>
                    <input className= "loginInput" type="email" name="email" placeholder="Email" required />
                    <input className= "loginInput" type="password" name="pswd" placeholder="Password" required />
                    <button className='loginbutton'>Login</button>
                </form>
            </div>
        </div>
        </div>
    );
}

export default Login;
