#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      utilisateur
#
# Created:     14/01/2024
# Copyright:   (c) utilisateur 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
from LBinaire603 import *

def lFrequences(lb) :
    """Renvoie la liste des fréquences de chaque valeur
    Une fréquence est un nombre entre 0 et 1 et correspond à un pourcentage : 0.25=25 %
    >>> lFrequences(LBinaire603([1,2,3,3,3,3,4,8,8,128]))[3]
    0.4
    """
    lf = [0] * 256
    n = len(lb)
    for oc in lb:
        lf[oc] += 1 / n
    return lf

def afficheTableauDesFrequences(lb) :
    lf = lFrequences(lb)
    print(f"Tableau des fréquences de la liste de {lb}")
    t = ""
    for b, f in enumerate(lf):
        t += f"{b:02x}:{LBinaire603.lchr[b]}"
        t += f"{(f*100):5.1f}%|"
        if (b + 1) % 8 == 0:
             print(t)
             t =""
    print(t)


def afficheTableauDesFrequencesDecroissantes(lb) :
    lf = lFrequences(lb)
    lbTrie = sorted([k for k in range(256)], key=lambda b: lf[b], reverse=True)
    lbTriesNonNuls = [b for b in lbTrie if lf[b] > 0]

    print(f"Tableau des fréquences décroissantes de la liste de {lb}")
    s = ""

    for k, b in enumerate(lbTriesNonNuls):
        s += f"{b:02x}:{LBinaire603.lchr[b]}"
        s += f"{(lf[b]*100):5.1f}%|"
        if (k + 1) % 8 == 0:
             print(s)
             s = ""
        k += 1
    print(s)

def afficheHistogrammeDesFrequences(lb,titre="Histogramme des fréquences",nbValMax=20) :
    """
    nbValMax est le nombre de valeurs affichées, il est donc à mettre à 256
    pour avoir l’intégralité des valeurs affichées
    """
    lf = lFrequences(lb)
    lbTries = sorted([k for k in range(256)], key=lambda b: lf[b], reverse=True)
    lbTriesNonNuls = [b for b in lbTries if lf[b] > 0]

    lEtiquettes = [f"{b:02x}:{LBinaire603.lchr[b]}" for b in lbTriesNonNuls]
    lVal = [lf[b] for b in lbTriesNonNuls]

    plt.bar(lEtiquettes[:nbValMax], lVal[:nbValMax])
    plt.title(titre)
    plt.show()

def afficheHistogrammeDesFrequencesFichier(nomFic, titre="Histogramme des fréquences", nbValMax=20):
    lb = LBinaire603.bin603DepuisFichier(nomFic)
    lf = lFrequences(lb)
    lbTries = sorted([k for k in range(256)], key=lambda b: lf[b], reverse=True)
    lbTriesNonNuls = [b for b in lbTries if lf[b] > 0]

    lEtiquettes = [f"{b:02x}:{LBinaire603.lchr[b]}" for b in lbTriesNonNuls]
    lVal = [lf[b] for b in lbTriesNonNuls]

    plt.bar(lEtiquettes[:nbValMax], lVal[:nbValMax])
    plt.title(titre)
    plt.show()

def main():
    pass

if __name__ == '__main__':
    main()
    #lb_test = LBinaire603([1, 2, 3, 3, 3, 3, 4, 8, 8, 128])
    #afficheTableauDesFrequences(lb_test)
   # afficheTableauDesFrequencesDecroissantes(lb_test)
   # afficheHistogrammeDesFrequences(lb_test)
    #afficheHistogrammeDesFrequencesFichier("BelAmi.txt", "Histogramme des fréquences du fichier texte BelAmi")
    #afficheHistogrammeDesFrequencesFichier("Germinal.txt", "Histogramme des fréquences du fichier texte Germinal")
    #afficheHistogrammeDesFrequencesFichier("RougeNoir.txt", "Histogramme des fréquences du fichier texte RougeNoir")
    #afficheHistogrammeDesFrequencesFichier("Bovary.txt", "Histogramme des fréquences du fichier texte Bovary")
   #
    afficheHistogrammeDesFrequencesFichier("Coul10a.bmp", "Histogramme des fréquences du fichier image coula")
    afficheHistogrammeDesFrequencesFichier("Coul10b.bmp", "Histogramme des fréquences du fichier image coulb")
    afficheHistogrammeDesFrequencesFichier("tete.bmp", "Histogramme des fréquences du fichier image tete")

    #afficheHistogrammeDesFrequencesFichier("DocChiffre1.txt", "Histogramme des fréquences du fichier DocChiffre1")


