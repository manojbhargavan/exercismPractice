class Transcriptor {
    toRna(dnaStrand: string): string {
        const dnaStrandArr: string[] = dnaStrand.split("");
        let rnaStrand = "";
        dnaStrandArr.forEach((curDnaStrand) => {
            let rna = "";
            try {
                rna = this.getRNA(curDnaStrand);
            }
            catch (e) {
                throw e;
            }
            rnaStrand += rna;
        });

        return rnaStrand;
    }

    private getRNA(strand: string): string {
        switch (strand.toUpperCase()) {
            case "G": return "C"; break;
            case "C": return "G"; break;
            case "T": return "A"; break;
            case "A": return "U"; break;
            default: throw Error("Invalid input DNA.");
        }
        return "";
    }
}

export default Transcriptor