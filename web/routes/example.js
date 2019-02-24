var express = require('express');
var router = express.Router();

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

module.exports = router;
