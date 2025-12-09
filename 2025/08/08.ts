import { readInput } from "../utils";

const input = await readInput();

const circuits = new Map<string, Set<string>>(input.map(line => [line, new Set([line])]));

console.log(circuits);

function calculate3dDistance(a: string, b: string): number {
	const [x, y, z] = a.split(",").map(Number)
	const [i, j, k] = b.split(",").map(Number)

	const dist = Math.sqrt(Math.pow(x - i, 2) + Math.pow(y - j, 2) + Math.pow(z - k, 2))

	return dist
}

const pairs = []
for (let i = 0; i < input.length - 1; i++) {
	for (let j = i + 1; j < input.length; j++) {
		pairs.push([input[i], input[j]] as const)
	}
}

pairs.sort((a, b) => calculate3dDistance(...a) - calculate3dDistance(...b))


const NUM_PAIRS_TO_CONNECT = 10;
console.log(pairs.slice(0, NUM_PAIRS_TO_CONNECT));

for (const [i, [a, b]] of pairs.entries()) {
	let aCircuit, bCircuit;

	for (const c of circuits) {
		if (c.has(a)) aCircuit = c;
		if (c.has(b)) bCircuit = c;
	}

	circuits.delete(aCircuit!)
	circuits.delete(bCircuit!)

	circuits.add(aCircuit!.union(bCircuit!))

	if (i === 10) break;
}

console.log(circuits);


// console.log(circuitMap);


// console.log(getDisjointCircuits(circuitMap).toSorted((a, b) => b.size - a.size));


// function getDisjointCircuits(map: Map<string, Set<string>>): Array<Set<string>> {
// 	const seen: Set<string> = new Set();

// 	const circuits = [];

// 	for (const [point, circuit] of map.entries()) {
// 		if (seen.has(point)) continue;

// 		for (const p of circuit) {
// 			seen.add(p)
// 		}

// 		circuits.push(circuit)
// 	}

// 	return circuits;
// }