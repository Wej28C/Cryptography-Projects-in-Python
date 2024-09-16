#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      utilisateur
#
# Created:     09/02/2024
# Copyright:   (c) utilisateur 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from LBinaire603 import LBinaire603
from CodeurCA import CodeurCA
import matplotlib.pyplot as plt

class HachageNaif(CodeurCA):
    def __init__(self,hachage):
        self.hachage=hachage
    def __repr__(self):
        return f"HachageNaif:{self.hachage}"

    def __str__(self):
        return f"HachageNaif:{self.hachage}"

    def binCode(self, monBinD: LBinaire603) -> LBinaire603:
        # Fonction de hachage naïve (substitution simple)
        lb = LBinaire603(monBinD)
        resultat = 0
        for b in lb:
            resultat =(resultat+b) % 256
        return resultat

    def binDecode(self, monBinC: LBinaire603) -> LBinaire603:
        raise NotImplementedError  # Pas besoin de décodage pour ce hachage naïf


# Exemple d'utilisation
if __name__ == "__main__":
    #monCodeur = CodeurCA()  # Remplacez ceci par l'initialisation de votre codeur spécifique
    message = 3546678
    monHachage=HachageNaif(message)
    monBin=LBinaire603.exBin603(256,76)
    resultat_hash = monHachage.binCode(monBin)
    print(f"Message: {message}")
    print(f"Résultat binaire après hachage: {resultat_hash}")
    for c1 in "abcdefghijklmnopqrstuvwxyz":
        for c2 in "abcdefghijklmnopqrstuvwxyz":
            for c3 in "abcdefghijklmnopqrstuvwxyz":
                for c4 in "abcdefghijklmnopqrstuvwxyz":
                    h=monHachage.binCode("hellolesamishdjfozugfilkzsdoihezfjb"+c1+c2+c3+c4+"hellolesamishdjfozugfilkzsdoihezfjb")
                    print(h)

  #  tester_diffusion_confusion(monCodeur, message)
