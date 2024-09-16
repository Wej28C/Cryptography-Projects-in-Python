#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:03:00 2024

@author: beatrice
"""

from LBinaire603 import *
from CodeurCA import CodeurCA
import matplotlib.pyplot as plt

class ChiffreurNaif(CodeurCA):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "ChiffreurNaif()"

    def __str__(self):
        return "Chiffreur naïf (XOR)"

    def binCode(self, monBinD: LBinaire603) -> LBinaire603:
        # Implémentation du chiffrement naïf (XOR)
        # Notez que pour cet exemple, nous utilisons simplement l'entrée comme étant sa propre "clé"
        if len(monBinD) == 0:
            return monBinD
        return LBinaire603([monBinD[0] ^ b for b in monBinD[1:]])

    def binDecode(self, monBinC: LBinaire603) -> LBinaire603:
        # La fonction de chiffrement naïf est réversible car elle utilise l'opération XOR
        return self.binCode(monBinC)


class FonctionHachageDaviesMeyer:
    def __init__(self, chiffreur: ChiffreurNaif):
        self.chiffreur = chiffreur

    def __repr__(self):
        return f"FonctionHachageDaviesMeyer(chiffreur={self.chiffreur})"

    def __str__(self):
        return f"Fonction de hachage Davies-Meyer (chiffreur={self.chiffreur})"

    def hacher(self, message: LBinaire603, iv: LBinaire603) -> LBinaire603:
        # Schéma Davies-Meyer pour la fonction de hachage
        hash_value = iv
        for block in message:
            hash_value = self.chiffreur.binCode(hash_value + LBinaire603([block]))
        return hash_value


# Testons la fonction de hachage Davies-Meyer
if __name__ == "__main__":
    # Création du chiffreur naïf
    chiffreur_naif = ChiffreurNaif()

    # Création de la fonction de hachage Davies-Meyer avec le chiffreur naïf
    fonction_hachage = FonctionHachageDaviesMeyer(chiffreur_naif)

    # Testons avec quelques exemples
    exemples_messages = [
        LBinaire603("hello"),
        LBinaire603("Salut les amies, ca va bien, comment ca se passe les etudes, vous avez des bonnes notes?"),
        LBinaire603("coucou maman, c'est quoi que t'as fait aujourd'hui à manger? J'en ai trop faim!"),
    ]
    iv = LBinaire603("initialization_vector")

    for message in exemples_messages:
        hash_value = fonction_hachage.hacher(message, iv)
        print(f"Message: {message}, IV: {iv}, Hash: {hash_value}")

    # Affichage de l'histogramme des fréquences de hashage
    valeurs_hash = [fonction_hachage.hacher(message, iv)[0] for message in exemples_messages]
    plt.hist(valeurs_hash, bins=range(256), density=True)
    plt.title("Histogramme des fréquences de hashage (Davies-Meyer)")
    plt.xlabel("Valeur de hachage")
    plt.ylabel("Fréquence")
    plt.show()
