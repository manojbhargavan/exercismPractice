function isLeapYear(year: number): boolean {
    //Every year that is evenly divisible by 4
    // Except every year that is evenly divisible by 100
    // Unless the year is also evenly divisible by 400
    return year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)
}

export default isLeapYear