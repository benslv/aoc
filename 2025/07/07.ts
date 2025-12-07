import { bench, run } from "mitata";
import { readInput } from "../utils";

const input = await readInput();

function partOne(input: string[]) {
	const grid: (string | number)[][] = input.map((row) => row.split(""));
	const startX = grid[0].indexOf("S");

	grid[1][startX] = "|";

	let partOne = 0;

	for (const [j, row] of grid.slice(0, -1).entries()) {
		for (const [i, char] of row.entries()) {
			if (char !== "|") continue;

			if (grid[j + 1][i] === "^") {
				grid[j + 1][i - 1] = "|";
				grid[j + 1][i + 1] = "|";

				partOne += 1;
			} else {
				grid[j + 1][i] = "|";
			}
		}
	}

	grid[1][startX] = 1;

	return [partOne, grid] as const;
}

function partTwo(grid: (string | number)[][]) {
	for (const [j, row] of grid.entries()) {
		for (const [i, char] of row.entries()) {
			if (char !== "|") continue;

			grid[j][i] = getPointValue(grid, j - 1, i);

			if (grid[j][i - 1] === "^") {
				grid[j][i] += getPointValue(grid, j - 1, i - 1);
			}

			if (grid[j][i + 1] === "^") {
				grid[j][i] += getPointValue(grid, j - 1, i + 1);
			}
		}
	}

	return grid
		.at(-1)
		?.filter((n) => typeof n === "number")
		.reduce((acc, val) => acc + val);
}

function getPointValue(
	grid: (string | number)[][],
	y: number,
	x: number
): number {
	return typeof grid[y][x] === "string" ? 0 : grid[y][x];
}

const [p1, grid] = partOne(input);
console.log("Part 1:", p1);
console.log("Part 2:", partTwo(grid));

bench("Part 1", () => partOne(input));
bench("Part 2", function* () {
	const [__, grid] = partOne(input);

	yield () => partTwo(grid);
});
run();
