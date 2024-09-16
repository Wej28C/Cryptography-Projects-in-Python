#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wejdene
#
# Created:     28/02/2024
# Copyright:   (c) utilisateur 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from math import log
from LBinaire603 import *

class Entropie(LBinaire603):
    def entropie(self):
        # Calcul de l'entropie sur un octet
        freq = [0] * 256
        total = len(self)

        for octet in self:
            freq[octet] += 1

        entropie = 0
        for f in freq:
            if f > 0:
                p = f / total
                entropie -= p * log(p, 2)

        return entropie

    def entropieDictionnaire(self):
        # Calcul de l'entropie sur un dictionnaire de deux octets
        freq = {}
        total = len(self) // 2

        for i in range(0, len(self)-1, 2):
            octet1 = self[i]
            octet2 = self[i + 1]
            key = (octet1, octet2)
            if key in freq:
                freq[key] += 1
            else:
                freq[key] = 1

        entropie = 0
        for f in freq.values():
            p = f / total
            entropie -= p * log(p, 2)

        return entropie

# Exemple d'utilisation des fonctions
nouveauLBinaire = Entropie([1, 2, 3, 4, 5])
entropie_octet = nouveauLBinaire.entropie()
entropie_dictionnaire = nouveauLBinaire.entropieDictionnaire()

print(entropie_octet)
print(entropie_dictionnaire)