import { readInput, time } from "../utils";

const [input] = await readInput();

const PART_1_REGEX = /mul\((\d+),(\d+)\)/g;

time(() => {
  const part1 = Array.from(input.matchAll(PART_1_REGEX)).reduce(
    (acc, val) => acc + parseInt(val[1]) * parseInt(val[2]),
    0
  );

  console.log("Part 1:", part1);
});

const PART_2_REGEX = /(mul|don't|do)\(((\d+),(\d+))?\)/g;

time(() => {
  let part2 = 0;
  let mulEnabled = true;

  for (const match of input.matchAll(PART_2_REGEX)) {
    const ins = match[1];

    switch (ins) {
      case "do":
        mulEnabled = true;
        break;
      case "don't":
        mulEnabled = false;
        break;
      case "mul":
        const [, , , x, y] = match;
        if (mulEnabled) part2 += parseInt(x) * parseInt(y);
        break;
      default:
        throw new Error(`Unexpected instruction: ${ins}`);
    }
  }

  console.log("Part 2:", part2);
});
