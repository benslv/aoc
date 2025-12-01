import { readInput } from "../utils";

const input = await readInput();

const computers = new Set<string>();
const connections = new Map<string, Set<string>>();

for (const line of input) {
	const [from, to] = line.split("-");

	if (!connections.has(from)) {
		connections.set(from, new Set());
	}

	if (!connections.has(to)) {
		connections.set(to, new Set());
	}

	connections.get(from)!.add(to);
	connections.get(to)!.add(from);

	computers.add(from);
	computers.add(to);
}

let part1 = 0;
for (const [a, b, c] of generateTriples([...computers])) {
	if (
		connections.get(a)?.has(b) &&
		connections.get(b)?.has(c) &&
		connections.get(c)?.has(a) &&
		[a, b, c].some((comp) => comp.startsWith("t"))
	) {
		part1 += 1;
	}
}

console.log(part1);

function* generateTriples<T>(arr: T[]) {
	for (let i = 0; i < arr.length - 2; i++) {
		for (let j = i + 1; j < arr.length - 1; j++) {
			for (let k = j + 1; k < arr.length; k++) {
				yield [arr[i], arr[j], arr[k]];
			}
		}
	}
}
