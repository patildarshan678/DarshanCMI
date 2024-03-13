import axios from "axios";
import links from "./urls";
async function Hello()
{
    let url = links.hello
    let headers = {
        'Access-Control-Allow-Origin': 'http://localhost:3000'
    }
    return await axios(
        {method:'GET',
        url : url,
        headers : headers
    }
    )
    .then((response => {
        console.log(response);
        return response;
    })).catch(
        (ex)=>{
            console.log('Exception occured wile calling hello API.',ex);
            return ex;
        }
    )

}

const homeAPIhelper = {
    Hello
}
export default homeAPIhelper;