#!/usr/bin/node

function factorial (n) {
	if (n > 0) {
		return num * factorial(n - 1);
	}
	return 1;
}

console.log(factorial(Number(process.argv[2])));
