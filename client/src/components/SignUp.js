import './SignUp.css'
import { Form, Button } from 'react-bootstrap';
import React from 'react'

function SignUp() {
    return (
        <div className='signup_container'>
            <Form className='SingUp Form'>
                <h2>SignUp</h2>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Email address</Form.Label>
                    <Form.Control type="email" placeholder="Enter email" />
                    <Form.Text className="text-muted">
                        We'll never share your email with anyone else.
                    </Form.Text>
                </Form.Group>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>UserName</Form.Label>
                    <Form.Control type="email" placeholder="Enter email" />
                    <Form.Text className="text-muted">
                        UserName should be unique
                    </Form.Text>
                </Form.Group>


                <Form.Group className="mb-3" controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" />
                </Form.Group>
             
                <Button variant="primary" type="submit" className='summit_btn'>
                    Submit
                </Button>
            </Form>

        </div>
    )
}

export default SignUp