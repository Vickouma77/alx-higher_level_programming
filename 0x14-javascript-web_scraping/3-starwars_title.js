#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/${movieId}';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    if (movieData.episode_id === parseInt(movieId)) {
      console.log(movieData.title);
    } else {
      console.log(`No movie found with episode id ${movieId}`);
    }
  }
});
