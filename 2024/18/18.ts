import { bench, run } from "mitata";
import { readInput } from "../utils";

const input = await readInput();

const tX = 70
const tY = 70;

function path(numObstacles: number) {
    const seen = new Set<string>(input.slice(0, numObstacles))
    const queue: [number, number, number][] = [[0, 0, 0]]

    while (queue.length > 0) {
        const [x, y, dist] = queue.shift()!;

        if (x === tX && y === tY) {
            return dist;
        }

        for (const [nx, ny] of [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]) {
            if (ny < 0 || ny > tY || nx < 0 || nx > tX) continue;
            if (seen.has(`${nx},${ny}`)) continue;

            seen.add(`${nx},${ny}`);
            queue.push([nx, ny, dist + 1])
        }
    }

    return Infinity
}

const part1 = path(1024);
console.log("Part 1:", part1);

function partTwo() {
    // 🔥🔥🔥 JANKY BINARY SEARCH WOOHOO 🔥🔥🔥
    let m = Math.floor(input.length / 2);
    let step = Math.floor(m / 2)
    while (step !== 0) {
        const d = path(m);

        if (d === Infinity) {
            m -= step;
        } else {
            m += step
        }

        step /= 2;
    }

    m = Math.round(m)

    return input[m - 1]
}

console.log("Part 2:", partTwo());

bench("Part 1", () => path(1024))
bench("Part 2", partTwo)
await run();