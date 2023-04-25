#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:' + response.statusCode);
  }
});
