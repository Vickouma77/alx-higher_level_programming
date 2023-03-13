#!/usr/bin/node
if (process.argv.length < 3) {
	console.log('Missing number of occurrences');
} else {
	const x = parseInt(process.argv[2]);
	if (isNaN(x)) {
		console.log('Missing number of occurrences');
	} else {
		const i = 0;
		while (i < x) {
			console.log('C is fun');
			i++;
		}
	}
}
