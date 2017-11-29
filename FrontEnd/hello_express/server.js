var express = require('express');
var session = require('express-session');
var app = express();

app.use(express.static(__dirname + "/static"));
app.use(express.static('style.css'));
app.use(session({secret: 'codingdoafd', resave: true, saveUninitialized: true}));

console.log(__dirname)

app.get('/', function(request, response) {
    response.send("<h1>Hello Express</h1>");
  });




// This sets the location where express will look for the ejs views
app.set('views', __dirname + '/views'); 
// Now lets set the view engine itself so that express knows that we are using ejs as opposed to another templating engine like jade
app.set('view engine', 'ejs');

app.get("/users", function (request, response){
    // hard-coded user data
    var users_array = [
        {name: "Michael", email: "michael@codingdojo.com"}, 
        {name: "Jay", email: "jay@codingdojo.com"}, 
        {name: "Brendan", email: "brendan@codingdojo.com"}, 
        {name: "Andrew", email: "andrew@codingdojo.com"}
    ];
    response.render('users', {users: users_array});
})
app.get("/main", function (request, response){
  if(!request.session.gold){
    request.session.gold=0;
  }
  response.render('main', {gold: request.session.gold});
});

app.post('/farming', function(request, response){

  request.session.gold++;
  response.redirect("/main");
});
app.post('/robbing', function(request, response){
  request.session.gold += 10;
  response.redirect("/main");
});
app.post('/gambling', function(request, response){
  response.redirect("/main");
  // random between -50 and 50 gold earned or losts
});


  app.listen(8000, function() {
    console.log("listening on port 8000");
  })