import { bench, run } from "mitata";
import { equalTo, solve, type Constraint, type Model } from "yalps";
import { readInput } from "../utils";
import { combinations } from "../utils/combinations";

const input = await readInput();

const machines = input.map((line) => {
	const parts = line.split(" ");

	const lights = parts[0]
		.slice(1, -1)
		.split("")
		.reduce<Set<number>>((acc, val, i) => {
			if (val === "#") acc.add(i);
			return acc;
		}, new Set());

	const buttons = parts
		.slice(1, -1)
		.map(
			(button) =>
				new Set(button.matchAll(/\d+/g).map((el) => Number(el[0])))
		);

	const joltages = Array.from(
		parts
			.at(-1)!
			.matchAll(/\d+/g)
			.map((el) => Number(el[0]))
	);

	return { lights, buttons, joltages };
});

function findButtonCounts(
	lights: Set<number>,
	buttons: Array<Set<number>>
): number {
	for (let i = 1; i < buttons.length; i++) {
		for (const c of combinations(buttons, i)) {
			const result = c.reduce((acc, v) => acc.symmetricDifference(v));

			if (lights.symmetricDifference(result).size === 0) {
				return c.length;
			}
		}
	}

	return Infinity;
}

function partOne() {
	return machines.reduce(
		(total, machine) =>
			total + findButtonCounts(machine.lights, machine.buttons),
		0
	);
}

function generateModel({
	buttons,
	joltages,
}: {
	buttons: Array<Set<number>>;
	joltages: Array<number>;
}) {
	const baseModel = {
		direction: "minimize",
		objective: "cost",
		constraints: {} as Record<string, Constraint>,
		variables: {} as Record<string, Record<string, number>>,
		integers: true,
	} satisfies Model;

	// Set up constraints (required joltages)
	for (const [i, joltage] of joltages.entries()) {
		baseModel.constraints[i.toString()] = equalTo(joltage);
	}

	// Set up variables (buttons)
	for (const [i, button] of buttons.entries()) {
		const obj: Record<string, number> = { cost: 1 };

		for (const t of button.values()) {
			obj[t.toString()] = 1;
		}

		baseModel.variables[i.toString()] = obj;
	}

	return baseModel;
}

function partTwo() {
	return machines
		.map(generateModel)
		.reduce((total, model) => total + solve(model).result, 0);
}

console.log("Part 1:", partOne());
console.log("Part 2:", partTwo());

bench("Part 1", partOne);
bench("Part 2", partTwo);
run();
