const fs = require("fs");

input = fs.readFileSync(process.argv[2], "utf-8").split("\n").map(Number);

console.time("Part 1: version 1");
for (let i = 0; i < input.length; i++) {
	for (let j = i; j < input.length; j++) {
		let a = input[i];
		let b = input[j];
		if (a + b === 2020) {
			console.log(a * b);
		}
	}
}
console.timeEnd("Part 1: version 1");

for (let i = 0; i < input.length; i++) {
	for (let j = i; j < input.length; j++) {
		for (let k = 0; k < input.length; k++) {
			const a = input[i];
			const b = input[j];
			const c = input[k];
			if (a + b + c === 2020) {
				console.log(a * b * c);
			}
		}
	}
}
