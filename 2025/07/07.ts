import { readInput } from "../utils";

const input = await readInput();

const grid: (string | number)[][] = input.map((row) => row.split(""));

const startX = grid[0].indexOf("S");

grid[1][startX] = "|";

// For each | in line
// If ^ is below |
//  Put | on line below at x-1, x+1
// Else put | on line below at x

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

function getPointValue(
	grid: (string | number)[][],
	y: number,
	x: number
): number {
	return typeof grid[y][x] === "string" ? 0 : grid[y][x];
}

console.log(
	grid
		.at(-1)
		?.filter((n) => typeof n === "number")
		.reduce((acc, val) => acc + val)
);
