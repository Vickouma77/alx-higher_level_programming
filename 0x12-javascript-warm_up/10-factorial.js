#!/usr/bin/node
function factNumber (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  } else {
    return n * factNumber(n - 1);
  }
}
const num = parseInt(process.argv[2]);
const result = factNumber(num);
console.log(result);
