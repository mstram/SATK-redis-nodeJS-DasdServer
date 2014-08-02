#!/home/action/.parts/bin/node
var redis = require("redis");

//var client = redis.createClient();  // localhost instance

var client = redis.createClient(10388,"pub-redis-10388.us-east-1-4.1.ec2.garantiadata.com");

client.on("error", function (err) {
    console.log("error event - " + client.host + ":" + client.port + " - " + err);
});

client.set("Simple_Node_redis:stringkey", "zopper", redis.print);
client.hset("Simple_Node_redis:hash", "hashtest 1", "some value", redis.print);

// mike
//client.hmset("Simple_Node_redis:hmset",{'k1',42,'k2',77},redis.print);
client.hmset("Simple_Node_redis:hmset",'k1',42,'k2',77,redis.print);
// ----------

client.hkeys("hash key", function (err, replies) {
    if (err) {
        return console.error("error response - " + err);
    }

    console.log(replies.length + " replies:");
    replies.forEach(function (reply, i) {
        console.log("    " + i + ": " + reply);
    });
});

client.quit(function (err, res) {
    console.log("Exiting from quit command.");
});
