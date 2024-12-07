import { readInput, time } from "../utils";

function getPossibleCalculations(
	numbers: number[],
	enableConcat = false
): number[] {
	const first = numbers.shift()!;

	return Array.from(generateCalculations(first, numbers));

	function* generateCalculations(
		value: number,
		arr: number[]
	): Generator<number> {
		if (arr.length === 0) {
			yield value;
		} else {
			yield* generateCalculations(value + arr[0], arr.slice(1));
			yield* generateCalculations(value * arr[0], arr.slice(1));

			if (enableConcat) {
				yield* generateCalculations(
					parseInt(`${value}${arr[0]}`),
					arr.slice(1)
				);
			}
		}
	}
}
const input = await readInput();

function partOne(): void {
	let part1 = 0;

	for (const line of input) {
		const [target, ...numbers] = line.match(/\d+/g)?.map(Number) ?? [];

		if (getPossibleCalculations(numbers).includes(target)) {
			part1 += target;
		}
	}

	console.log("Part 1:", part1);
}

function partTwo(): void {
	let part2 = 0;

	for (const line of input) {
		const [target, ...numbers] = line.match(/\d+/g)?.map(Number) ?? [];

		if (getPossibleCalculations(numbers, true).includes(target)) {
			part2 += target;
		}
	}

	console.log("Part 1:", part2);
}

time(partOne);
time(partTwo);
