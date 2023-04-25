#!/usr/bin/node

const fs = require('fs');
const request = require('require');


request(process.argv[2], function (err, response, body) {
  if (err == null) {
    fs.writeFileSync(process.argv[3], body);
  }
});
