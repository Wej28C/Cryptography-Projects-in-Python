#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Wejdane
#
# Created:     28/02/2024
# Copyright:   (c) utilisateur 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from LBinaire603 import *
from CodeurCA import CodeurCA
from FBij64BitsDES import FBij64BitsDES
from TP7_hachage_naif_DaviesMeyer import *
from ChiffreurDES import liste16Cles
import matplotlib.pyplot as plt

class HachageDaviesMeyerDES(FonctionHachageDaviesMeyer):
    def __init__(self, chiffreur: FBij64BitsDES):
        super().__init__(chiffreur)

    def hacher(self, message: LBinaire603, iv: LBinaire603) -> LBinaire603:
        # Schéma Davies-Meyer pour la fonction de hachage avec DES
        hash_value = iv
        for block in message:
            # Chiffrement du bloc avec le chiffreur DES
            block_key = LBinaire603([block] * 8)  # Répétition du bloc pour obtenir 64 bits
            hash_value = hash_value + block_key

        return hash_value

# Testons la fonction de hachage Davies-Meyer avec DES
if __name__ == "__main__":
    # Création du chiffreur DES
    cle_des = 0x123556789ABDDEF0
    chiffreur_des = FBij64BitsDES(cle_des)

    # Création de la fonction de hachage Davies-Meyer avec DES
    fonction_hachage_des = HachageDaviesMeyerDES(chiffreur_des)

    # Testons avec quelques exemples
    exemples_messages = [
        LBinaire603("hello"),
        LBinaire603("Salut les amies, ca va bien, comment ca se passe les etudes, vous avez des bonnes notes?"),
        LBinaire603("coucou maman, c'est quoi que t'as fait aujourd'hui à manger? J'en ai trop faim!"),
    ]
    iv = LBinaire603("initialization_vector")

    for message in exemples_messages:
        hash_value = fonction_hachage_des.hacher(message, iv)
        print(f"Message: {message}, IV: {iv}, Hash: {hash_value}")
    #print(f"Message: {message}, IV: {iv}, Hash: {hash_value}")

    # Créez un histogramme
    plt.hist(hash_value, bins=50, density=True)
    plt.title('Distribution des valeurs hachées')
    plt.xlabel('Valeur hachée (entier)')
    plt.ylabel('Fréquence relative')
    plt.show()