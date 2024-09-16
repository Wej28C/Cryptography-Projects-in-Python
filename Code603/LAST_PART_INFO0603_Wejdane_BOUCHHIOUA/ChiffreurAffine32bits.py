from arithmetiqueDansZ import ElementDeZnZ,PGCD
from LBinaire603 import LBinaire603
from  CodeurCA import CodeurCA
class ChiffreurAffine32Bits(CodeurCA):
    """Théorie des codes p 150"""
    #2**32=4294967296 ~~ 4.3E9
    def __init__(self ,a=1234567899,b=987654321):
        self.a=ElementDeZnZ(a,4294967296)
        self.b=ElementDeZnZ(b,4294967296)
    def __str__(self):
        return f"Chiffreur affine 32 bits avec a={self.a} et b={self.b}"
    def __repr__(self):
        return f"ChiffreurAffine32Bits({self.a},{self.b})"

    def binCode(self,monBin):
        #On doit mémoriser la longueur totale de la liste à chiffrer
        lbc=LBinaire603([])
        lbc.ajouteLongueValeur(len(monBin))
        pos=0
        while pos<len(monBin):
            x,pos=monBin.lisMot32Bits(pos)
            y=(self.a*x+self.b) # se fait donc modulo 4294967296
            lbc.ajouteMot32Bits(y)
        return LBinaire603(lbc)

    def binDecode(self,monBinC):
        assert self.a.estInversible(),"{self.a=} doit être inversible et donc doit être premier avec 256"
        inva=self.a.inverse()
        monBinD=LBinaire603([])
        longueur,pos=monBinC.lisLongueValeur(0)

        while pos<len(monBinC):
            y,pos=monBinC.lisMot32Bits(pos)
            x=(y-self.b)*inva
            monBinD.ajouteMot32Bits(x)
        return LBinaire603(monBinD[:longueur])

    def demo():
        monBin=LBinaire603([0x01,0x02,0x010,0x20,0x40,0x80,0x00,0x01,0x02,0x010,0x20,0x40,0x80])
        for monCodeur in [ChiffreurAffine32Bits(),ChiffreurAffine32Bits(3,5),ChiffreurAffine32Bits(1,1),ChiffreurAffine32Bits(1,0)]:
            print(f"Codage avec {monCodeur} :")
            print("   Bin:       ",monBin)
            monBinC=monCodeur.binCode(monBin)
            print("   Bin Codé:  ",monBinC)
            monBinD=monCodeur.binDecode(monBinC)
            print("   Bin Décodé:",monBinD)
            print("   monBinD (décodé) est égal à Monbin ?",monBinD==monBin)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ChiffreurAffine32Bits.demo()

