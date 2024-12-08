import { readInput, time } from "../utils";

function canGenerateTarget(
	numbers: number[],
	target: number,
	enableConcat = false
): boolean {
	const first = numbers.shift()!;

	for (const num of generateCalculations(first, numbers)) {
		// arr.push(num);
		if (num === target) return true;
	}

	return false;

	function* generateCalculations(
		value: number,
		arr: number[]
	): Generator<number> {
		if (arr.length === 0 || value > target) {
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

		if (canGenerateTarget(numbers, target)) {
			part1 += target;
		}
	}

	console.log("Part 1:", part1);
}

function partTwo(): void {
	let part2 = 0;

	for (const line of input) {
		const [target, ...numbers] = line.match(/\d+/g)?.map(Number) ?? [];

		if (canGenerateTarget(numbers, target, true)) {
			part2 += target;
		}
	}

	console.log("Part 2:", part2);
}

time(partOne);
time(partTwo);
