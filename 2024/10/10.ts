import { readInput } from "../utils";

const input = await readInput();

const grid = input.map((line) => line.split("").map(Number));

console.log(grid);

function getAdjacentCoords(y: number, x: number): [number, number][] {
	const coords: [number, number][] = [];

	for (const dy of [-1, 0, 1]) {
		for (const dx of [-1, 0, 1]) {
			if (
				Math.abs(dy) + Math.abs(dx) === 1 &&
				y + dy >= 0 &&
				y + dy < grid.length &&
				x + dx >= 0 &&
				x + dx < grid[0].length
			) {
				coords.push([y + dy, x + dx]);
			}
		}
	}

	return coords;
}

function DFS(grid: number[][]) {
	for (let y = 0; y < grid.length; y++) {
		for (let x = 0; x < grid[y].length; x++) {
			console.log("Starting at", y, x);

			const paths = traverse(y, x);

			console.log(paths);
		}
	}

	function traverse(y: number, x: number, path: string[] = []) {
		for (const [y2, x2] of getAdjacentCoords(y, x)) {
			if (grid[y2][x2] === 9) {
				return [...path, `${y2},${x2}`];
			}

			if (!path.includes(`${y2},${x2}`)) {
				return traverse(y2, x2, [...path, `${y2},${x2}`]);
			}
		}
	}
}

DFS(grid);
