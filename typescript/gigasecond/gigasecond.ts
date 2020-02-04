class Gigasecond {
    constructor(private dateIn: Date) {
        this.dateIn.setSeconds(this.dateIn.getSeconds() + 1000000000);
    }

    date(): Date {
        return this.dateIn;
    }

}

export default Gigasecond
