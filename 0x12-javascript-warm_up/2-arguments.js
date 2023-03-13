#!/usr/bin/node

const count = process.arg.length;
console.log(count === 2 ? 'No argument found' : count === 3 ? 'Argument found' : 'Argument found');
