#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      utilisateur
#
# Created:     15/12/2023
# Copyright:   (c) utilisateur 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from LBinaire603 import *
from CodeurCA import*
class ChiffreurparDecalage(CodeurCA)
def __init__(self ):
    super().__init__(self)

def __str__(self):
    super().__str__(self)

def  __repr__(self):
    super().__repr__(self)

def binCode(self,monBinD):
    """
    >>> #ici on fait des tests avec le run
    """
        lresult =[(b+self.decalage)%256 for b in monBinD]
        return LBinaire603(lresult)
        lres=LBinaire603([])
        for b in monBinD:
            lres.append((b+self.decalage)%256)
        return  lres #Binaire603
def binDecode(self,monBinC):

if __name__ == '__main__':
import doctest
    doctest.testmod()
    c=ChiffreurparDecalage(5)
