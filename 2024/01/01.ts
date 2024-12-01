import { readInput } from "../utils";

const input = await readInput();

const start = performance.now();

const sortedCols = input
	.reduce<[number[], number[]]>(
		(acc, line: string) => {
			const [a, b] = line.split(/\s+/).map((val) => parseInt(val));

			if (!a || !b) {
				throw new Error(
					"Could not split the line as expected. Check input file?"
				);
			}

			acc[0].push(a);
			acc[1].push(b);

			return acc;
		},
		[[], []]
	)
	.map((arr) => arr.sort((a, b) => a - b)) as [number[], number[]];

let part1 = 0;

for (let i = 0; i < sortedCols[0].length; i++) {
	const a = sortedCols[0][i];
	const b = sortedCols[1][i];

	if (!a || !b) {
		throw new Error("Could not access one of the indexes in sortedCols.");
	}

	part1 += Math.abs(a - b);
}

console.log("Part 1:", part1);

const freqs = sortedCols[1]?.reduce((acc, val) => {
	acc.set(val, (acc.get(val) ?? 0) + 1);

	return acc;
}, new Map<number, number>());

const part2 = sortedCols[0]!.reduce((acc, val) => {
	acc += val * (freqs.get(val) ?? 0);

	return acc;
}, 0);

const end = performance.now();
const ms = (end - start).toFixed(3);

console.log("Part 2", part2);
console.log(`Ran in ${ms}ms`);
