import { readInput } from "../utils";

const input = await readInput();

const circuits = new Set<Set<string>>(input.map((line) => new Set([line])));

function calculate3dDistance(a: string, b: string): number {
	const [x, y, z] = a.split(",").map(Number);
	const [i, j, k] = b.split(",").map(Number);

	const dist = Math.sqrt(
		Math.pow(x - i, 2) + Math.pow(y - j, 2) + Math.pow(z - k, 2)
	);

	return dist;
}

const pairs = [];
for (let i = 0; i < input.length - 1; i++) {
	for (let j = i + 1; j < input.length; j++) {
		pairs.push([input[i], input[j]] as const);
	}
}

pairs.sort((a, b) => calculate3dDistance(...a) - calculate3dDistance(...b));

const NUM_PAIRS_TO_CONNECT = 1000;

for (const [i, [a, b]] of pairs.entries()) {
	if (i === NUM_PAIRS_TO_CONNECT) {
		const sortedCircuits = Array.from(circuits).toSorted(
			(a, b) => b.size - a.size
		);

		const partOne =
			sortedCircuits[0].size *
			sortedCircuits[1].size *
			sortedCircuits[2].size;

		console.log("Part 1:", partOne);
	}

	let aCircuit, bCircuit;

	for (const c of circuits) {
		if (c.has(a)) aCircuit = c;
		if (c.has(b)) bCircuit = c;
	}

	circuits.delete(aCircuit!);
	circuits.delete(bCircuit!);

	circuits.add(aCircuit!.union(bCircuit!));

	if (circuits.size === 1) {
		const [x1] = a.split(",").map(Number);
		const [x2] = b.split(",").map(Number);

		console.log("Part 2:", x1 * x2);
		break;
	}
}
