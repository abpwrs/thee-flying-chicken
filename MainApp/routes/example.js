var express = require('express');
var router = express.Router();
var Example = require('../models/example');

/* GET Example */
router.get('/', function (req, res, next) {
    res.render('example/index');
    next();
});

/* GET Example */
router.get('/:id', function (req, res, next) {
    res.render('example/example', {tag: req.param('id')});
    next();
});
router.post('/', function (req, res, next) {

});

module.exports = router;
