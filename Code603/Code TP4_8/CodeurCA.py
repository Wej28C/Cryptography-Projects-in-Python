
from LBinaire603 import *
from abc import ABC, abstractmethod
class CodeurCA(object):
    """Un codeur doit surcharger les méthodes __init__ __repr__ __str__
    binCode, binDecode et codeurTest
    renvoyant et recevant un LBinaire603
    C'est une forme de classe abstraites"""
    def __init__(self ):
        pass

    def __str__(self):
        pass
    def __repr__(self):
        pass

    def binCode(self,monBinD:LBinaire603)->LBinaire603:
        pass
    def binDecode(self,monBinC:LBinaire603)->LBinaire603:
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
##    monCodeur=CodeurCA() #A modifier si repris dans une classe en héritant
##    for k in range(5):
##        monBin=LBinaire603.exBin603(num=k,taille=25)
##        print("Bin:",monBin)
##        monBinCr=monCodeur.binCode(monBin)
##        print("Bin Codée:",monBinCr)
##        print("monBinCr décodé est égal à Monbin ?",monCodeur.binDecode(monBinCr)==monBin)


