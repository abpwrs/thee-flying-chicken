var express = require('express');
var app = express();

var square = require('./square');
app.get('/', function(req, res) {
  res.send('Hello World!');
});

app.all('/secret', function(req, res, next) {
  console.log('Accessing the secret section ...');
  next(); // pass control to the next handler
});

app.listen(3000, function() {
  console.log('Example app listening on port 3000!');
  console.log('the area of a 2x2 is ' + square.area(4));
});
