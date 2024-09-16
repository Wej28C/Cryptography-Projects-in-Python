import arithmetiqueDansZ
from FBijection8bitsCA import FBijection8bitsCA

class FPermutationDes8Bits(FBijection8bitsCA):
    "Une Bijection triviale"
    def __init__(self,lp=[2,4,1,3,6,5,0,7]):
        "Fonction bijective sur [0..255] permutant les bits"
        "par exemple le bit 0 de l'image de arg sera la valeur du bit 2 de arg"
        assert len(lp)==8
        for k in range(8):assert k in lp
        self.lp=lp
        self.lpInv=[lp.index(k) for k in range(8)]

    def __repr__(self):
        return f"FPermutationDes8Bits({self.lp})"

    def __call__(self,octet):
        """
        renvoie l'image de octet
        >>> bin(FPermutationDes8Bits([7,1,2,3,4,5,6,0])(0b11001110))
        '0b1001111'
        >>> bin(FPermutationDes8Bits([1,0,2,3,4,5,6,7])(0b11001110))
        '0b11001101'
        """
        x=int(octet)
        lb=[0]*8
        for k in range(8):
            lb[self.lp[k]]=x%2
            x=x//2
        res=0;p2=1
        for k in range(8):
            res+=lb[k]*p2
            p2*=2
        return res
    def valInv(self,octet):
        x=int(octet)
        lb=[0]*8
        for k in range(8):
            lb[self.lpInv[k]]=x%2
            x=x//2
        res=0;p2=1
        for k in range(8):
            res+=lb[k]*p2
            p2*=2
        return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    FPermutationDes8Bits().afficheGraphiquesDeDiffusionConfusion()
    FPermutationDes8Bits([1,0,2,3,4,5,6,7]).afficheGraphiquesDeDiffusionConfusion()