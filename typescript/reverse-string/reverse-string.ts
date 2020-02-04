class ReverseString {
    static reverse(word: string): string {
        const charArr = word.split("");
        let reverseString = "";
        for (let i = charArr.length - 1; i >= 0; i--) {
            reverseString += charArr[i];
        }
        return reverseString;
    }
}

export default ReverseString
