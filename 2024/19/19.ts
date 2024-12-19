import { bench, run } from "mitata";
import { readInput } from "../utils";

const input = await readInput();

const [availableString, , ...arrangements] = input;

const available = availableString.split(", ");

function check(pattern: string): number {
	if (pattern === "") return 1;

	let poss = 0;

	for (const a of available) {
		if (pattern.startsWith(a)) {
			poss += memoisedCheck(pattern.slice(a.length));
		}
	}

	return poss;
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

const memoisedCheck = memoise(check);

const part1 = () =>
	arrangements
		.map(memoisedCheck)
		.reduce((acc, val) => (acc += val > 0 ? 1 : 0), 0);

const part2 = () =>
	arrangements
		.map(memoisedCheck)
		.reduce((acc, val) => (acc += val > 0 ? val : 0), 0);

console.log("Part 1:", part1());
console.log("Part 2:", part2());

bench("Part 1", part1);
bench("Part 2", part2);

await run();
