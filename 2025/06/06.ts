import { bench, run } from "mitata";
import assert from "node:assert";
import { readInput } from "../utils";

const input = await readInput();

function partOne() {
	const rows = input
		.slice(0, -1)
		.map((row) => row.trim().split(/\s+/).map(Number));
	const ops = input.at(-1)!.trim().split(/\s+/);

	let partOne = 0;

	for (const [i, op] of ops.entries()) {
		const func = {
			"+": (a: number, b: number) => a + b,
			"*": (a: number, b: number) => a * b,
		}[op];

		assert(func);

		let answer = rows[0][i];

		for (const row of rows.slice(1)) {
			answer = func(answer, row[i]);
		}

		partOne += answer;
	}

	return partOne;
}

function partTwo() {
	const numCols = input[0].length;
	const numRows = input.length;

	const transposedInput = [];

	let partTwo = 0;

	for (let i = 0; i < numCols; i++) {
		const items = [];

		for (let j = 0; j < numRows; j++) {
			items.unshift(input[j][i]);
		}

		const [op, ...nums] = items;

		const finalNum = nums.toReversed().join("").trim();

		transposedInput.push([op, Number(finalNum) || undefined] as const);
	}

	let currentOp;
	let nums = [];

	for (const row of transposedInput) {
		const [op, num] = row;

		if (num === undefined) {
			assert(currentOp);
			const func = {
				"+": (a: number, b: number) => a + b,
				"*": (a: number, b: number) => a * b,
			}[currentOp];

			assert(func);
			partTwo += nums.reduce(func);

			nums = [];

			continue;
		}

		if (op !== " ") currentOp = op;
		nums.push(num);
	}

	assert(currentOp);
	const func = {
		"+": (a: number, b: number) => a + b,
		"*": (a: number, b: number) => a * b,
	}[currentOp];

	assert(func);
	partTwo += nums.reduce(func);

	return partTwo;
}

console.log("Part 1:", partOne());
console.log("Part 2:", partTwo());

bench("Part 1", partOne);
bench("Part 2", partTwo);
run();
