
import './Login.css'
import React from 'react'
import {Form,Button} from 'react-bootstrap';
function Login() {
    return (
        <div className='Login_container'>
            <Form title='Login Form' className='LoginForm'>
            <h2>Login Form</h2>
                <Form.Group className="mb-3" controlId="formGroupEmail">
                    <Form.Label>Email address</Form.Label>
                    <Form.Control type="email" placeholder="Enter email" />
                </Form.Group>
                <Form.Group className="mb-3" controlId="formGroupPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" />
                </Form.Group>
                
            <Button>Login</Button>
            </Form>
        </div>
    )
}

export default Login