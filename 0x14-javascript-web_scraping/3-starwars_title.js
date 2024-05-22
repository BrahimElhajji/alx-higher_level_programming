#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const movieData = JSON.parse(body);
    console.log(`${movieData.title}`);
  }
});
