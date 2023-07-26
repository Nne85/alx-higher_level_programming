#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);

    // Initialize an object to store the count of completed tasks per user
    const completedTasks = {};

    // Loop through each todo
    for (const todo of todos) {
      // Check if the todo is completed (completed === true)
      if (todo.completed) {
        // Increment the count of completed tasks for the user (userId)
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    }

    console.log(completedTasks);
  }
});
