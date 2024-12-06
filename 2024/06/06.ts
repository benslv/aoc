import { readInput } from "../utils";

const input = await readInput();

let guardX: number = Infinity;
let guardStartPos = "";
let guardY: number = Infinity;

let guardDx = 0;
let guardDy = -1;

const obstaclePositions = new Set();

for (let y = 0; y < input.length; y++) {
	for (let x = 0; x < input[y].length; x++) {
		if (input[y][x] === "#") {
			obstaclePositions.add(`${y},${x}`);
		}

		if (input[y][x] === "^") {
			guardX = x;
			guardY = y;
			guardStartPos = `${y},${x}`;
		}
	}
}

const visited = new Set([`${guardY},${guardX}`]);
const fullPath = [`${guardY},${guardX},${guardDy},${guardDx}`];

while (input[guardY + guardDy]?.[guardX + guardDx] !== undefined) {
	while (obstaclePositions.has(`${guardY + guardDy},${guardX + guardDx}`)) {
		[guardDy, guardDx] = [guardDx, -guardDy];
	}

	guardY += guardDy;
	guardX += guardDx;

	visited.add(`${guardY},${guardX}`);
}

console.log("Part 1:", visited.size);

let part2 = 0;

const potentialObstaclePositions = new Set([...visited]);
potentialObstaclePositions.delete(guardStartPos);

for (const pos of potentialObstaclePositions) {
	[guardY, guardX] = guardStartPos.split(",").map(Number);
	guardDy = -1;
	guardDx = 0;

	obstaclePositions.add(pos);

	const path = new Set();

	while (input[guardY + guardDy]?.[guardX + guardDx] !== undefined) {
		while (
			obstaclePositions.has(`${guardY + guardDy},${guardX + guardDx}`)
		) {
			[guardDy, guardDx] = [guardDx, -guardDy];
		}

		guardY += guardDy;
		guardX += guardDx;

		const guardState = `${guardY},${guardX},${guardDy},${guardDx}`;

		if (path.has(guardState)) {
			part2 += 1;
			break;
		}

		path.add(guardState);
	}

	obstaclePositions.delete(pos);
}

// for (let i = 0; i < fullPath.length; i++) {
// 	const path = fullPath.slice(0, i);
// 	// Initialise guard at start.
// 	const start = fullPath[i];
// 	[guardY, guardX, guardDy, guardDx] = start.split(",").map(Number);
// 	const isAlreadyBlocked =
// 		input[guardY + guardDy]?.[guardX + guardDx] === "#";
// 	// console.log(`Blocking ${guardY + guardDy}, ${guardX + guardDx}`);
// 	// Ignore any start positions which are already blocked.
// 	if (isAlreadyBlocked) continue;
// 	// Pretend position IS blocked. Turn guard right.
// 	[guardDy, guardDx] = [guardDx, -guardDy];
// 	path.push(`${guardY},${guardX},${guardDy},${guardDx}`);
// 	while (input[guardY + guardDy]?.[guardX + guardDx] !== undefined) {
// 		while (input[guardY + guardDy]?.[guardX + guardDx] === "#") {
// 			[guardDy, guardDx] = [guardDx, -guardDy];
// 		}
// 		guardY += guardDy;
// 		guardX += guardDx;
// 		if (path.includes(`${guardY},${guardX},${guardDy},${guardDx}`)) {
// 			part2 += 1;
// 			break;
// 		}
// 		path.push(`${guardY},${guardX},${guardDy},${guardDx}`);
// 	}
// }

console.log(part2);
