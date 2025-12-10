export function* allCombinations<T>(array: T[]): Generator<T[]> {
	const N = array.length;

	for (let n = 1; n <= N; n++) {
		yield* combinations(array, n);
	}
}

export function* combinations<T>(
	array: T[],
	n: number = array.length
): Generator<T[]> {
	if (n < 0 || n > array.length) return;

	function* backtrack(
		start: number,
		currentCombination: T[]
	): Generator<T[]> {
		if (currentCombination.length === n) {
			yield [...currentCombination];
			return;
		}

		for (let i = start; i < array.length; i++) {
			yield* backtrack(i + 1, [...currentCombination, array[i]]);
		}
	}

	yield* backtrack(0, []);
}
