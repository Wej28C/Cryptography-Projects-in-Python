
from LBinaire603 import LBinaire603
from LBinaire603 import LBinaire603

from arithmetiqueDansZ import *
from ElemtE07Etd import ElemtE07
from math import log

class ChiffreurE07(object):
    """Chiffreur à partir de la courbe elliptique sur F65537"""
    def __init__(self,a,B,G=ElemtE07(47106,21934,65537),p =65537):
        """Dans les valeurs par défaut B=54321*G
        """
        assert log(p,2)>16 #Il faut sufisamment d'éléments pour pouvoir chiffrer des octets
        self.a = a
        self.B = B
        self.G = G
        self.p = p
        self.A = a * G

    def getClePublique(): return self.A

    def __str__(self):
        return f"CodeurE0765537 avec la clé privé {self.a=} et sa clé publique {self.A=}, la clé publique d'un tier {self.B=}, avec comme point générateur {self.G=} sur F{self.p}"
    def __repr__(self):
        return f"CodeurE0765537({self.a},{self.B},{self.G},{self.p})"

    def binCode(self,monBinD:LBinaire603)->LBinaire603:
        """ """
        monBinC=LBinaire603()
        for b in monBinD:
            m=b*256
            M=ElemtE07.elemtE07APartirDeX(ElmtZnZ(m,self.p))
            k = randint(2, self.p - 2)
            C1 = k * self.G
            C2 = M + k * self.B
            monBinC.ajouteMot64Bits(C1.__hash__())
            monBinC.ajouteMot64Bits(C2.__hash__())
           # monBinC.ajouteMot64Bits(MP.__hash__())
        return monBinC
    def binDecode(self,monBinC:LBinaire603)->LBinaire603:
        pos=0
        monBinD=LBinaire603()
        while pos<len(monBinC):
            h1,pos=monBinC.lisMot64Bits(pos)
            #MP=ElemtE07.ElemtE07DepuisHash(h,self.p)

            h2, pos = monBinC.lisMot64Bits(pos)
            C1 = ElemtE07.ElemtE07DepuisHash(h1, self.p)
            C2 = ElemtE07.ElemtE07DepuisHash(h2, self.p)

            MP = C2 - self.a * C1

            monBinD.ajouteOctet(M.x.a//256)
        return monBinD

#G=ElemtE07(47106,21934,65537)
#raise NotImplementedError

#mes=Texte603("Bonjour les amis !")
#print(f"Message à coder :{mes}")
#binc=ca.binCode(mes.toLBinaire603())
#print(f"Message chiffré avec la clé secrète de {a=} et la clé publique {B=} :{Texte603(binc)}")
#bind=cb.binDecode(binc)
#print(f"Message déchiffré avec la clé secrète de {b=} et la clé publique {A=} :{Texte603(bind)}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    a = randint(2, 65535)
    B = randint(2, 65535)
    ca = ChiffreurE07(a, B)

    b = randint(2, 65535)
    A = randint(2, 65535)
    cb = ChiffreurE07(b, A)

    message = "Bonjour les amis !"
    print(f"Message à coder : {message}")
    binc = ca.binCode(LBinaire603([ord(c) for c in message]))
    print(f"Message chiffré avec la clé secrète de {a=} et la clé publique {B=} : {binc}")
    bind = cb.binDecode(binc)
    print(f"Message déchiffré avec la clé secrète de {b=} et la clé publique {A=} : {"".join(map(chr, bind))}")