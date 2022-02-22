alphalist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]


def clean(text):
    accent = {"à": "a", "á": "a", "â": "a", "ã": "a", "ä": "a", "å": "a", "ç": "c", "è": "e", "é": "e", " ê": "e",
              "ë": "e", "ì": "i", "í": "i", "î": "i", "ï": "i", "ñ": "n", "ò": "o", "ó": "o", "ô": "o", "õ": "o",
              "ö": "o", "ù": "u", "ú": "u", "û": "u", "ü": "u", "ý": "y", "ÿ": "y"}
    text = text.lower()
    for a in accent:
        text = text.replace(a, accent[a])
    return text


# print(clean("Coàc ou"))


def occurenceOfLetter(text, alphalist):
    tab = {}
    for a in alphalist:
        tab[a] = 0
    for a in text:
        if a in alphalist:
            tab[a] = tab[a] + 1
    return tab


# print(occurenceOfLetter(clean("Coàcou"), alphalist))


def rateOfLetter(text, alphalist):
    tab = occurenceOfLetter(text, alphalist)
    for a in tab:
        tab[a] = "%.3f" % (tab[a] / len(text))
    return tab


# print(rateOfLetter(clean("Coàcou"), alphalist))


def openFile(filename):
    f = open(filename, mode='r', encoding='utf-8')
    file = f.read()
    f.close()
    return file


# print(openFile("demofile"))


def writeFile(filename, text):
    f = open(filename, mode='w', encoding='utf-8')
    f.write(text)
    f.close()
    return "OK"


# print(writeFile("demofile", "Bonjour"))


def charToCesar(char, key, alphalist):
    if char in alphalist:
        key = alphalist.index(char) + key
        char = alphalist[key % len(alphalist)]
    return char


# print(charToCesar("a", 3, alphalist))


def cesarToChar(char, key, alphalist):
    if char in alphalist:
        key = alphalist.index(char) - key
        char = alphalist[key % len(alphalist)]
    return char


# print(cesarToChar("z", 3, alphalist))


def textToCesar(text, key, alphalist):
    newStr = ""
    for char in text:
        newStr += charToCesar(char, key, alphalist)
    return newStr


# print(textToCesar("abcdefghijqlmnopqrstuvwxyz", 3, alphalist))


def cesarToText(text, key, alphalist):
    newStr = ""
    for char in text:
        newStr += cesarToChar(char, key, alphalist)
    return newStr


# print(cesarToText("defghijklmqopqrstqrvwxyzabc", 3, alphalist))


def fileToCesar(filename, key, alphalist):
    file = openFile(filename)
    text = textToCesar(file, key, alphalist)
    new_file_name = filename + "_code.txt"
    writeFile(new_file_name, text)
    return "OK"


# print(fileToCesar("demofile", 3, alphalist))


def textToVig(text, key, alphalist):
    newStr = ""
    i = 0
    for char in text:
        newKey = key[i % len(key)]
        newStr += charToCesar(char, newKey, alphalist)
        i += 1
    return newStr


key = [3, 5, 6]


# print(textToVig("azertyuiop", key, alphalist))


def vigToText(text, key, alphalist):
    newStr = ""
    i = 0
    for char in text:
        newKey = key[i % len(key)]
        newStr += cesarToChar(char, newKey, alphalist)
        i += 1
    return newStr


# print(vigToText("dekuyexnus", key, alphalist))

def fileToVig(filename, key, alphalist):
    file = openFile(filename)
    text = textToVig(file, key, alphalist)
    new_file_name = filename + "_vcode.txt"
    writeFile(new_file_name, text)
    return "OK"


# print(fileToVig("dekuyexnus", key, alphalist))

def vigToFile(filename, key, alphalist):
    file = openFile(filename)
    text = vigToText(file, key, alphalist)
    new_file_name = filename.replace("_vcode.txt", "")
    writeFile(new_file_name, text)
    return "OK"

# print(vigToFile("demofile_vcode.txt", key, alphalist))
