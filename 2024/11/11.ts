import { readInput, time } from "../utils";

const input = await readInput().then((data) => data[0].split(" ").map(Number));

function count(stone: number, blinks: number): number {
	if (blinks === 0) return 1;
	if (stone === 0) return memoisedCount(1, blinks - 1);

	const digitLength = Math.floor(Math.log10(stone)) + 1;

	if (digitLength % 2 === 0) {
		const numString = stone.toString();
		const middle = numString.length / 2;

		const left = parseInt(numString.substring(0, middle));
		const right = parseInt(numString.substring(middle));

		return memoisedCount(left, blinks - 1) + memoisedCount(right, blinks - 1);
	}

	return memoisedCount(stone * 2024, blinks - 1);
}

function memoise<T extends unknown[], A>(fn: (...args: T) => A) {
	const cache = new Map();

	return (...args: T) => {
		const key = args.join("_");

		if (cache.has(key)) {
			return cache.get(key);
		}

		const result = fn(...args);

		cache.set(key, result);
		return result;
	};
}

const memoisedCount = memoise(count);

time(() => {
	console.log(
		"Part 1:",
		input.map((s) => memoisedCount(s, 25)).reduce((acc, val) => acc + val)
	);
});

time(() => {
	console.log(
		"Part 2:",
		input.map((s) => memoisedCount(s, 75)).reduce((acc, val) => acc + val)
	);
});
