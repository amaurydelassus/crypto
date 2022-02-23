import TP1 as tp1

alphalist = tp1.alphalist


def attaque_brute_force_sa(text, alphalist):
    while (True):
        print("Veuillez entrez un nombre quelconque")
        nb = input()
        t = tp1.cesarToText(text, int(nb), alphalist)
        print("Clef " + nb + " Text = " + t)


c = tp1.textToCesar("bonjour a toutes et a tous, soyez les bienvenues", 3, alphalist)
print(c)
# attaque_brute_force_sa(c, tp1.alphalist)

def lettreToKey(e, c, alphalist):
    return alphalist.index(c) - alphalist.index(e)
def e_attack(text, alphalist):
    attack = ["e", "a", "i", "s", "t", "n", "r", "u", "l", "o", "d", "m", "p", "c", "v", "q", "g", "b", "f", "j", "h",
              "z", "x", "y", "k", "w"]
    text = tp1.clean(text)
    tab = tp1.occurenceOfLetter(text, alphalist)
    tab = sorted(tab.items(), key=lambda x: x[1], reverse=True)
    print(tab)
    i = 0
    z = "Y"
    while (z != "N"):
        key = lettreToKey(attack[0], tab[i][0], alphalist)
        t = tp1.cesarToText(text, key, tp1.alphalist)
        print("Clef " + str(key) + " Text = " + t)
        print("Continuer ?")
        z = input()
        i += 1
    return 'ok'

c = tp1.textToCesar("bonjour à toutes et a tous, soyez les bienvenues aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 3, alphalist)
# e_attack(c, tp1.alphalist)


def double_lettre(text):
    i = 1
    for char in text:
        if i == len(text):
            return ""
        if char == text[i]:
            return char
        i += 1


def ee_attack(text, alphalist):
    attack = ["m", "r", "c", "p", "d", "s", "t", "z", "g", "l", "f", "n"]
    text = tp1.clean(text)
    dl = double_lettre(text)
    print(dl)
    if dl != "":
        i = 0
        z = "Y"
        while (z != "N"):
            key = lettreToKey(attack[i], dl, alphalist)
            t = tp1.cesarToText(text, key, tp1.alphalist)
            print("Clef " + str(key) + " Text = " + t)
            print("Continuer ?")
            z = input()
            i += 1
    return 'ok'


c = tp1.openFile("demo.txt")
c = tp1.textToCesar(c, 3, alphalist)
print(ee_attack(c, alphalist))


def indexC(text, alphalist):
    global index
    tab = tp1.occurenceOfLetter(tp1.clean(text), alphalist)
    n, N = 0, 0
    for i in tab.items():
        q = int(i[1])
        n += q * (q - 1)
        N += q
    if (N * (N - 1)) != 0:
        index = n / (N * (N - 1))
    else:
        index = 0
    index = round(index, 4)
    return index


def decoupe(text, n):
    t = str(text)
    list = {}
    for x in range(0, n):
        list[x] = []
    for i in range(0, len(t)):
        mod = i % n
        list[mod].append(t[i])
    return list


def tab_to_str(tab):
    str = ""
    for i in tab:
        str += i
    return str


def decoupe_to_ic_tab(text):
    print(text)
    text = tp1.clean(text)
    text = text.replace(" ", "")
    tab = {}
    for i in range(1, len(text)):
        c = decoupe(text, i)
        x, ic = 0, 0
        for y in c.items():
            t = tab_to_str(y[1])
            ic += indexC(t, alphalist)
            x += 1
        ic = ic / x
        tab[i] = round(ic, 4)
    return tab

def len_key(text):
    tab = decoupe_to_ic_tab(text)
    tab = sorted(tab.items(), key=lambda x: x[1])
    return  tab
# print(len_key(c))
