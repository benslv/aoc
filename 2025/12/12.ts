import { barplot, bench, run, summary } from "mitata";
import { readInput } from "../utils";

const input = await readInput().then((data) => data.join("\n").split("\n\n"));
const regions = input.at(-1)!.split("\n");

const partOne = () =>
	regions
		.map(
			(region) =>
				region
					.split(": ")
					.at(0)!
					.split("x")
					.map(Number)
					.reduce((acc, val) => acc * val, 1) >=
				9 *
					region
						.split(": ")
						.at(1)!
						.split(" ")
						.map(Number)
						.reduce((acc, count) => acc + count)
		)
		.filter(Boolean).length;

console.log("Part 1:", partOne());

function partOneRegex() {
	let answer = 0;

	for (const region of regions) {
		const [w, h, ...nums] = Array.from(region.matchAll(/\d+/g)).map((x) =>
			Number(x[0])
		);

		answer += Number(w * h >= 9 * nums.reduce((a, b) => a + b));
	}

	return answer;
}

const partOneOptimised = () =>
	regions.reduce((acc, region) => {
		const [area, nums] = region.split(": ");
		return (
			acc +
			Number(
				area.split("x").reduce((acc, val) => acc * Number(val), 1) >=
					9 *
						nums
							.split(" ")
							.reduce((acc, count) => acc + Number(count), 0)
			)
		);
	}, 0);

barplot(() => {
	summary(() => {
		bench("Part 1 (normal)", partOne);
		bench("Part 1 (optimised)", partOneOptimised);
		bench("Part 1 (regex)", partOneRegex);
	});
});
run();
