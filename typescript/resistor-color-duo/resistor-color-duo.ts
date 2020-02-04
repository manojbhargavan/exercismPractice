export class ResistorColor {
  private colors: string[];

  constructor(colors: string[]) {
    if (!colors || colors.length < 2)
      throw Error("At least two colors need to be present");
    this.colors = colors;
  }
  value = (): number => {
    let colorCode = "";

    for (let i = 0; i < 2; i++) {
      switch (this.colors[i].toLowerCase()) {
        case "black": colorCode += "0"; break;
        case "brown": colorCode += "1"; break;
        case "red": colorCode += "2"; break;
        case "orange": colorCode += "3"; break;
        case "yellow": colorCode += "4"; break;
        case "green": colorCode += "5"; break;
        case "blue": colorCode += "6"; break;
        case "violet": colorCode += "7"; break;
        case "grey": colorCode += "8"; break;
        case "white": colorCode += "9"; break;
      }
    }

    return +colorCode;
  };
}
