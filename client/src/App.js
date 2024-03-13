import './App.css';
import Login from './components/Login';
import SignUp from './components/SignUp';
import { Route, Routes, useNavigate} from  'react-router-dom';
import Home from './components/home/Home';
import { useEffect } from 'react';
function App() {
  const navigation = useNavigate()
  useEffect(() => {
    navigation('/home')
  }, [])
  
  return (
    <div className="App">
      {/* <Login/> */}
      
        <Routes>
        <Route Component={Home} path='/home'/>
        <Route Component={Login} path='/login'/>
        <Route Component={SignUp} path='/signup'/>
        </Routes>
      
      
    </div>
  );
}

export default App;
