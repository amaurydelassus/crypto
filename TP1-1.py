import TP1 as tp1
import operator

alphalist = tp1.alphalist
def attaque_brute_force_sa(text, alphalist):
    z = "Y"
    while (z == "Y"):
        print("Veuillez entrez un nombre quelconque")
        nb = input()
        t = tp1.cesarToText(text, int(nb), alphalist)
        print("Clef " + nb + " Text = " + t)
        # print("Continuer ? Y/N")
        # z = input()


c = tp1.textToCesar("bonjour a toutes et a tous, soyez les bienvenues", 3, alphalist)


# attaque_brute_force_sa(c, tp1.alphalist)

def e_attack(text, alphalist):
    attack = ["e", "a", "i", "s", "t", "n", "r", "u", "l", "o", "d", "m", "p", "c", "v", "q", "g", "b", "f", "j", "h",
              "z", "x", "y", "k", "w"]
    tab = tp1.occurenceOfLetter(text, alphalist)
    tab = sorted(tab.items(), key=lambda x: x[1], reverse=True)
    print(tab)
    i = 0
    z = "Y"
    while (z != "N"):
        key = lettreToKey(attack[i], tab[i][0], alphalist)
        t = tp1.cesarToText(text, key, tp1.alphalist)
        print("Clef " + str(key) + " Text = " + t)
        print("Continuer ?")
        z = input()
        i += 1
    return 'ok'


def lettreToKey(e, c, alphalist):
    return alphalist.index(c) - alphalist.index(e)


c = tp1.openFile("demo.txt")
c = tp1.textToCesar(c,13,alphalist)
print(e_attack(c, alphalist))

def indexC(text,alphalist):
    tab = tp1.occurenceOfLetter(text, alphalist)

def key_len(text):
    tab = tp1.occurenceOfLetter(text, alphalist)

def decode(filename):
    tab = tp1.occurenceOfLetter(filename, alphalist)

