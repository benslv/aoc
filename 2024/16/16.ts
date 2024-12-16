import assert from "node:assert";
import { readInput } from "../utils";

const input = await readInput();

const HEIGHT = input.length;
const WIDTH = input[0].length;

const startIndex = input.join("").match(/S/)?.index;
const endIndex = input.join("").match(/E/)?.index;

assert(startIndex, "Couldn't find start position.");
assert(endIndex, "Couldn't find end position.");

function getPositionFromIndex(idx: number, height: number): [number, number] {
	const y = Math.floor(idx / height);
	const x = idx % WIDTH;

	return [y, x];
}

const start = getPositionFromIndex(startIndex, HEIGHT);

function runDFS([startY, startX]: [number, number]) {
	const paths: string[][] = [];

	DFS(startY, startX, [`${startY},${startX}`]);

	return paths;

	function DFS(y: number, x: number, path: string[]) {
		for (const [dy, dx] of [
			[-1, 0],
			[1, 0],
			[0, -1],
			[0, 1]
		]) {
			const nextY = y + dy;
			const nextX = x + dx;

			if (path.includes(`${nextY},${nextX}`) || input[nextY][nextX] === "#")
				continue;

			if (input[nextY][nextX] === "E") {
				paths.push([...path, `${nextY},${nextX}`]);
				return;
			}

			DFS(nextY, nextX, [...path, `${nextY},${nextX}`]);
		}
	}
}

function calculateCost(path: string[]): number {
	const pathToCoords = path.map((node) => node.split(",").map(Number));

	// +1 for every move
	let cost = pathToCoords.length - 1;

	// East
	let dir: [number, number] = [0, 1];

	for (let i = 1; i < pathToCoords.length; i++) {
		const [y1, x1] = pathToCoords[i - 1];
		const [y2, x2] = pathToCoords[i];

		const newDir: [number, number] = [y2 - y1, x2 - x1];

		cost += turnCost(newDir, dir);

		dir = newDir;
	}

	return cost;
}

function turnCost(
	[y2, x2]: [number, number],
	[y1, x1]: [number, number]
): number {
	const yCost = Math.abs(y2 - y1);
	const xCost = Math.abs(x2 - x1);

	return Math.max(yCost, xCost) * 1000;
}

const costs = runDFS(start)
	.map(calculateCost)
	.toSorted((a, b) => a - b);

console.log(costs[0]);
