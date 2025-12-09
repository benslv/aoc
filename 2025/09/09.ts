import { bench, run } from "mitata";
import { readInput } from "../utils";

const input = await readInput();
const points = input.map(
	(line) => line.split(",").map(Number) as [number, number]
);

function bothParts() {
	const greenLines = [];

	// Coordinates are defined "in order" around the polygon, so we can do this.
	for (let i = 0; i < points.length; i++) {
		greenLines.push([points[i], points[(i + 1) % points.length]]);
	}

	let partOne = 0;
	let partTwo = 0;

	for (let i = 0; i < points.length - 1; i++) {
		const [x1, y1] = points[i];

		for (let j = i + 1; j < points.length; j++) {
			const [x2, y2] = points[j];

			const rMinX = Math.min(x1, x2);
			const rMaxX = Math.max(x1, x2);
			const rMinY = Math.min(y1, y2);
			const rMaxY = Math.max(y1, y2);

			const area = (rMaxY - rMinY + 1) * (rMaxX - rMinX + 1);

			partOne = Math.max(partOne, area);

			if (area > partTwo) {
				let isColliding = false;

				for (const [[p, q], [r, s]] of greenLines) {
					const eMinX = Math.min(p, r);
					const eMaxX = Math.max(p, r);
					const eMinY = Math.min(q, s);
					const eMaxY = Math.max(q, s);

					if (
						rMinX < eMaxX &&
						rMaxX > eMinX &&
						rMinY < eMaxY &&
						rMaxY > eMinY
					) {
						isColliding = true;
						break;
					}
				}

				if (!isColliding) {
					partTwo = Math.max(partTwo, area);
				}
			}
		}
	}

	return [partOne, partTwo] as const;
}

const [partOne, partTwo] = bothParts();

console.log("Part 1:", partOne);
console.log("Part 2:", partTwo);

bench("Both", bothParts);
run();
