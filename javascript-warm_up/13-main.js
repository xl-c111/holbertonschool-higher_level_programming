#!/usr/bin/node

// Using require('./13-add') to import the file 13-add.js
// add function is a property inside the add obj
const add = require('./13-add').add;
console.log(add(3, 5));
