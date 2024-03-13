var host = 'http://127.0.0.1'
var port = ':5000'
var paths = 
{
    login : '/api/user/login',
    signup  : '/api/user/add_user',
    hello : '/api/hello/message',
    saveCsvToDb: '/api/files/saveCsvToDb'
}
var links = {
    login : host+port + paths.login,
    signup : host + port + paths.signup,
    hello : host+ port + paths.hello,
    saveCsvToDb : host + port + paths.saveCsvToDb
}

export default links;