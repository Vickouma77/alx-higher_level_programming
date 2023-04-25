#!/usr/bin/node

const request = require('request');
const urlValue = process.argv[1];
const option = { method: 'GET' };

request(option, urlValue, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
