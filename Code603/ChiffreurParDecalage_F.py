#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      utilisateur
#
# Created:     12/01/2024
# Copyright:   (c) utilisateur 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from CodeurCA import*
from LBinaire603 import*
class ChiffreurParDecalage(CodeurCA):

    def __init__(self,decalage):

        self.decalage=decalage

    def __str__(self):
         return f"Chiffreur par decalage:{self.decalage}"
    def __repr__(self):
         return f"Chiffreur par decalage:{self.decalage}"
    def binCode(self,monBinD:LBinaire603)->LBinaire603:

        lresult =[(b+self.decalage)%256 for b in monBinD]
        return LBinaire603(lresult)

    def binDecode(self,monBinC:LBinaire603)->LBinaire603:

        lresult =[(b-self.decalage)%256 for b in monBinC]
        return LBinaire603(lresult)

def main():
    pass

if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()
    monCodeur = ChiffreurParDecalage(decalage=5)

    for k in range(5):
        monBin = LBinaire603.exBin603(num=k, taille=25)
        print("Bin:", monBin)

        monBinCr = monCodeur.binCode(monBin)
        print("Bin Codée:", monBinCr)

        monBinDec = monCodeur.binDecode(monBinCr)
        print("monBinCr décodé est égal à Monbin ?", monBinDec == monBin)
