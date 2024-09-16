from arithmetiqueDansZ import ElementDeZnZ,PGCD
from LBinaire603 import LBinaire603
from CodeurCA import CodeurCA
class ChiffreurAffine(CodeurCA):
    """Théorie des codes p 150"""
    def __init__(self ,a=13,b=5):
        assert ElementDeZnZ(a,256).estInversible(),"a doit être inversible et donc doit être premier avec 256"
        self.a=ElementDeZnZ(a,256)
        self.b=ElementDeZnZ(b,256)
    def __str__(self):
        return f"Chiffreur affine avec a={self.a} et b={self.b}"
    def __repr__(self):
        return f"ChiffreurAffine({repr(self.a)},{repr(self.b)})"

    def binCode(self,monBinD):
        """
        >>> ChiffreurAffine(3,1).binCode(LBinaire603("Bonjour"))
        LBinaire603([ 0xc7, 0x4e, 0x4b, 0x3f, 0x4e, 0x60, 0x57])
        """
        lbc=[(self.a*x+self.b) for x in monBinD]
        return LBinaire603(lbc)

    def binDecode(self,monBinC):
        """
        >>> ChiffreurAffine(3,1).binDecode(LBinaire603([ 0xc7, 0x4e, 0x4b, 0x3f, 0x4e, 0x60, 0x57])).toString()
        'Bonjour'
        """
        lb=[((y-self.b)//self.a) for y in monBinC]
        return LBinaire603(lb)

    def demo():
        monBin=LBinaire603([0x00,0x01,0x02,0x010,0x20,0x40,0x80])
        for monCodeur in [ChiffreurAffine(3,5),ChiffreurAffine(1,1),ChiffreurAffine(1,0)]:
            print()
            print(f"Codage avec {monCodeur} :")
            print("   Bin:         ",monBin)
            monBinC=monCodeur.binCode(monBin)
            print("   Bin Codé:    ",monBinC)
            monBinD=monCodeur.binDecode(monBinC)
            print("   Bin Décodé : ",monBinD)
            print("   monBinD (décodé) est égal à Monbin ?",monBinD==monBin)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ChiffreurAffine.demo()

