#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 10:55:00 2024

@author: beatrice & wejdane
"""

from LBinaire603 import *
from CodeurCA import CodeurCA
import matplotlib.pyplot as plt

class FonctionHachageNaive(CodeurCA):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "FonctionHachageNaive()"

    def __str__(self):
        return "Fonction de hachage naïve (XOR)"

    def binCode(self, monBinD: LBinaire603) -> LBinaire603:
        # Implémentation de la fonction de hachage (XOR)
        hash_value = monBinD[0]
        for byte in monBinD[1:]:
            hash_value ^= byte
        return LBinaire603([hash_value])

    def binDecode(self, monBinC: LBinaire603) -> LBinaire603:
        raise NotImplementedError("La fonction de hachage n'est pas déchiffrable")


# Testons la fonction de hachage naïve
if __name__ == "__main__":
    # Création de la fonction de hachage naïve
    hacheur = FonctionHachageNaive()

   # Initialisation de la liste pour stocker les valeurs de hachage
valeurs_hash = []

# Chaîne principale pour le test
chaine_principale = "hellolesamishdjfozugfilkzsdoihezfjb"

# Boucles imbriquées pour générer différentes combinaisons de caractères à ajouter à la fin de la chaîne principale
for c1 in "abcdefghijklmnopqrstuvwxyz":
    for c2 in "abcdefghijklmnopqrstuvwxyz":
        for c3 in "abcdefghijklmnopqrstuvwxyz":
            for c4 in "abcdefghijklmnopqrstuvwxyz":
                # Construction de la chaîne de test en ajoutant les caractères à la fin de la chaîne principale
                chaine_test = chaine_principale + c1 + c2 + c3 + c4 + chaine_principale
                # Calcul de la valeur de hachage pour la chaîne de test et ajout à la liste
                hash_value = hacheur.binCode(LBinaire603(chaine_test))
                valeurs_hash.append(hash_value[0])

    # Affichage de l'histogramme des fréquences de hashage

    plt.hist(valeurs_hash, bins=range(256), density=True)
    plt.title("Histogramme des fréquences de hashage")
    plt.xlabel("Valeur de hachage")
    plt.ylabel("Fréquence")
    plt.show()
