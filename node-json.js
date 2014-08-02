 socket.on('chat', function  (data) {
    message = {user : data.message.user, message : data.message.message};
    chat_room.sockets.emit('chat', {message: message});

    jsonString = JSON.stringify(message);

    fs.appendFile("public/chat.json", jsonString, function(err) {
        if(err) {
            console.log(err);
        } else {
            console.log("The file was saved!");
        }
    }); 

  });