#!/home/action/.parts/bin/node
var redis = require('redis');
var uuid = require('node-uuid');
//redis.debug_mode = true;

var moment = require('moment');
moment().format();
var mytime = moment().format('MMMM Do YYYY, h:mm:ss a');

//var client = redis.createClient();  // localhost redis instance

var client1 = redis.createClient(10388,"pub-redis-10388.us-east-1-4.1.ec2.garantiadata.com");
var client2 = redis.createClient(10388,"pub-redis-10388.us-east-1-4.1.ec2.garantiadata.com");
var msg_count = 0;
//console.log("client1",client1);
//console.log("client2",client2);


client1.on("error", function (err) {
    console.log("(client1)error event - " + client1.host + ":" + client1.port + " - " + err);
});

client2.on("error", function (err) {
    console.log("(client2)error event - " + client2.host + ":" + client2.port + " - " + err);
});

function d1(){
  client.hkeys("node-pc-hmset", function (err, replies) {
    if (err) {
        return console.error("error response - " + err);
    }
    console.log(replies.length + " replies:");
    replies.forEach(function (reply, i) {
        console.log("    " + i + ": " + reply);
    });
 });
}


// list command ? ... append to list instead

///////////////////
var chan = "herc";
//var OP = "SATK-rdRec";
var OP = 'SATK-wrtRec';
client1.subscribe(chan);

//client2.hmset(cmd,'lang','NodeJs,'host','Nitrous','id','1','cyl','0','hd','5','r',42);

var uuid = uuid.v1(); 
client2.hmset(uuid,'OP',OP
                  'id',135,
                  'cyl',6,
                  'hd',1,
                  'r','1',
                  'k','42',
                  'd','What is the meaning of life ?',
                  redis.print
                 );

client2.lpush('q',uuid);

msg = 'q';
client1.on("subscribe", function (chan, count) {
   console.log("client1.on(subscribe'  .. sending msg with client2");
        //client2.publish("a nice channel", "I am sending a message.");
   //client2.publish(chan,cmd,redis.print);
  client2.publish(chan,msg,redis.print);
 });

    client1.on("message", function (chanl, msg) {
        console.log("client1 channel " + chan + ": " + msg);
        msg_count += 1;

       if (chanl == chan && msg == cmd) {
          console.log("ending on (chanl == chan && msg == cmd)");
       // if (msg_count === 3) {
              client1.unsubscribe();
            client1.end();
            client2.end();
        }
    });

/*
client1.quit(function (err, res) {
    console.log("(client1) Exiting from quit command.");
});

client2.quit(function (err, res) {
    console.log("(client2) Exiting from quit command.");
});
*/

