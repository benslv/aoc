import { readInput } from "../utils";

const input = await readInput();

const lines = input.map((line) => line.split(" ").map((val) => parseInt(val)));

function checkLine(line: number[]): boolean {
	const diffs = line.slice(0, -1).map((__, i) => line[i + 1]! - line[i]!);

	const increasing = diffs.every((diff) => diff > 0);
	const decreasing = diffs.every((diff) => diff < 0);
	const noExceedMaxDiff = Math.max(...diffs) <= 3 && Math.min(...diffs) >= -3;

	return (increasing || decreasing) && noExceedMaxDiff;
}

const part1 = lines.map(checkLine).filter(Boolean).length;
console.log("Part 1:", part1);

function doPartTwo(lines: number[][]): number {
	let numSafe = 0;
	const badLines = [];

	for (const line of lines) {
		if (checkLine(line)) {
			numSafe += 1;
		} else {
			badLines.push(line);
		}
	}

	for (const line of badLines) {
		for (let i = 0; i < line.length; i++) {
			const newLine = line.slice();

			newLine.splice(i, 1);

			if (checkLine(newLine)) {
				numSafe += 1;
				break;
			}
		}
	}

	return numSafe;
}

console.log("Part 2:", doPartTwo(lines));
