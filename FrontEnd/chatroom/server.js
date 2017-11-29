const express = require("express");
const path = require("path")

var app = express();

app.use(express.static(path.join(__dirname, "./static")));

const server = app.listen(8000, function() {
    console.log("listening on port 8000");
});

const io = require("socket.io").listen(server);

io.sockets.on('connection', function (socket) {
    console.log("Client/socket is connected!");
    console.log("Client/socket id is: ", socket.id);
    // all the server socket code goes in here
    socket.on("got_new_user", function(data){
        console.log(data.thename+ " connected to the socket!");
        io.emit("Show_user", {new_user: data.thename});
    })
  });