#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(apiUrl + movieId,  (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
	  const responseJs = JSON.parse(body);
	  console.log('code: ' + response.statusCode);
  }
});
