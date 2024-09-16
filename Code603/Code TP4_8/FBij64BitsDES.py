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
from FBijections32Bits import*
from ChiffreurDES import *

class FBij64BitsDES(FBijection32BitsCA):
    """Une classe abstraite de bijection sur des mots de 64 bits"""

    def __init__(self, cle, verbose=False):
        super().__init__()
        self.cle = cle
        self.verbose = verbose
        self.cles = liste16Cles(self.cle, self.verbose)  # Génère les 16 clés de tour

    def __repr__(self):
        return f"FBij64BitsDES({self.cle=:016x})"

    def __call__(self, mot64bits):
        """
        >>> hex(FBij64BitsDES(0x0e329232ea6d0d73)(0x8787878787878787))
        '0x0'
        >>> hex(FBij64BitsDES(0x123556789ABDDEF0)(0x0123456789ABCDEF))
        '0x85e813540f0ab405'
        """
        # Permutation initiale
        mot_permute = intImage(mot64bits, tPI, 64)
        L, R = mot_permute >> 32, mot_permute & 0xFFFFFFFFFFFFFFFF

        # 16 rounds de Feistel
        for i in range(1, 17):
            L, R = R, L ^ functionF(R, self.cles[i])

        # Combinaison de R et L (Note: L et R sont inversés dans la dernière étape)
        mot_combine = (R << 32) | L

        # Permutation finale
        mot_final = intImage(mot_combine, tPIm1, 64)
        return mot_final

    def valInv(self, mot64bitsChiffre):
        """
        >>> hex(FBij64BitsDES(0x0e329232ea6d0d73).valInv(0x0000000000000000))
        '0x8787878787878787'
        >>> hex(FBij64BitsDES(0x123556789ABDDEF0).valInv(0x85e813540f0ab405))
        '0x123456789abcdef'
        """
        # Permutation initiale inverse
        mot_permute = intImage(mot64bitsChiffre, tPI, 64)
        L, R = mot_permute >> 32, mot_permute & 0xFFFFFFFFFFFFFFFF

        # 16 rounds de Feistel en ordre inverse
        for i in range(16, 0, -1):
            L, R = R, L ^ functionF(R, self.cles[i])

        # Combinaison de R et L (Note: L et R sont inversés dans la dernière étape)
        mot_combine = (R << 32) | L

        # Permutation finale inverse
        mot_final = intImage(mot_combine, tPIm1, 64)
        return mot_final

# Exemple d'utilisation
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    cle_des = 0x123556789ABDDEF0
    f_bij64_bits_des = FBij64BitsDES(cle_des)

    mot64bits = 0x0123456789ABCDEF
    mot_chiffre = f_bij64_bits_des(mot64bits)
    mot_dechiffre = f_bij64_bits_des.valInv(mot_chiffre)

    print(f"Mot original: {hex(mot64bits)}")
    print(f"Mot chiffré: {hex(mot_chiffre)}")
    print(f"Mot déchiffré: {hex(mot_dechiffre)}")
