import { bench, run } from "mitata";
import { readInput } from "../utils";

const P1_REGEX = /^(\d+)\1$/;
const P2_REGEX = /^(\d+)\1+$/;

const input = await readInput();

const ranges = input
	.at(0)!
	.split(",")
	.map((r) => r.split("-").map(Number));

function solve() {
	let partOne = 0;
	let partTwo = 0;

	for (const [start, end] of ranges) {
		for (let i = start; i <= end; i++) {
			if (P1_REGEX.test(i.toString())) partOne += i;
			if (P2_REGEX.test(i.toString())) partTwo += i;
		}
	}

	return [partOne, partTwo] as const;
}

const [part1, part2] = solve();
console.log(`Part 1: ${part1}\nPart 2: ${part2}`);

bench("Part 1 & 2", solve);
run();
