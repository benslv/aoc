import { readInput } from "../utils";

const input = await readInput();

const obstacles = new Set(input)

type Step = {
    y: number;
    x: number;
    path: string[];
}

const tY = 70;
const tX = 70;

const todo: Step[] = [{ y: 0, x: 0, path: [] }];
const paths: string[][] = [];

while (todo.length > 0) {
    const pos = todo.pop()!;

    if (pos.path.includes(`${pos.y},${pos.x}`)) {
        console.log(`Already seen ${pos.y},${pos.x} in path.`);
        continue;
    };
    if (obstacles.has(`${pos.x},${pos.y}`)) {
        console.log(`Position ${pos.y},${pos.x} is blocked.`);
        continue;
    };
    if (pos.y < 0 || pos.y > tY || pos.x < 0 || pos.x > tX) {
        console.log(`Position ${pos.y},${pos.x} is OOB.`);
        continue;
    };

    if (pos.y === tY && pos.x === tX) {
        paths.push([...pos.path, `${pos.y},${pos.x}`]);
    }

    const { y, x } = pos;

    for (const [ny, nx] of [[y + 1, x], [y, x + 1], [y - 1, x], [y, x - 1]]) {
        console.log(`Addding`, ny, nx);

        todo.unshift({ y: ny, x: nx, path: [...pos.path, `${y},${x}`] })
    }
}

console.log(paths);
