class ArmstrongNumbers {
    static isArmstrongNumber(num: number): boolean {
        const digits = num.toString().split("").map(d => +d);
        const length = digits.length;
        const sum = digits.reduce((accumulator, current) =>
            Math.pow(current, length) + accumulator, 0);
        return num === sum;
    }
}

export default ArmstrongNumbers