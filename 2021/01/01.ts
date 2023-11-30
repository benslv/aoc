const file = Bun.file("./01.in");

const depths = (await file.text()).split("\n").map(Number);

let part1 = 0;
let depth = undefined;

for (const line of depths) {
  if (depth && line > depth) {
    part1 += 1;
  }

  depth = line;
}

console.log(part1);
