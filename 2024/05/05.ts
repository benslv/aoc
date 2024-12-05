import { readInput } from "../utils";

const [rules, updates] = await readInput().then((lines) => {
  const sepIndex = lines.indexOf("");

  return [lines.slice(0, sepIndex), lines.slice(sepIndex + 1)];
});

const orderMap = new Map<string, Set<string>>();

for (const rule of rules) {
  const [before, after] = rule.split("|");

  if (!orderMap.has(before)) {
    orderMap.set(before, new Set());
  }

  orderMap.get(before)?.add(after);
}

function processUpdate(update: string[]) {
  const seen = new Set();
  for (const page of update) {
    const succ = orderMap.get(page) ?? new Set();

    if (succ.intersection(seen).size !== 0) return false;

    seen.add(page);
  }

  return true;
}

let part1 = 0;

for (const update of updates) {
  const splitUpdate = update.split(",");
  if (processUpdate(splitUpdate)) {
    console.log(splitUpdate);

    console.log(splitUpdate[Math.round(splitUpdate.length / 2) - 1]);

    part1 += parseInt(splitUpdate[Math.round(splitUpdate.length / 2) - 1]);
  }
}

console.log(part1);
