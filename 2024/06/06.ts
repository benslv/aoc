import { readInput } from "../utils";

const input = await readInput();

let guardX: number = Infinity;
let guardY: number = Infinity;

let guardDx = 0;
let guardDy = -1;

for (let y = 0; y < input.length; y++) {
  for (let x = 0; x < input[y].length; x++) {
    const char = input[y][x];

    if (char === "^") {
      guardX = x;
      guardY = y;
    }
  }
}

const visited = new Set([`${guardY},${guardX}`]);

while (input[guardY + guardDy]?.[guardX + guardDx] !== undefined) {
  if (input[guardY + guardDy]?.[guardX + guardDx] === "#") {
    [guardDy, guardDx] = [guardDx, -guardDy];
  }

  guardY += guardDy;
  guardX += guardDx;

  visited.add(`${guardY},${guardX}`);
}

console.log(visited.size);
