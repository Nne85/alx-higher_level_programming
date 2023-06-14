#!/usr/bin/node
const { dict } = require('./101-data');

// Initialize the new dictionary
const newDict = {};

// Iterate over the keys and values of the input dictionary
for (const [userId, occurrence] of Object.entries(dict)) {
  // If the occurrence is already a key in the new dictionary, push the user ID to the corresponding array
  if (occurrence in newDict) {
    newDict[occurrence].push(userId);
  } else {
    // Otherwise, create a new array with the user ID as the value for the occurrence key
    newDict[occurrence] = [userId];
  }
}

// Print the new dictionary
console.log(newDict);
