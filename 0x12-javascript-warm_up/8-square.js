#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let square = '';
    for (let j = 0; j < size; j++) square += 'X';
    console.log(square);
  }
}
