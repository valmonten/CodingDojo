module.exports = {
    static_contents: function(request, response){
        if(request.url === '/'){
            fs.readFile('/index.html', 'utf8', function (errors, contents) {
              response.write(contents); 
              response.end();
            });
        }else{
            fs.readFile(request.url, 'utf8', function(errors, contents){
                response.write(contents);
                resonpnse.end();
            });
        }
    }

}