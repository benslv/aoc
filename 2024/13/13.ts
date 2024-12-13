import Matrix, { solve } from "ml-matrix";
import { readInput } from "../utils";
import { bench, run } from "mitata";

const MATCH_DIGITS = /\d+/g;

const input = await readInput().then((data) => data.join("\n").split("\n\n"));

function runClawMachine(offset: number = 0) {
	let answer = 0;
	for (const line of input) {
		const [xA, yA, xB, yB, prizeX, prizeY] = Array.from(
			line.match(MATCH_DIGITS) ?? []
		).map(Number);

		const M = new Matrix([
			[xA, xB],
			[yA, yB]
		]);

		const target = Matrix.columnVector([prizeX, prizeY]).add(offset);

		const [[, , a], [, , b]] = solve(M, target).round();

		// Accounting for bad division precision (hey that rhymes!)
		if (
			a * xA + b * xB === target.getRow(0)[0] &&
			a * yA + b * yB === target.getRow(1)[0]
		) {
			answer += 3 * a + b;
		}
	}

	return answer;
}

console.log("Part 1:", runClawMachine());
console.log("Part 2:", runClawMachine(10000000000000));

bench("Part 1", () => runClawMachine());
bench("Part 2", () => runClawMachine(10000000000000));

await run();
