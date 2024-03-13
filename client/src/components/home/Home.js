import React, { useEffect, useState } from 'react'
import './Home.css'
import homeAPIhelper from '../../apis/HomeAPis'
import { Button } from 'react-bootstrap'
import { useNavigate } from 'react-router-dom'
function Home() {
    const [isAuthorized, setIsAuthorized] = useState(false)
    const [message, setMessage] = useState('')
    useEffect(() => {
      fetchHome()
    
      return () => {
        
      }
    }, [])
    const navigation = useNavigate()
    async function fetchHome()
    {
        var resposne = await homeAPIhelper.Hello();
        let data = resposne.data
        let error = data.error;
        let message = data.message;
        console.log('data is ',data);
        console.log('error is ',error);
        if(error === undefined)
        {
          setIsAuthorized(true)
          
        }
        setMessage(message)
        console.log('Hello resposne ',resposne);
        
    }
    function LoginHandler()
    {
      navigation('/login')
    }
  return (
    <div className='home_container'>
      <h2>{message}</h2>
      {(isAuthorized===false)?(
      <>
      <br/>
      <Button onClick={LoginHandler}>Login</Button>
      </>):''}
    </div>
  )
}

export default Home