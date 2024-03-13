import axios from "axios";
import links from "./urls";
async function Hello()
{
    let url = links.hello
    return await axios.get(url)
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