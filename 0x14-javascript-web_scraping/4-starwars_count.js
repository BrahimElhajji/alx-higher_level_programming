#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const movies = JSON.parse(body).results;
    const wedgeMovies = movies.filter(movie => {
      return movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
    });
    console.log(`${wedgeMovies.length}`);
  }
});
