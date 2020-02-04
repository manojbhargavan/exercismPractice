class Words {
    count(sentence: string): Map<string, number> {
        const result = new Map<string, number>();
        for (let curWord of sentence.split(/\s+/)) {
            curWord = curWord.trim().toLowerCase();
            if (curWord && curWord !== "") {
                result.has(curWord) ? result.set(curWord, (+result.get(curWord)! + 1))
                    : result.set(curWord, 1);
            }
        }
        return result;
    }
}

export default Words