import { bench, run } from "mitata";
import { readInput } from "../utils";
import { Grid } from "../utils/Grid";

const input = await readInput();

function partOne() {
	const grid = new Grid(input);

	let answer = 0;

	for (const [pos, val] of grid.points.entries()) {
		if (val !== "@") continue;

		const [y, x] = pos.split(",").map(Number);

		let nearbyRolls = 0;

		for (const dy of [-1, 0, 1]) {
			for (const dx of [-1, 0, 1]) {
				if (dy === 0 && dx === 0) continue;

				if (grid.get(y + dy, x + dx) === "@") {
					nearbyRolls += 1;
				}
			}
		}

		if (nearbyRolls < 4) {
			answer += 1;
		}
	}

	return answer;
}

function partTwo() {
	const grid = new Grid(input);

	let answer = 0;
	let rollsToRemove: string[] = [];

	do {
		for (const pos of rollsToRemove) {
			answer += 1;

			const [y, x] = pos.split(",").map(Number);
			grid.set(y, x, ".");
		}
		rollsToRemove = [];

		for (const [pos, val] of grid.points.entries()) {
			if (val !== "@") continue;

			const [y, x] = pos.split(",").map(Number);

			let nearbyRolls = 0;

			for (const dy of [-1, 0, 1]) {
				for (const dx of [-1, 0, 1]) {
					if (dy === 0 && dx === 0) continue;

					if (grid.get(y + dy, x + dx) === "@") {
						nearbyRolls += 1;
					}
				}
			}

			if (nearbyRolls < 4) {
				rollsToRemove.push(`${y},${x}`);
			}
		}
	} while (rollsToRemove.length > 0);

	return answer;
}

console.log("Part 1:", partOne());

console.log("Part 2:", partTwo());

bench("Part 1", partOne);
bench("Part 2", partTwo);
run();
