//Require Mongoose
const mongoose = require('mongoose');

//Define a schema
const Schema = mongoose.Schema;

const Example = new Schema({
    a_string: String,
});


//Export function to create "SomeModel" model class
module.exports = mongoose.model('Example', Example);