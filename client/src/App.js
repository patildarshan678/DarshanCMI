import './App.css';
import Login from './components/Login';
import SignUp from './components/SignUp';
import {Router, Route, Routes} from  'react-router-dom';
import Home from './components/home/Home';
function App() {
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
