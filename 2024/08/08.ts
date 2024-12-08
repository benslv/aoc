import { readInput } from "../utils";

const input = await readInput();

const height = input.length;
const width = input[0].length;

const antennae = input.join("").matchAll(/[A-Za-z0-9]{1}/g);

// Array of coordinates that you can find each antenna of a given character at.
// { "A": [[2,3], [4,5]] } etc...
const antennaMap: Record<string, [number, number][]> = {};

for (const a of antennae) {
	const aY = Math.floor(a.index / height);
	const aX = a.index - aY * height;

	(antennaMap[a[0]] ??= []).push([aY, aX]);
}

const partOneAntinodes = new Set();
const partTwoAntinodes = new Set();

for (const antenna in antennaMap) {
	const positions = antennaMap[antenna];

	for (let i = 0; i < positions.length - 1; i++) {
		for (let j = i + 1; j < positions.length; j++) {
			const posA = positions[i];
			const posB = positions[j];

			for (const [y, x] of getAntinodePositions(posA, posB)) {
				if (y >= 0 && y < height && x >= 0 && x < width) {
					partOneAntinodes.add(`${y},${x}`);
				}
			}

			for (const pos of getAllPointsOnLine(posA, posB)) {
				partTwoAntinodes.add(pos);
			}
		}
	}
}

// console.log(partTwoAntinodes);

console.log("Part 1:", partOneAntinodes.size);
console.log("Part 2:", partTwoAntinodes.size);

function* getAntinodePositions(
	[aY, aX]: [number, number],
	[bY, bX]: [number, number]
): Generator<[number, number]> {
	const dy = bY - aY;
	const dx = bX - aX;

	yield [bY + dy, bX + dx];
	yield [aY - dy, aX - dx];
}

function* getAllPointsOnLine(
	[aY, aX]: [number, number],
	[bY, bX]: [number, number]
) {
	const dy = bY - aY;
	const dx = bX - aX;

	switch (dy / dx) {
		case Infinity:
		case -Infinity:
			for (let y = 0; y < height; y++) {
				yield `${y},${aX}`;
			}
			break;
		case 0:
			for (let x = 0; x < height; x++) {
				yield `${aY},${x}`;
			}
			break;
		default:
			const c = aY - (dy / dx) * aX;

			for (let x = 0; x < width; x++) {
				const y = (dy / dx) * x + c;

				if (Number.isInteger(y) && y >= 0 && y < height) {
					yield `${y},${x}`;
				}
			}
	}
}
