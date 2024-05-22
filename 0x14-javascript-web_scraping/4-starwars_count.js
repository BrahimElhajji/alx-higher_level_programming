#!/usr/bin/node
const request = require('request');
const API_URL = process.argv[2];
let movieCount = 0;

request(API_URL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movies = JSON.parse(body).results;
  movies.forEach((movie) => {
    movie.characters.forEach((charUrl) => {
      if (charUrl.endsWith('/18/')) {
        movieCount += 1;
      }
    });
  });
  console.log(movieCount);
});
