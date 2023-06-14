#!/usr/bin/node
const { list } = require('./100-data');

// Create a new array using map
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log(list);
console.log(newList);
