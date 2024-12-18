import assert from "node:assert";
import { setTimeout } from "node:timers/promises";
import { readInput } from "../utils";

const input = await readInput();

const grid = input.map((line) => line.split(""));

const WIDTH = input[0].length;

const startIndex = input.join("").match(/S/)?.index;
assert(startIndex, "Couldn't find start position.");

const endIndex = input.join("").match(/E/)?.index;
assert(endIndex, "Couldn't find end position.");

function getPositionFromIndex(idx: number): [number, number] {
	const y = Math.floor(idx / WIDTH);
	const x = idx % WIDTH;

	return [y, x];
}

const [sy, sx] = getPositionFromIndex(startIndex);
const [ey, ex] = getPositionFromIndex(endIndex);

const seen = new Set<string>();
const queue = [[sy, sx]];

while (queue.length > 0) {
	// BFS Method.
	const [y, x] = queue.shift()!;

	// // Uncomment for DFS Method.
	// const [y,x] = queue.pop()!

	if (grid[y][x] === "#" || seen.has(`${y},${x}`)) continue;

	seen.add(`${y},${x}`);

	await printGrid(grid, seen);

	if (y === ey && x === ex) {
		console.log("Found it!");
		break;
	}

	for (const pos of [
		[y + 1, x],
		[y - 1, x],
		[y, x + 1],
		[y, x - 1],
	]) {
		queue.push(pos);
	}
}

async function printGrid(grid: string[][], visited: Set<string>) {
	for (const [y, x] of visited
		.values()
		.map((pos) => pos.split(",").map(Number))) {
		grid[y][x] = "\x1b[31mO\x1b[0m";
	}

	console.clear();
	console.log(grid.map((line) => line.join("")).join("\n"));
	await setTimeout(5);
}
