import { bench, run } from "mitata";
import { readInput } from "../utils";
import { mod } from "../utils/mod";

const ROTATON_REGEX = /([LR])(\d+)/g

const input = await readInput().then(data => Array.from(data.join("\n").matchAll(ROTATON_REGEX)));

function partOne() {
	let rot = 50;
	let answer = 0;

	for (const [, direction, amount] of input) {
		switch (direction) {
			case "L": {
				rot = mod((rot - Number(amount)), 100);
				break;
			}
			case "R": {
				rot = mod((rot + Number(amount)), 100)
			}
		}

		if (rot === 0) answer += 1;
	}

	return answer
}

function partTwo() {
	let rot = 50;
	let answer = 0;

	for (const [, direction, amount] of input) {
		switch (direction) {
			case "L": {
				for (let i = 0; i < Number(amount); i++) {
					rot = mod(rot - 1, 100);

					if (rot === 0) answer += 1;
				}

				break;
			}
			case "R": {
				for (let i = 0; i < Number(amount); i++) {
					rot = mod(rot + 1, 100);

					if (rot === 0) answer += 1;
				}
			}
		}
	}

	return answer
}

console.log("Part 1:", partOne());
console.log("Part 2:", partTwo());

bench("Part 1:", partOne)
bench("Part 2:", partTwo)
run();