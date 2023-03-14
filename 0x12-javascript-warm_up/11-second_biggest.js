#!/usr/bin/node
const list = process.argv.slice(2).map(arg => parseInt(arg));
if (list.length === 0 || list.length === 1) {
  console.log(0);
} else {
  const sortedList = list.sort((a, b) => b - a);
  console.log(sortedList[1]);
}
