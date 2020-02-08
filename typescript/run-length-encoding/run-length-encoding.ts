class RunLengthEncoding {
    static encode(encodeStr: string): string {
        const encodeArray = encodeStr.split("");
        if (encodeArray.length === 0) return "";
        let prevChar: string = encodeArray[0];
        let runningTotal = 1;
        let encodedString = "";
        for (let i = 1; i < encodeArray.length; i++) {
            if (prevChar === encodeArray[i]) {
                runningTotal++;
            }
            else {
                encodedString += runningTotal === 1 ? prevChar : `${runningTotal}${prevChar}`;
                runningTotal = 1;
            }
            prevChar = encodeArray[i];
        }
        encodedString += runningTotal === 1 ? prevChar : `${runningTotal}${prevChar}`;
        return encodedString;
    }

    static decode(encodedStr: string): string {
        const encodeArray = encodedStr.split("");
        if (encodeArray.length === 0) return "";
        let runningTotal = 0;
        let decodedString = "";
        for (let i = 0; i < encodeArray.length; i++) {
            if (encodeArray[i].match(/[0-9]/)) {
                runningTotal = runningTotal * 10 + +encodeArray[i];
            }
            else {
                decodedString += runningTotal === 0 ? encodeArray[i] : encodeArray[i].repeat(runningTotal);
                runningTotal = 0;
            }
        }
        return decodedString;
    }
}

export default RunLengthEncoding