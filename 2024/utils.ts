import readline from "readline/promises";

/**
 * @returns Array containing the lines of the input file.
 */
export async function readInput(): Promise<string[]> {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
        terminal: false
    })

    const lines: string[] = [];

    for await (const line of rl) {
        lines.push(line)
    }

    return lines;
}