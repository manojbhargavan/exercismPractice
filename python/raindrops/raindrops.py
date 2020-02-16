soundDict = {
    3: "Pling",
    5: "Plang",
    7: "Plong"
}


def convert(number):
    sounds = ""
    for soundIndex in soundDict:
        if number % soundIndex == 0:
            sounds += soundDict[soundIndex]
    if sounds == "":
        sounds = str(number)
    return sounds
