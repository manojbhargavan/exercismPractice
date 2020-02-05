export default class Triangle {

    sides: number[]

    constructor(...sides: number[]) {
        this.sides = sides
    }

    kind(): string {
        if (this.sides.length !== 3)
            throw new Error("Three sides required for a triangle");

        if (this.sides[0] <= 0 || this.sides[1] <= 0 || this.sides[2] <= 0)
            throw new Error("Side length cannot be zero or less than zero");

        if (this.sides[0] + this.sides[1] < this.sides[2] || this.sides[0] + this.sides[2] < this.sides[2]
            || this.sides[1] + this.sides[2] < this.sides[0])
            throw new Error("Triangle inequality");

        if (this.sides[0] === this.sides[1] && this.sides[0] === this.sides[2])
            return "equilateral";

        if (this.sides[0] === this.sides[1] || this.sides[0] === this.sides[2] || this.sides[1] === this.sides[2])
            return "isosceles";

        if (this.sides[0] !== this.sides[1] && this.sides[0] !== this.sides[2] && this.sides[1] !== this.sides[2])
            return "scalene";


        return ""
    }
}