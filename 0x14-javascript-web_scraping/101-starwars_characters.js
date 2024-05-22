#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const film = JSON.parse(body);
  const charactersUrl = film.characters;
  charactersUrl.forEach((url) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
