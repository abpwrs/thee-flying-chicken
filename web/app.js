var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var http = require('http');
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

// MongoDB setup
// ///////////////////////////////
//Import the mongoose module
var mongoose = require('mongoose');

var mongoDB = 'mongodb://127.0.0.1/tfc';
mongoose.connect(mongoDB);
// Get Mongoose to use the global promise library
mongoose.Promise = global.Promise;
//Get the default connection
var db = mongoose.connection;
//Bind connection to error event (to get notification of connection errors)
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
// ///////////////////////////////


// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// Project specific routes
// ////////////////////////////////
app.use('/', indexRouter);
app.use('/example', exampleRouter);
// ////////////////////////////////


// catch 404 and forward to error handler
app.use(function (req, res, next) {
    next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err : {};

    // render the error page
    res.status(err.status || 500);
    res.render('error');
});

app.listen(5000, () => {
    console.log("Listening on port " + 5000);
    app.emit('APP_STARTED')
});

module.exports = app;
