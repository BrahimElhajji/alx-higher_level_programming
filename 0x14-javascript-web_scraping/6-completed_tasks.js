#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const todos = JSON.parse(body);
  const userIds = {};
  todos.forEach((todo) => {
    if (todo.completed) {
      if (!userIds[todo.userId]) {
        userIds[todo.userId] = 0;
      }
      userIds[todo.userId]++;
    }
  });
  console.log(userIds);
});
