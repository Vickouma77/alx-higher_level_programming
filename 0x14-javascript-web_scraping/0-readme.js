#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];

fs.readFile(path, 'utf-8', (error, content) => {
  if (error) {
    console.error(error);
  } else {
    console.log(content);
  }
});
