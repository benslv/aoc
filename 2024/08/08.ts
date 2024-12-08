import { readInput, time } from "../utils";

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

time(() => {
	for (const antenna in antennaMap) {
		const positions = antennaMap[antenna];

		for (let i = 0; i < positions.length - 1; i++) {
			for (let j = i + 1; j < positions.length; j++) {
				const posA = positions[i];
				const posB = positions[j];

				for (const [y, x] of getAllPointsOnLine(posA, posB)) {
					if (y >= 0 && y < height && x >= 0 && x < width) {
						if (
							y - posA[0] === 2 * (y - posB[0]) ||
							y - posB[0] === 2 * (y - posA[0])
						) {
							partOneAntinodes.add(`${y},${x}`);
						}

						partTwoAntinodes.add(`${y},${x}`);
					}
				}
			}
		}
	}

	console.log("Part 1:", partOneAntinodes.size);
	console.log("Part 2:", partTwoAntinodes.size);
});

function* getAllPointsOnLine(
	[aY, aX]: [number, number],
	[bY, bX]: [number, number]
) {
	const dy = bY - aY;
	const dx = bX - aX;

	let y = aY;
	let x = aX;

	while (y < height && x < width) {
		yield [y, x];

		y += dy;
		x += dx;
	}

	y = aY;
	x = aX;

	while (y >= 0 && x >= 0) {
		yield [y, x];

		y -= dy;
		x -= dx;
	}
}
