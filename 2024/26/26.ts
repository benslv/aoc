import { readInput } from "../utils";

// ......
// .2....
// 1.....
// .23...
// .3....
// ......

const [crates, targets] = await readInput().then((data) =>
	data.join("\n").split("\n\n")
);

const [start, end] = targets
	.split("\n")
	.map((l) => l.split(" ")[0].split(",").map(Number));

console.log(start, end);

const heights = new Map<string, number>();

for (const c of crates.split("\n")) {
	const [coord, height] = c.split(" ");

	heights.set(coord, parseInt(height));
}

const grid = new Set(heights.keys());

function tipCrate(
	[y, x]: [number, number],
	height: number,
	[dy, dx]: [number, number]
): Set<string> {
	const tippedPoints = new Set<string>();

	for (let i = 1; i <= height; i++) {
		tippedPoints.add(`${y + i * dy},${x + i * dx}`);
	}

	return tippedPoints;
}

console.log(tipCrate([3, 2], 3, [-1, 0]));

// Starting from the position in the start variable, we need to test tipping over the crates in every valid direction and see if a route can be made from the start crate to the end create. You can only move between crates in vertical and horizontal motions and cannot touch the ground (the gap between creates) at any time.
function run() {
	const [sy, sx] = start;
	const [ey, ex] = end;

	const startHeight = heights.get(`${sy},${sx}`)!;

	const queue = [
		{
			y: sy,
			x: sx,
			height: startHeight,
		},
	];

	const visited = new Set<string>();
}
