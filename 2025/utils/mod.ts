// Because % is actually "remainder" in JS...
export function mod(n: number, m: number) {
    return ((n % m) + m) % m;
}