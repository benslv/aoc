import { readInput } from "../utils";
import { mod } from "../utils/mod";

const input = await readInput();

const ROTATON_REGEX = /([LR])(\d+)/

let part1 = 50;
let ans1 = 0;
for (const line of input) {
	const [, direction, amount] = line.match(ROTATON_REGEX);

	switch (direction) {
		case "L": {
			part1 = mod((part1 - Number(amount)), 100);
			break;
		}
		case "R": {
			part1 = mod((part1 + Number(amount)), 100)
		}
	}

	if (part1 === 0) ans1 += 1;
}

console.log(ans1);
