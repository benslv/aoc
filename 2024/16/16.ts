import assert from "assert";
import { readInput } from "../utils";
import { Heap } from "heap-js";

type State = {
    y: number;
    x: number;
    direction: number;
    distance: number;
    path: string[];
};

function toString(state: State): string {
    return `${state.y},${state.x},${state.direction}`;
}

const input = await readInput();

const WIDTH = input[0].length;

const startIndex = input.join("").match(/S/)?.index;
assert(startIndex, "Couldn't find start position.");

const endIndex = input.join("").match(/E/)?.index;
assert(endIndex, "Couldn't find end position.");

function getPositionFromIndex(idx: number): [number, number] {
    const y = Math.floor(idx / WIDTH);
    const x = idx % WIDTH;

    return [y, x];
}

const [sy, sx] = getPositionFromIndex(startIndex);

let best = Infinity;
const seen = [];
const distances: Record<string, number> = {}
const queue = new Heap<State>((a, b) => a.distance - b.distance);

queue.init([{ y: sy, x: sx, direction: 1, distance: 0, path: [`${sy},${sx}`] }]);

while (!queue.isEmpty()) {
    const { y, x, direction, distance, path } = queue.pop()!

    if (distance > distances[`${y},${x},${direction}`]) continue;

    distances[`${y},${x},${direction}`] = distance

    if (input[y][x] === "E" && distance <= best) {
        seen.push(...path)
        best = distance
    }

    const [nextY, nextX] = [
        [y + 1, x], // 0 - NORTH
        [y, x + 1], // 1 - EAST
        [y - 1, x], // 2 - SOUTH
        [y, x - 1] //  3 - WEST
    ][direction];

    if (input[nextY][nextX] !== "#") {
        queue.add({
            y: nextY,
            x: nextX,
            distance: distance + 1,
            direction,
            path: [...path, `${nextY},${nextX}`]
        });
    }

    queue.add({
        y,
        x,
        distance: distance + 1000,
        direction: (direction + 1) % 4,
        path: [...path]
    });
    queue.add({
        y,
        x,
        distance: distance + 1000,
        direction: (direction + 3) % 4,
        path: [...path]
    });
}

console.log("Part 1:", best);
console.log("Part 2:", new Set(seen).size);
