import { readInput } from "../utils";

const [rules, updates] = await readInput().then((lines) => {
  const sepIndex = lines.indexOf("");

  return [lines.slice(0, sepIndex), lines.slice(sepIndex + 1)];
});

const orderMap = new Map<number, Set<number>>();

for (const rule of rules) {
  const [before, after] = rule.split("|").map(Number);

  if (!orderMap.has(before)) {
    orderMap.set(before, new Set());
  }

  orderMap.get(before)?.add(after);
}

function checkUpdate(update: number[]) {
  const seen = new Set();
  for (const page of update) {
    const succ = orderMap.get(page) ?? new Set();

    if (succ.intersection(seen).size !== 0) return false;

    seen.add(page);
  }

  return true;
}

let part1 = 0;
let part2 = 0;

for (const update of updates) {
  const splitUpdate = update.split(",").map(Number);
  if (checkUpdate(splitUpdate)) {
    const midpoint = Math.floor(splitUpdate.length / 2);

    part1 += splitUpdate[midpoint];
  } else {
    const update = dfsTopologicalSort(splitUpdate);
    const midpoint = Math.floor(update.length / 2);

    part2 += update[midpoint];
  }
}

console.log(part1);
console.log(part2);

function dfsTopologicalSort(update: number[]): number[] {
  const visited = new Set();
  const ordered: number[] = [];

  for (const num of update) {
    traverse(num);
  }

  function traverse(num: number) {
    if (visited.has(num)) return;
    visited.add(num);

    const allDeps = orderMap.get(num) ?? new Set();
    const depsActuallyInGraph = allDeps.intersection(new Set(update));

    for (const dep of depsActuallyInGraph) {
      traverse(dep);
    }

    ordered.unshift(num);
  }

  return ordered;
}
