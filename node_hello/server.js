var express = require('express');
var app = express();

app.get('/hello', function(req, res){
  res.send('Hello from Nodejs (via expressjs)');
});


function shutdown() {
    server.close(); // socket file is automatically removed here
    process.exit();
}
process.on('SIGINT', shutdown);

//app.listen(8080);
//console.log('Node listening on port 8080');
var server = app.listen('/tmp/node_hello.sock', '0.0.0.0', 8191);
console.log('Node listening at unix://tmp/node_hello.sock');
