import { bench, run } from "mitata";
import { readInput } from "../utils";

const input = await readInput();

// Part 1
const part1 = () => {
	let index = 0;
	const data = input[0].split("").flatMap((val, i) => {
		if (i % 2 === 1) {
			return Array.from({ length: parseInt(val) }, () => undefined);
		}

		index += 1;

		return Array.from({ length: parseInt(val) }, () => index - 1);
	});

	let i = 0;
	let j = data.length - 1;

	while (i < j) {
		while (data[i] !== undefined) {
			i++;
		}

		while (data[j] === undefined) {
			j--;
		}

		[data[i], data[j]] = [data[j], data[i]];

		i++;
		j--;
	}
	return data
		.filter((i) => i !== undefined)
		.reduce((acc, val, i) => acc + val * i);
};

// Part 2
const part2 = () => {
	let index = 0;
	const data = input[0].split("").map((val, i) => {
		if (i % 2 === 1) {
			return [-1, parseInt(val)];
		}

		index += 1;
		//         INDEX       LENGTH
		return [index - 1, parseInt(val)];
	});

	let j = data.length - 1;
	const moved = new Set();
	while (j > 0) {
		const [blockId, blockLength] = data[j];

		if (blockId !== -1 && !moved.has(blockId)) {
			moved.add(blockId);
			for (let i = 0; i < j; i++) {
				const [emptyId, emptyLength] = data[i];

				if (emptyId !== -1) continue;
				if (emptyLength < blockLength) continue;

				if (emptyLength > blockLength) {
					// Set (portion) of empty block to data block.
					data[i] = [blockId, blockLength];
					// data[i][0] = blockId;
					// data[i][1] = blockLength;

					// Mark data block as empty space.
					data[j] = [-1, blockLength];

					// Insert remaining portion of empty space at the end of the (new) data block.
					data.splice(i + 1, 0, [-1, emptyLength - blockLength]);

					break;
				}

				if (emptyLength === blockLength) {
					// Set empty block ID to data block ID.
					data[i][0] = blockId;

					// Mark data block as empty space.
					data[j][0] = -1;

					break;
				}
			}
		}

		j--;
	}

	return data
		.flatMap((block) => Array.from({ length: block[1] }, () => block[0]))
		.reduce((acc, val, i) => {
			if (val === -1) return acc;

			return acc + val * i;
		}, 0);
};

console.log("Part 1:", part1());
console.log("Part 2:", part2());

bench("Part 1", part1);
bench("Part 2", part2);

await run();
