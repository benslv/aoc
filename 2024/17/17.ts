import { bench, run } from "mitata";

class Intcode {
	pointer: number = 0;
	regA: number = 0;
	regB: number = 0;
	regC: number = 0;
	output: number[] = [];

	constructor(a: number, b: number, c: number) {
		this.regA = a;
		this.regB = b;
		this.regC = c;
	}

	run(tape: number[]) {
		while (this.pointer >= 0 && this.pointer < tape.length) {
			const opcode = tape[this.pointer];

			const literal = tape[this.pointer + 1]
			const combo = [0, 1, 2, 3, this.regA, this.regB, this.regC, Infinity][tape[this.pointer + 1]]

			switch (opcode) {
				case 0: this.regA = Math.trunc(this.regA / Math.pow(2, combo)); break; 		// adv
				case 1: this.regB = this.regB ^ literal; break; 	 												// bxl
				case 2: this.regB = combo & 7; break;																			// bst
				case 3: if (this.regA !== 0) this.pointer = literal - 2; break; 					// jnz
				case 4: this.regB = this.regB ^ this.regC; break; 												// bxc
				case 5: this.output.push(combo & 7); break; 															// out
				case 6: this.regB = Math.trunc(this.regA / Math.pow(2, combo)); break; 		// bdv
				case 7: this.regC = Math.trunc(this.regA / Math.pow(2, combo)); break; 		// cdv
				default: throw new Error(`Received unexpected opcode: ${opcode}`)
			}

			this.pointer += 2;
		}

		return this.output
	}
}

function partOne() {
	const part1 = new Intcode(48744869, 0, 0)
	return part1.run([2, 4, 1, 2, 7, 5, 1, 3, 4, 4, 5, 5, 0, 3, 3, 0])
}

function arrayEquals<T>(arr: T[], brr: T[]) {
	return arr.length === brr.length && arr.every((val, i) => val === brr[i])
}


// This is what my program decompiles to.
/* function runDecompiled(a: number, b: number, c: number) {
	const out = [];

	while (a !== 0) {
		b = a % 8;
		b ^= 2;
		c = Math.trunc(a / Math.pow(2, b))
		b ^= 3;
		b ^= c;
		out.push(b & 7)
		a = Math.trunc(a / Math.pow(2, 3))
	}

	return out;
} */


function partTwo() {
	const input = [2, 4, 1, 2, 7, 5, 1, 3, 4, 4, 5, 5, 0, 3, 3, 0]
	const tests = [[1, 0]]

	for (const [i, x] of tests) {
		for (let a = x; a < x + 8; a++) {
			if (arrayEquals(new Intcode(a, 0, 0).run(input), input.slice(-i))) {
				tests.push([i + 1, a * 8])

				if (i === input.length) {
					return a
				}
			}

		}
	}
}

console.log("Part 1:", partOne());
console.log("Part 2:", partTwo());

bench("Part 1", partOne)
bench("Part 2", partTwo)

await run()