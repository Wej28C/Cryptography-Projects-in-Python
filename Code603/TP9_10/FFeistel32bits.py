import arithmetiqueDansZ
from FBijection8bitsCA import FBijection8bitsCA
import random

def f4bitsExemple(x , cle):
    "Renvoie un nombre sur 4 bits"
    xx=int(x)%16
    b0=xx%2;xx//=2
    b1=xx%2;xx//=2
    b2=xx%2;xx//=2
    b3=xx%2
    return ((b1*8+b2*4+(b0+b1+b2+b3)*2+b3) ^ cle)%16

def flcle(cle,nb=16):
    "Renvoie une liste de clés"
    random.seed(int(cle))
    return [random.randint(0, 255) %16 for k in range(nb)]

class FFeistel8bits(FBijection8bitsCA):
     "Voir Introduction à la Cryptographie Dunod chap 5.1"
     def __init__(self,cle=7,fgenCle=flcle , f = f4bitsExemple,nbRounds=16):
         """La fonction f est une fonction  qui à (k,x) renvoie une valeur sur 4bits
         fgenCle renvoie une liste de nb clés à partir d'une graine k
         """
         self.cle,self.nbRounds = cle,nbRounds
         self.fgenCle=fgenCle
         self.f =f
         self.lk=self.fgenCle(cle=cle,nb=nbRounds)

     def __repr__(self):
         return f"FFeistel8bits(cle={self.cle},fgenCle={self.fgenCle},\n      f={self.f},nbRounds={nbRounds})"

     def __call__(self,_octet):
         octet=int(_octet)
         assert octet>=0 and octet <256

         l,r=octet//16, octet%16
         for i in range(self.nbRounds):
            l,r = r , l^self.f( x=r , cle=self.lk[i]   )

         return (r*16+l) % 256

     def valInv(self,octetC):
         """Renvoie l'antécédent de octetC
         >>> FFeistel8bits().valInv(FFeistel8bits()(7))
         7
         """

         r,l = octetC//16, octetC%16
         #print(l,r)
         for i in range(self.nbRounds-1,-1,-1):#de r-1 à 0 inclu
            r,l = l , r^self.f(x=l , cle=self.lk[i]  )

         return (l*16+r)%256

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    for nbRounds in [1,2,4,7,15]:
        f=FFeistel8bits(nbRounds=nbRounds)
        f.afficheGraphiquesDeDiffusionConfusion()
