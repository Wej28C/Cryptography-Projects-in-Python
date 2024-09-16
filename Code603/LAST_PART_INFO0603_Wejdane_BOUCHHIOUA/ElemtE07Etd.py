import copy
from random import *
from math import sqrt,log
from sympy import isprime
from arithmetiqueDansZ import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


#Les méthodes magiques : https://blog.finxter.com/python-dunder-methods-cheat-sheet/
#Voir Au coeur du Bitcoin - Programmer la Blockchain ouverte - collection O'Reilly
#Voir https://www.johndcook.com/blog/2018/08/14/bitcoin-elliptic-curves/
class ElemtE07(object):
    "Ensemble des solutions de Y²=X^3+7 dans Fp Courbe secp256k1"
    def __init__(self,x,y=None,p=None):
        """
        Défini par deux ElementDeZnZ mais seul le modulo de x est utilisé . Celui de y doit donc lui être égal.
        Avec l'élément neutre ayant self.y='Inf'
        ElemtE07(7,6,11) doit renvoyer une erreur
        >>> ElemtE07(ElementDeZnZ(7,11),ElementDeZnZ(8,11))
        ElemtE07(7,8,11)
        >>>
        >>> ElemtE07(1,"Inf",11)
        ElemtE07(1,"INF",11)
        """
        if isinstance(x,ElemtE07):
            self.x,self.y= x.x, x.y
        else :
            self.x=ElementDeZnZ(x) if isinstance(x,ElementDeZnZ)  else ElementDeZnZ(x,p)

            if type(y) in [type(None),str]: #Elément neutre à l'infini
                self.y="INF"
            else:
                self.y=ElementDeZnZ(y) if isinstance(y,ElementDeZnZ) else ElementDeZnZ(y,self.x.n)
                assert isinstance(self.y,str) or (self.y**2==self.x**3+7)% self.x.n, f"{self=} ne vérifie pas l'équation"
                if isinstance(self.y, str) or (self.y**2 != self.x**3 + 7) % self.x.n:
                    print(f"Erreur pour {self.x=} {self.y=} : {self.y**2=} {self.x**3+7=}")

    def lDesElements(p=47):
        """
        >>> ElemtE07.lDesElements(5)
        [ElemtE07(0,"INF",5), ElemtE07(2,0,5), ElemtE07(3,2,5), ElemtE07(3,3,5), ElemtE07(4,1,5), ElemtE07(4,4,5)]
        >>> len(ElemtE07.lDesElements(11))
        12
        >>> ElemtE07(6,5,11) in (ElemtE07.lDesElements(11))
        True
        """
        assert sontPremiersEntreEux(7, p) and p > 2 and estPremier(p), "Ne rentrons pas dans les complications"
        l = [ElemtE07(0, "INF", p)]
        for x in range(0,p):
            for y in range(p):
                  if( ((y**2)%p) == (x**3+7)%p ):
                    l.append(ElemtE07(x,y,p))
        return l

    def __hash__(self):
        """Une fonction injective utilisée les ensembles et dans le chiffreur"""
        if isinstance(self.y,str):
            return 0
        else:
            return self.x.a*self.x.n+self.y.a

    def ElemtE07DepuisHash(h,p):
        """
        >>> h=ElemtE07(6,5,11).__hash__()
        >>> ElemtE07.ElemtE07DepuisHash(h,11)
        ElemtE07(6,5,11)
        """
        if h==0:
            return ElemtE07(0,"INF",p)
        else:
            return ElemtE07(h//p,h%p,p)

    def eDesElements(p=47,verbose=False):
        """
        >>> ElemtE07.eDesElements(5)==set(ElemtE07.lDesElements(5))
        True
        >>> ElemtE07(8,3,17) in (ElemtE07.eDesElements(17))
        True
        """
        assert sontPremiersEntreEux(7,p) and p>2 and estPremier(p)," Ne rentrons pas dans les complications et gardons (0,0) comme élément neutre"
        el=set([ElemtE07(0,"INF",p)])
        for x in range(0,p):
            y2=ElementDeZnZ(x**3+7,p)
            if y2.estUnCarre():
                e37=ElemtE07(ElementDeZnZ(x,p),y2.racineCarree())
                if verbose: print(f"Ajout {len(el)} de eDesElements {e37}")
                el.add(e37)
                el.add(-e37)
        return el
    def __str__(self):
        """
        >>> print(ElemtE07(ElementDeZnZ(3,47),ElementDeZnZ(9,47)))
        (3,9)[47]
        """
        if self==0: return "O(à l'infini)"
        else: return f"({self.x.a},{self.y.a})[{self.x.n}]"
    def __repr__(self):
        """
        """
        if isinstance(self.y,ElementDeZnZ): valy=self.y.a
        elif isinstance(self.y,str) :valy=f'"{self.y}"'
        else : valy=self.y
        return f"ElemtE07({self.x.a},{valy},{self.x.n})"

    def __add__(self,other):
        """
        >>> ElemtE07(2,2,11)+ElemtE07(3,1,11)
        ElemtE07(7,3,11)
        >>> (ElemtE07(3,"INF",47)+ElemtE07(3,9,47))+ElemtE07(3,"INF",47)
        ElemtE07(3,9,47)
        """
        if self==0:return other
        elif other==0 :return self
        elif self.x==other.x:
            if self.y+other.y==0 : return ElemtE07(0,"INF",self.x.n)
            elif self.y==other.y: return ElemtE07(0, "INF", self.x.n)
            else : assert f"{self} et {other} ne peuvent être tous deux des éléments de la même courbe"
        else:

        # Calcul de lambda
            lam = (other.y - self.y) / (other.x - self.x)
            x_res = lam**2 - self.x - other.x
            y_res = -(lam * (x_res - self.x) + self.y)
            return ElemtE07(x_res, y_res, self.x.n)



    def double(self):
        """
        >>> ElemtE07(2,2,11).double()
        ElemtE07(5,0,11)
        """
        if self == 0:
            return ElemtE07(0, "INF", self.x.n)
        else:
            # Calcul de lambda
            lam = (3 * self.x**2) * self.y.inverse() * 2
            x_res = lam**2 - 2 * self.x
            y_res = -(lam * (x_res - self.x) + self.y)
        return ElemtE07(x_res, y_res, self.x.n)

    def lOrbite(self):
        """
        >>> ElemtE07(2,2,11).lOrbite()
        [ElemtE07(2,2,11), ElemtE07(5,0,11), ElemtE07(2,9,11), ElemtE07(0,"INF",11)]
        """
        if self == 0:
         return [ElemtE07(0, "INF", self.x.n)]

        current_point = ElemtE07(self)
        orbit = [current_point]

        while True:
            current_point = current_point + ElemtE07(self.x, self.y, self.x.n)
            if current_point in orbit:
                break
            orbit.append(current_point)

        return orbit
    def __mul__(self,other):
        """
        >>> ElemtE07(6,5,11)*3
        ElemtE07(5,0,11)
        >>> ElemtE07(15,13,17)*0
        ElemtE07(0,"INF",17)
        """
        k=other.a if isinstance(other,ElementDeZnZ) else other
        if k==0 or self==0: return ElemtE07(0,"INF",self.x.n)
        if k<0 : return (-self)*(-k)
        elif k==1 : return ElemtE07(self)
        else:
            result = ElemtE07(0, "INF", self.x.n)
            addend = ElemtE07(self)
            while k > 0:
                if k % 2 == 1:
                    result += addend
                addend = addend.double()
                k //= 2
            return result

    def __rmul__(self,other):
        """
        >>> 2*ElementDeZnZ(3,10)
        ElementDeZnZ(6,10)
        >>> 2*(ElemtE07(3,"INF",47)+3*ElemtE07(3,9,47))+ElemtE07(3,"INF",47)
        ElemtE07(43,32,47)
        """
        return self.__mul__(other)

    def __eq__(self,other):
        """
        >>> 3*ElemtE07(6,5,11)==ElemtE07(5,0,11)
        True
        >>> ElemtE07(0,"Inf",47)==0
        True
        >>> ElemtE07(3,9,47)==ElemtE07(3,"Inf",47) or ElemtE07(3,"Inf",47)==ElemtE07(3,9,47)
        False
        """
        if isinstance(other,int):# test ==0
            assert other==0,f" Test d'égalité avec un int non nul !! {other}"
            return isinstance(self.y,str)
        elif isinstance(self.y,str):
                return isinstance(other.y,str)
        elif isinstance(other.y,str):
                return isinstance(self.y,str)
        else :
            return (self.x==other.x) and (self.y==other.y)

    def __neg__(self):
        """
        >>> -ElemtE07(7,3,11)
        ElemtE07(7,8,11)
        """
        return ElemtE07(self.x, -self.y, self.x.n)
    def __sub__(self,other):
        """
        >>> ElemtE07(3,10,11)-ElemtE07(7,3,11)
        ElemtE07(4,7,11)
        >>> ElemtE07(3,9,47)-ElemtE07(3,9,47)==0
        True
        """
        return self + (-other)
    def ordreCourbe(p=17):
        """
        >>> ElemtE07.ordreCourbe(11)
        12
        """
        return len(ElemtE07.lDesElements(p))
    def ordrePoint(self):
        """
        >>> ElemtE07(3,10,11).ordrePoint()
        3
        >>> ElemtE07(7,3,11).ordrePoint()
        12
        """
        return len(self.lOrbite())
    def estGenerateur(self):
        """
        >>> ElemtE07(7,3,11).estGenerateur()
        True
        >>> ElemtE07(3,10,11).estGenerateur()
        False
        """
        return ElemtE07.ordreCourbe(self.x.n)==self.ordrePoint()
    def lDesElementsGenerateurs(p=47):
        """
        >>> ElemtE07.lDesElementsGenerateurs(11)
        [ElemtE07(4,4,11), ElemtE07(4,7,11), ElemtE07(7,3,11), ElemtE07(7,8,11)]
        """
        return [e for e in ElemtE07.lDesElements(p) if e.estGenerateur()]

    def lDesElementsDOrdrePremier(p=47):
        """
        >>> ElemtE07.lDesElementsDOrdrePremier(11)
        [ElemtE07(3,1,11), ElemtE07(3,10,11), ElemtE07(5,0,11)]
        """
        return [e for e in ElemtE07.lDesElements(p) if estPremier(e.ordrePoint())]
    def elemtE07APartirDeX(x:ElementDeZnZ):
        """
        Renvoie un point avec x ou une valeur proche de x comme abscisse
        >>> ElemtE07.elemtE07APartirDeX(ElementDeZnZ(2,11))
        ElemtE07(2,2,11)
        """
        xx,p=ElementDeZnZ(x),x.n
        assert p%2==1
        y2=xx**3+7
        while not(y2.estUnCarre()):  #yy est une racine carré
            xx=xx+1
            y2=xx**3+7
        #print(xx,y2)
        return ElemtE07(xx,y2.racineCarree())
    def randElemtE07(p):
        """Renvoie un élément non nul au hasard"""
        return ElemtE07.elemtE07APartirDeX(ElementDeZnZ(randint(0,p-1),p))
    def randGenerateurE07(p=47):
        """Renvoie un élément non nul au hasard
        >>> ElemtE07.randGenerateurE07(47).estGenerateur()
        True
        """
        el=ElemtE07.eDesElements(p)
        lel=list(el)
        r=choice(lel)
        while r.ordrePoint()!=len(lel):
            r=choice(lel)
        return r

    def affichePointMaxDOrdresPremier():
        p=7
        while p<1000:
            p=nbPremierSuivant(p)
            le=ElemtE07.lDesElementsDOrdrePremier(p)
            GMax,omax=None,-1
            for e in le:
                ord=e.ordrePoint()
                if ord>omax:
                    GMax,omax=ElemtE07(e),ord
            print(f"Avec F{p} l'ordre premier max est atteint avec {GMax} et vaut : {omax}")
    def afficheGraphique1(p,nbgmax=35):
        #matplotlib.rcParams['text.usetex'] = True # Faire import matplotlib

        plt.grid(True, lw = 1,markevery=1)
        #plt.axis('equal')
        plt.yticks(range(-p,p+1))
        plt.xticks(range(int(-((p*p+7)**1/3)),p+1))
        kmin,kmax=-p,p*p
        if nbgmax>0:
            kmin,kmax=max(-int(sqrt(nbgmax)),-p),min(nbgmax,p**2)
        for k in range(kmin,kmax):
            ly=np.linspace(-p,p,1001)

            lx=[(y**2+k*p-7)**(1/3) if (y**2+k*p-7)>=0 else -(7-y**2-k*p)**(1/3) for y in ly]
            if -2<k<3:
                s=f"Y^2 = X^3-7 {-k:+2}×{p}"
                st=r""
                plt.plot(lx,ly,"-",label=r"$"+s+"$")
            else:
                plt.plot(lx,ly,"-")
        plt.legend(loc='upper right') #Pour afficher les label définis plus haut
        le=ElemtE07.lDesElements(p)
        lx,ly=[],[]
        #print(le)
        for e in le:
            if e!=0:
                lx.append(e.x.a  )
                ly.append(e.y.a if e.y.a<=p//2 else e.y.a-p)
        print(lx,ly)
        plt.plot(lx,ly,"*r")
        plt.show()

    def demo(p=67,nbgmax=10):
        """
        Voir https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc

        """
        le=ElemtE07.lDesElements(p)
        print(f"Liste des {len(le)}  élements des solutions à Y**2==X**3+7 modulo {p} :")
        print(le)
        print(f"Soit {len(le)} éléments")
        print(f"Liste des élements d'ordre Premier : ")
        leop=ElemtE07.lDesElementsDOrdrePremier(p)
        for e in leop:
            print(f"{e}:{e.ordrePoint()}",end="")

        print()
        print(f"Liste des {len(le)}  élements des solutions à Y**2==X**3+7 modulo {p} :")
        print()
        P,Q=le[1],le[2]
        print(f"{P}+{Q}={P+Q}")
        print(f"{P}-{P}==0 : {P-P==0}")

        lop=P.lOrbite()
        print(f"L'orbite de {P=} a {len(lop)} éléments :")
        print(lop)
        #Démo Graphe1
        print(ElemtE07.lDesElements(p))
        ElemtE07.afficheGraphique1(p)
        for p in [3,5,11,13]:
            print(ElemtE07.lDesElements(p))
        ElemtE07.afficheGraphique2(p)

    def afficheTable(p=13):
        """Affiche le tableau de toutes les sommes possibiles"""
        le=ElemtE07.lDesElements(p)

        for row in le:
            for col in le:
                print(f"{row} + {col} = {row + col}")


    def afficheClesPourCodage(p=65537,essaiCle=12345):
        x=ElementDeZnZ(essaiCle,p)
        M=ElemtE07.elemtE07APartirDeX(x)
        print(M)
        e=ElemtE07.randElemtE07(p)
        print(f"{e=}")
        #el=ElemtE07.eDesElements(p)
        #print(el)
        g=ElemtE07.randGenerateurE07(p)
        print(f"{g=}")

    def demoChiffre(nbBitsCle=32):
            p=nbPremierAleaParNbBits(nbBitsCle*2)
            k=nbPremierAleaParNbBits(nbBitsCle*2)

            le=ElemtE07.lDesElements(p)
            print(f"Liste des {len(le)}  élements des solutions à Y**2==X**3+7 modulo {p} :")
            print(le)
            print(f"Soit {len(le)} éléments")
            print()
            leop=ElemtE07.lDesElementsDOrdrePremier(p)
            for A in leop:
                print(f"{A} a pour ordre premier : {A.ordrePoint()}")



if __name__ == "__main__":


    p=17
    ElemtE07.demo(p)
    ElemtE07.afficheTable(p=p)



    import doctest
    doctest.testmod()
