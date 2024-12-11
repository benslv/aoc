import { bench, run } from "mitata";

import { readInput } from "../utils";

const input = await readInput();

const grid = input.map((line) => line.split("").map(Number));

function getAdjacentCoords(y: number, x: number): [number, number][] {
	const coords: [number, number][] = [];

	const currHeight = grid[y][x];

	for (const dy of [-1, 0, 1]) {
		for (const dx of [-1, 0, 1]) {
			const newHeight = grid[y + dy]?.[x + dx];
			if (
				Math.abs(dy) + Math.abs(dx) === 1 &&
				newHeight === currHeight + 1
			) {
				coords.push([y + dy, x + dx]);
			}
		}
	}

	return coords;
}

function DFS(grid: number[][]) {
	const part1 = new Map<string, Set<string>>();
	const part2: string[][] = [];

	for (let y = 0; y < grid.length; y++) {
		for (let x = 0; x < grid[y].length; x++) {
			if (grid[y][x] === 0) {
				traverse(y, x);
			}
		}
	}

	function traverse(y: number, x: number, path: string[] = []) {
		if (grid[y][x] === 9) {
			part2.push([...path, `${y},${x}`]);

			const start = path[0];

			if (!part1.has(start)) {
				part1.set(start, new Set());
			}

			part1.get(start)!.add(`${y},${x}`);

			return;
		}

		for (const point of getAdjacentCoords(y, x)) {
			if (path.includes(`${y},${x}`)) continue;

			traverse(...point, [...path, `${y},${x}`]);
		}
	}

	return [part1, part2] as const;
}

const [part1, part2] = DFS(grid);

console.log(
	"Part 1:",
	part1.entries().reduce((acc, [, ends]) => acc + ends.size, 0)
);

console.log("Part 2:", part2.length);

bench("Traverse Grid", () => DFS(grid));

await run();
