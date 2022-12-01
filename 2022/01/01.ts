import fs from "fs";

const inp = fs
	.readFileSync("./01.in", "utf-8")
	.split("\n\n")
	.map((line) =>
		line
			.split("\n")
			.map(Number)
			.reduce((a, b) => a + b, 0)
	)
	.sort((a, b) => b - a);

const part1 = Math.max(...inp);
console.log("Part 1:", part1);

const part2 = inp.slice(0, 3).reduce((a, b) => a + b, 0);
console.log("Part 2:", part2);
