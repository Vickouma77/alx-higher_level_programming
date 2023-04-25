#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiURL = 'https://swapi-api.hbtn.io/api/films/';

request(apiURL + movieId, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
