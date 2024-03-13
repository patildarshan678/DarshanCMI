
import './Login.css'
import React, { useState } from 'react'
import {Form,Button} from 'react-bootstrap';
import userhelper from '../apis/UserAPI';
import { useNavigate } from 'react-router-dom';
function Login() {
    const [UserName, setUserName] = useState('')
    const [password, setPassword] = useState('')
    const navigation = useNavigate()
    async function summithandler()
    {
        console.log('password state is ',password);
        console.log('username state is ',UserName);
        let loginresposne = await userhelper.login(UserName,password)
        console.log('login response ',loginresposne);
        let data  =loginresposne.data
        console.log('data is ',data);
        let error = data.error
        let message = data.message
        
        if(error === undefined)
        {
            navigation('/home')
        }
        else{
            alert(message)
        }

    }
    function passwordhanlder(params) {
        setPassword(params.target.value)
    }
    function UserNamehanlder(params) {
        setUserName(params.target.value)
    }
    return (
        <div className='Login_container'>
           <Form>
            <h2>Login From</h2>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Email address</Form.Label>
        <Form.Control type="email" placeholder="Enter email" onChange={UserNamehanlder}/>
        <Form.Text className="text-muted">
          We'll never share your email with anyone else.
        </Form.Text>
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" placeholder="Password" onChange={passwordhanlder}/>
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicCheckbox">
        <Form.Check type="checkbox" label="Check me out" />
      </Form.Group>
      <Button variant="primary" onClick={summithandler} >
        Submit
      </Button>
    </Form>
        </div>
    )
}

export default Login