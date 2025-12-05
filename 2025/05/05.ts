import { bench, run } from "mitata";
import { readInput } from "../utils";

const [ranges, ingredients] = await readInput().then(data => data.join("\n").split("\n\n").map(x => x.split("\n")));

type Range = {
	lower: number;
	upper: number;
}

const freshRanges = ranges.map<Range>(r => { const [lower, upper] = r.split("-").map(Number); return { lower, upper } });

function partOne() {
	let answer = 0;

	for (const ing of ingredients) {
		for (const r of freshRanges) {
			if (Number(ing) >= r.lower && Number(ing) <= r.upper) {
				answer += 1
				break;
			}
		}
	}

	return answer
}

console.log("Part 1:", partOne())

const sortedRanges = freshRanges.toSorted((a, b) => a.lower - b.lower)

function partTwo() {
	let answer = 0;
	let curr = 0;

	for (const range of sortedRanges) {
		let start = Math.max(range.lower, curr + 1);
		answer += Math.max(0, range.upper - start + 1)
		curr = Math.max(curr, range.upper);
	}

	return answer
}

console.log("Part 2:", partTwo())

bench("Part 1", partOne)
bench("Part 2", partTwo)
run()