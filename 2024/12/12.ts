import { readInput } from "../utils";

const input = await readInput();

function getRegions(grid: string[]): Array<Set<string>> {
	const pointsAlreadyInARegion = new Set<string>();
	const regions = [];

	for (let y = 0; y < grid.length; y++) {
		const line = grid[y];
		for (let x = 0; x < line.length; x++) {
			const region = floodFill(y, x);

			if (!region) continue;

			for (const point of region) {
				pointsAlreadyInARegion.add(point);
			}

			regions.push(region);
		}
	}

	return regions;

	function floodFill(y: number, x: number): Set<string> | undefined {
		const points = new Set<string>([`${y},${x}`]);
		const initialValue = input[y][x];

		const queue: [number, number][] = [[y, x]];

		while (queue.length > 0) {
			const [y, x] = queue.shift()!;

			if (pointsAlreadyInARegion.has(`${y},${x}`)) {
				return undefined;
			}

			for (const [dy, dx] of [
				[0, 1],
				[0, -1],
				[1, 0],
				[-1, 0]
			]) {
				const nextY = y + dy;
				const nextX = x + dx;

				if (
					nextY < 0 ||
					nextY >= grid.length ||
					nextX < 0 ||
					nextX >= grid[0].length
				)
					continue;

				if (points.has(`${nextY},${nextX}`)) continue;

				if (input[nextY]?.[nextX] === initialValue) {
					queue.push([nextY, nextX]);
					points.add(`${nextY},${nextX}`);
				}
			}
		}

		return points;
	}
}

function getExposedSides(y: number, x: number, grid: string[]): number {
	const value = grid[y]?.[x];

	const top = grid[y - 1]?.[x];
	const bottom = grid[y + 1]?.[x];
	const left = grid[y]?.[x - 1];
	const right = grid[y]?.[x + 1];

	return [top, bottom, left, right].reduce(
		(acc, num) => (num !== value ? acc + 1 : acc),
		0
	);
}

function getPerimeter(region: Set<string>, grid: string[]): number {
	return region.values().reduce((acc, point) => {
		const [y, x] = point.split(",").map(Number);

		return acc + getExposedSides(y, x, grid);
	}, 0);
}

const part1 = () => {
	const regions = getRegions(input);

	const result = regions.reduce((acc, region) => {
		const perimeter = getPerimeter(region, input);

		return acc + region.size * perimeter;
	}, 0);

	return result;
};

console.log("Part 1:", part1());
