import arithmetiqueDansZ
from FBijection8bitsCA import FBijection8bitsCA

class FBijMasque8bits(FBijection8bitsCA):
     "Une Bijection trop simple"
     def __init__(self,oMasque=0b10101010 ):
         self.oMasque=oMasque

     def __repr__(self):
         return f"FBijMasque8bits({self.oMasque})"

     def __call__(self,octet):
         return int(octet)^self.oMasque

     def valInv(self,octetC):
         """Renvoie l'antécédent de octetC
         >>> FAffine8bits().valInv(FAffine8bits()(123))
         123
         """
         return int(octetC)^self.oMasque

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    FBijMasque8bits().afficheGraphiquesDeDiffusionConfusion()
    FBijMasque8bits(0b11001010).afficheGraphiquesDeDiffusionConfusion()
