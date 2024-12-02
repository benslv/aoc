import assert from "node:assert";
import { readInput } from "../utils";

const input = await readInput();

const start = performance.now();

const sortedCols = input
  .reduce<[number[], number[]]>(
    (acc, line: string) => {
      const [a, b] = line.split("   ").map((val) => parseInt(val));

      assert(a && b);

      acc[0].push(a);
      acc[1].push(b);

      return acc;
    },
    [[], []]
  )
  .map((arr) => arr.sort((a, b) => a - b)) as [number[], number[]];

const part1 = sortedCols[0].reduce(
  (acc, val, i) => acc + Math.abs(val - sortedCols[1][i]!),
  0
);

console.log("Part 1:", part1);

const freqs = sortedCols[1].reduce((acc, val) => {
  acc.set(val, (acc.get(val) ?? 0) + 1);

  return acc;
}, new Map<number, number>());

const part2 = sortedCols[0].reduce(
  (acc, val) => acc + val * (freqs.get(val) ?? 0),
  0
);

const end = performance.now();
const ms = (end - start).toFixed(3);

console.log("Part 2", part2);
console.log(`Ran in ${ms}ms`);
