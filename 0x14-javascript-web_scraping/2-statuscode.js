#!/usr/bin/node

const request = require('request');
const urlValue = process.argv[2];

request(urlValue, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:' + response.statusCode);
  }
});
