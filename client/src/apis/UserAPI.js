import axios from 'axios'
import links from './urls'

async function login(username, password)
{
    let url = links.login
    let data = {
        "username":username,
        "password":password
    
    }
    return await axios({
        method:'POST',
        url : url,
        data : data
    })
    .then((response)=>{
         return response
    }
    ).catch(
        (e)=>{
            console.log('Exception occures in Login API call.0',e);
            return e;
        }
    )
}

async function SignUp(username, password,email)
{
    let url = links.signup
    let data = {
        "Email": email,
        "username":username,
        "password":password
    
    }
    return axios.post({
        url: url,
        data: data
    })
    .then((response)=>{
         return response
    }
    )
}

const userhelper = {
    login,
    SignUp
}
export default userhelper;