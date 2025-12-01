export class Grid {
    points: Map<string, string>
    width: number;
    height: number;

    constructor(input?: string[]) {
        this.points = new Map()
        this.width = 0;
        this.height = 0;

        if (input) {
            this.parse(input);
        }
    }

    parse<T>(stringArray: string[]) {
        for (let y = 0; y < stringArray.length; y++) {
            for (let x = 0; x < stringArray[y].length; x++) {
                const val = stringArray[y][x];

                this.points.set(`${y},${x}`, val)
            }
        } []

        this.height = stringArray.length;
        this.width = stringArray[0].length

        return this;
    }

    toString() {
        let str = "";

        for (let y = 0; y < this.height; y++) {
            for (let x = 0; x < this.width; x++) {
                str += this.get(y, x)
            }
            str += "\n"
        }

        return str;
    }

    get(y: number, x: number) {
        return this.points.get(`${y},${x}`)
    }

    find(val: string): [number, number] | undefined {
        const key = this.points.keys().find(key => this.points.get(key) === val)

        return key ? key.split(",").map(Number) as [number, number] : undefined;
    }

    findAll(val: string) {
        const positions: [number, number][] = [];

        this.points.entries().forEach(([pos, v]) => {
            if (v === val) {
                positions.push(pos.split(",").map(Number) as [number, number]);
            }
        })

        return positions
    }

    // getRow(y: number) {
    //     if (y < 0) throw new Error("Specified index is out of bounds. Too low.")
    //     if (y > this.height - 1) throw new Error("Specified index is out of bounds. Too high.")

    //     return this.points.entries().filter([pos] => )
    // }
}

const grid = new Grid([".#", "#."])

