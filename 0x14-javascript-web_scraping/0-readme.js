#!/usr/bin/node

const file = require("file");
const path = process.argv[2]

file.readFile(path, 'utf-8', (error, content) => {
	if (error) {
		console.error(error)
	} else {
		console.log(content)
	}
});
