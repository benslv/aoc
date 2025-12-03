import { bench, run } from "mitata";
import { readInput } from "../utils";

const input = await readInput().then(data => data.map(line => line.split("").map((n => parseInt(n)))));

function partOne() {
	return input.reduce((total, bank) => total + findLargestJoltageForNBatteries(bank, 2), 0);
}

function partTwo() {
	return input.reduce((total, bank) => total + findLargestJoltageForNBatteries(bank, 12), 0);
}

function findLargestJoltageForNBatteries(bank: Array<number>, n: number): number {
	const array = Array.from({ length: n }, () => 0)

	for (let i = 0; i < array.length; i++) {
		const prevIndex = i === 0 ? 0 : array[i - 1] + 1

		array[i] = maxIndex(bank, prevIndex, bank.length - (n - (i + 1)))
	}

	return array.reduce((acc, val, i) => acc + bank[val] * Math.pow(10, array.length - (i + 1)), 0)
}


function maxIndex(array: Array<number>, start: number, end: number): number {
	let m = Math.max(start, 0)

	for (let i = start; i < end; i++) {
		if (array[i] > array[m]) m = i
	}

	return m;
}

console.log("Part 1:", partOne());
console.log("Part 2:", partTwo());

bench("Part 1", partOne)
bench("Part 2", partTwo)
run()