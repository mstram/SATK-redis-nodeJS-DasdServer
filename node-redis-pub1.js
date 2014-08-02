#!/home/action/.parts/bin/node
var redis = require('redis');

var uuid = require('node-uuid');

//redis.debug_mode = true;

var moment = require('moment');
moment().format();
var mytime = moment().format('MMMM Do YYYY, h:mm:ss a');

console.log("moment : ",moment);
var mytime = moment().format('MMMM Do YYYY, h:mm:ss a');
console.log("mytime : ",mytime);


var client1 = redis.createClient(10388,"pub-redis-10388.us-east-1-4.1.ec2.garantiadata.com");
var client2 = redis.createClient(10388,"pub-redis-10388.us-east-1-4.1.ec2.garantiadata.com");

var msg_count = 0;
//console.log("client1",client1);
//console.log("client2",client2);
//port, host, options)

//var client = redis.createClient();  // localhost instance

client1.on("error", function (err) {
    console.log("(client1)error event - " + client1.host + ":" + client1.port + " - " + err);
});

client2.on("error", function (err) {
    console.log("(client2)error event - " + client2.host + ":" + client2.port + " - " + err);
});


var chan = "herc";
//var cmd = "SATK-rdRec";
var OP = 'SATK-wrtRec';
//var cmd = "BOGUS";
client1.subscribe(chan);

//client2.hmset(cmd,'tag','NodeJs(PC)','id',987,'cyl',0,'hd',5,'r','42', redis.print);



var uuid = uuid.v1();
client2.hmset(uuid,
                  'OP',OP,
                  'id','102',
                  'cyl','6',
                  'hd','1',
                  'r','1',
                  'k','456',
                  'd','more stuff here',
                  redis.print
                 );


var req = {'uuid':uuid,
                   'OP': OP,
                   'id': 100,
                  'cyl': 8,
                   'hd': 4,
                    'recn': 1,
                    'key': 'ABC',
                    'data': 'A record here'
                 };

//client2.lpush('q',uuid);
client2.lpush('q',JSON.stringify(req));

var msg = 'q';
client1.on("subscribe", function (chan, count) {
        console.log("client1.on(subscribe'  .. sending msg with client2");
        //client2.publish("a nice channel", "I am sending a message.");
        client2.publish(chan,msg,redis.print);
    });

// n.toString()

client1.on("message", function (chanl, msg) {
        console.log("(client1)(on.'message') chan " + chan + " msg: " + msg + "  msg_count:" + msg_count);
        msg_count += 1;
        s = msg_count.toString()
        //client2.publish(chan,'(PCTest #' + s +')',redis.print);

         //if (chanl == chan && msg == cmd) {

          if (msg_count == 4) {   // 3

           console.log("quitting on msg_count == 3");
           console.log("quitting on chanl == chan && msg == cmd");
            client1.unsubscribe();
            client1.end();
            client2.end();
        }
    });

function dump1(){
  console.log("(dump1)")
//  client2.hkeys(cmd, function (err, replies) {
    client2.hkeys(msg, function (err, replies) {
    if (err) {
        return console.error("error response - " + err);
    }
    console.log(replies.length + " replies:");
    replies.forEach(function (reply, i) {
        console.log(" reply:   " + i + ": " + reply);
      //  console.log(" reply.value:   " + i + ": " + reply.value);

    });
 });
}

dump1();
console.log("other stuff #1 after dump1()");
//client2.publish(chan,'(EXTERN#',redis.print);


/*
client1.quit(function (err, res) {
    console.log("(client1) Exiting from quit command.");
});

client2.quit(function (err, res) {
    console.log("(client2) Exiting from quit command.");
});
*/



