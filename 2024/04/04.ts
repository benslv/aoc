import { readInput } from "../utils";

const input = await readInput();

let part1 = 0;

for (let y = 0; y < input.length; y++) {
  for (let x = 0; x < input[y].length; x++) {
    // console.log({ x, y });

    const horizontal =
      x < input[y].length - 3 &&
      input[y][x] + input[y][x + 1] + input[y][x + 2] + input[y][x + 3];

    const vertical =
      y < input.length - 3 &&
      input[y][x] + input[y + 1][x] + input[y + 2][x] + input[y + 3][x];

    const posDiag =
      y >= 3 &&
      x < input[y].length - 3 &&
      input[y][x] +
        input[y - 1][x + 1] +
        input[y - 2][x + 2] +
        input[y - 3][x + 3];

    const negDiag =
      y < input.length - 3 &&
      x < input[y].length - 3 &&
      input[y][x] +
        input[y + 1][x + 1] +
        input[y + 2][x + 2] +
        input[y + 3][x + 3];

    // console.log([posDiag])

    for (const word of [horizontal, vertical, posDiag, negDiag]) {
      if (word === "XMAS" || word === "SAMX") {
        part1 += 1;
      }
    }
  }
}

console.log(part1);
