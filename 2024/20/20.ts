import assert from "node:assert";
import { readInput } from "../utils";
import { permutations } from "itertools";

const input = await readInput();

const grid = input.flatMap((line, y) => line.split("").map((char, x) => [y, x, char] as [number, number, string])).reduce((map, [y, x, char]) => map.set(`${y},${x}`, char), new Map<string, string>());

const distances: Record<string, number> = {}

const WIDTH = input[0].length;

const startIndex = input.join("").match(/S/)?.index;
assert(startIndex, "Couldn't find start position.");

function getPositionFromIndex(idx: number): [number, number] {
    const y = Math.floor(idx / WIDTH);
    const x = idx % WIDTH;

    return [y, x];
}

const [sy, sx] = getPositionFromIndex(startIndex);

const seen = new Set<string>()
const queue = [[sy, sx, 0]]

while (queue.length > 0) {
    const [y, x, dist] = queue.shift()!

    if (seen.has(`${y},${x}`)) continue;
    seen.add(`${y},${x}`);

    distances[`${y},${x}`] = dist;

    for (const [ny, nx] of [[y + 1, x], [y - 1, x], [y, x + 1], [y, x - 1]]) {
        if (grid.has(`${ny},${nx}`) && grid.get(`${ny},${nx}`) !== "#") {
            queue.push([ny, nx, dist + 1])
        }
    }
}

const pointPairs = permutations(seen, 2)

let part1 = 0;
let part2 = 0;

for (const [a, b] of pointPairs) {
    const d = manhattan(a, b)
    if (d === 2 && distances[b] - distances[a] - d >= 100) {
        part1 += 1
    }
    if (d <= 20 && distances[b] - distances[a] - d >= 100) {
        part2 += 1
    }
}

console.log("Part 1:", part1);
console.log("Part 2:", part2);

function manhattan(a: string, b: string) {
    const [ay, ax] = a.split(",").map(Number);
    const [by, bx] = b.split(",").map(Number)

    return Math.abs(by - ay) + Math.abs(bx - ax);
}