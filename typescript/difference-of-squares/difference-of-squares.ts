class Squares {

    squareOfSum: number;
    sumOfSquares: number;
    difference: number;

    constructor(private range: number) {

        this.squareOfSum = 0;
        this.sumOfSquares = 0;

        for (let i = 1; i <= this.range; i++) {
            this.squareOfSum += i;
            this.sumOfSquares += i * i;
        }

        this.squareOfSum *= this.squareOfSum;
        this.difference = this.squareOfSum - this.sumOfSquares;

    }
}

export default Squares