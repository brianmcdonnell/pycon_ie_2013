var express = require('express');
var app = express();

app.get('/hello', function(req, res){
  res.send('Hello from Nodejs via (expressjs)');
});

//app.listen(8080);
//console.log('Node listening on port 8080');
app.listen('/tmp/node_hello.sock');
console.log('Node listening at unix://tmp/node_hello.sock');
