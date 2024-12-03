import readline from "readline/promises";

/**
 * @returns Array containing the lines of the input file.
 */
export async function readInput(): Promise<string[]> {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
  });

  const lines: string[] = [];

  for await (const line of rl) {
    lines.push(line);
  }

  return lines;
}

export function time<T>(fn: () => T) {
  performance.mark("start");
  fn();
  performance.mark("end");

  const measure = performance.measure("Function Runtime", "start", "end");

  console.log(`Ran in: ${measure.duration.toFixed(3)}ms`);

  performance.clearMarks();
  performance.clearMeasures();
}
