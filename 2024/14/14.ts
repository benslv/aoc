import { assert } from "console";
import { bench, run } from "mitata";
import { readInput } from "../utils";

type Robot = [number, number, number, number];

const input = await readInput();

const DIGITS_REGEX = /p=(\d+),(\d+) v=(-?\d+),(-?\d+)/g;

const WIDTH = 101;
const HEIGHT = 103;

const CENTRE_X = Math.floor(WIDTH / 2);
const CENTRE_Y = Math.floor(HEIGHT / 2);

const robots = input.map((line) => {
	const digits = Array.from(line.matchAll(DIGITS_REGEX))[0]
		.slice(1, 5)
		.map(Number);

	assert(
		digits?.length === 4,
		"Couldn't match expected number of digits on: " + line
	);

	return digits;
}) as Robot[];

function calculateEndPosition(robot: Robot, steps: number): Robot {
	const [x, y, dx, dy] = robot;

	return [mod(x + steps * dx, WIDTH), mod(y + steps * dy, HEIGHT), dx, dy];
}

// Because % is actually "remainder" in JS...
function mod(n: number, m: number) {
	return ((n % m) + m) % m;
}

function getQuadrant([x, y, _, __]: Robot): -1 | 1 | 2 | 3 | 4 {
	if (x === CENTRE_X || y === CENTRE_Y) return -1;

	if (x < CENTRE_X) {
		if (y < CENTRE_Y) return 1;

		return 3;
	} else {
		if (y < CENTRE_Y) return 2;

		return 4;
	}
}

function partOne() {
	const part1quadrants = robots
		.map((r) => calculateEndPosition(r, 100))
		.map(getQuadrant)
		.reduce(
			(acc, quadrant) => {
				if (quadrant === -1) return acc;

				acc[quadrant] += 1;

				return acc;
			},
			{ 1: 0, 2: 0, 3: 0, 4: 0 }
		);

	return Object.values(part1quadrants).reduce((acc, val) => acc * val, 1);
}

console.log("Part 1:", partOne());

bench("Part 1", partOne);

await run();
