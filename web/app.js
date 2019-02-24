var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

// Project specific routes
// ///////////////////////////////
var indexRouter = require('./routes/index');
var exampleRouter = require('./routes/example');
// ///////////////////////////////

var app = express();

// helmet is a security middleware
// ///////////////////////////////
var helmet = require('helmet');
app.use(helmet());
// ///////////////////////////////

// disable feature to avoid
// node.js targeted attacks
// ///////////////////////////////
app.disable('x-powered-by');
// ///////////////////////////////

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// Project specific routes
// ////////////////////////////////
app.use('/', indexRouter);
app.use('/example', exampleRouter);
// ////////////////////////////////


// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

server = app.listen();

module.exports = app;
