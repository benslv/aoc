import { bench, run } from "mitata";
import { readInput } from "../utils";

const input = await readInput();

const nodes = new Map<string, Set<string>>();

for (const line of input) {
	const [parent, ...children] = line.split(" ");

	nodes.set(parent.slice(0, -1), new Set(children));
}

function partOne() {
	const paths = [];

	const queue: Array<Array<string>> = [["you"]];

	while (queue.length > 0) {
		const path = queue.shift()!;
		const node = path[path.length - 1];

		if (node === "out") {
			paths.push(path);
			continue;
		}

		const children = nodes.get(node);

		for (const child of children ?? []) {
			queue.push([...path, child]);
		}
	}

	return paths.length;
}

function partTwo(): number {
	const cache = new Map<string, number>();

	return countPaths("svr", false, false);

	function countPaths(here: string, dac: boolean, fft: boolean): number {
		const cacheKey = `${here}-${dac}-${fft}`;
		const cachedValue = cache.get(cacheKey);
		if (cachedValue !== undefined) return cachedValue;

		let dacVisited = dac;
		let fftVisited = fft;

		switch (here) {
			case "out":
				const result = Number(dac && fft);
				cache.set(cacheKey, result);
				return result; // return 1 if both visited, otherwise 0
			case "dac":
				dacVisited = true;
				break;
			case "fft":
				fftVisited = true;
				break;
		}

		const result2 = Array.from(nodes.get(here) ?? []).reduce(
			(total, v) => total + countPaths(v, dacVisited, fftVisited),
			0
		);

		cache.set(`${here}-${dac}-${fft}`, result2);

		return result2;
	}
}

console.log("Part 1:", partOne());
console.log("Part 2:", partTwo());

bench("Part 1", partOne);
bench("Part 2", partTwo);
run();
