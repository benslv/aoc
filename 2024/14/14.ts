import { assert } from "console";
import { appendFileSync } from "fs";
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

function partTwo(visualise = false) {
	const scores = [];

	for (let i = 0; i < 10000; i++) {
		const quadrants = robots
			.map((r) => calculateEndPosition(r, i))
			.map(getQuadrant)
			.reduce(
				(acc, quadrant) => {
					if (quadrant === -1) return acc;

					acc[quadrant] += 1;

					return acc;
				},
				{ 1: 0, 2: 0, 3: 0, 4: 0 }
			);

		const safetyScore = Object.values(quadrants).reduce(
			(acc, val) => acc * val,
			1
		);

		scores.push([i, safetyScore]);

		if (visualise) {
			visualiseInFile(i);
		}
	}

	scores.sort((a, b) => a[1] - b[1]);

	return `Highest clustering at ${scores[0][0]} seconds. Image likely to be found at this position. Run with visualise=true to generate visualisations file.`;
}

function visualiseInFile(steps: number) {
	const grid = Array.from({ length: HEIGHT }, () =>
		Array.from({ length: WIDTH }, () => ".")
	);

	for (const [x, y] of robots.map((r) => calculateEndPosition(r, steps))) {
		grid[y][x] = "#";
	}

	const gridString = grid.map((line) => line.join("")).join("\n");

	appendFileSync("christmas.txt", `${steps}\n${gridString}\n\n`);
}

console.log("Part 1:", partOne());
console.log("Part 2:", partTwo(true));

bench("Part 1", partOne);
bench("Part 2", partTwo);

await run();
