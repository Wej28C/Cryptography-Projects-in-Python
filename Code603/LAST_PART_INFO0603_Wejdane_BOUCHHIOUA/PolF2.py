#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
from random import *
from math import sqrt,log
from sympy import isprime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from arithmetiqueDansZ import strExp #Pour avoir de jolis exposants


#Les méthodes magiques : https://blog.finxter.com/python-dunder-methods-cheat-sheet/

class PolF2(object):
    "Polynôme dans F2"
    def __init__(self,x):
        """
        Défini par une liste d' ElmntZnZ
        >>> PolF2([1,0,1,0,1])
        PolF2(0b10101)
        >>> PolF2(0b1000110010) #Entier -> Polynome dans F2
        PolF2(0b1000110010)
        >>> PolF2(0)
        PolF2(0b0)
        """
        self.lcoef=[]
        if isinstance(x,list):
            for e in x:
                assert isinstance(e,int)
                self.lcoef.append(int(e))
        elif  isinstance(x,PolF2):
            self.lcoef=(x.lcoef).copy()
        else:
            if x==0:
                self.lcoef=[0]
            else:
                val=x
                while val>0:
                    self.lcoef.append(val%2)
                    val=val//2
        while len(self.lcoef)>1 and self.lcoef[-1]==0:
            self.lcoef.pop() #On enlève les coefficients de plus haut degré qui sont nuls

    def __hash__(self):
        """
        >>> PolF2(0b100011).__hash__()
        35
        """
        return int(self)


    def __str__(self):
        """
        >>> print(PolF2(0b110010))
        X⁵+X⁴+X
        >>> print(PolF2(2**16))
        X¹⁶
        >>> print(PolF2([0, 1,1]))
        X²+X
        """
        if len(self.lcoef)==1:
            return f"+{self.lcoef[0]}"
        else:
            if self.lcoef[0]==0:
                res=""
            else:
                res="+1"
        for k,c in enumerate(self.lcoef[1:]):
            if c==1:
                res="+X"+strExp(k+1)+res
        return res[1:]
    def __repr__(self):
        """
        """
##        s=""
##        for c in self.lcoef:
##            s+=c.__repr__()+","
##        s=s[:-1]
        #return f"PolF2({self.lcoef})"
        return f"PolF2(0b{int(self):b})"

    def degre(self):
        """
        >>> PolF2(0b100011).degre()
        5
        """
        return len(self.lcoef)-1
    def sommeCoef(self):
        """
        >>> PolF2(0b100011).sommeCoef()
        3
        """
        s=0
        for c in self.lcoef:
            if c==1:s+=1
        return s
    def distanceHamming(self,other):
        """
        >>> PolF2(0b100011).distanceHamming(PolF2(0b1100011))
        1
        """
        return (self+other).sommeCoef()

    def __add__(self,other):
        """
        >>> PolF2(0b100011)+PolF2(0b1100011)
        PolF2(0b1000000)
        >>> print(PolF2(0b1100011)+ PolF2(0b100011))
        X⁶
        >>> PolF2([0, 0, 1])+PolF2([1,1])
        PolF2(0b111)
        """
        pother=PolF2(other)
        resl=[]
        for c,cc in zip(self.lcoef,pother.lcoef):
            resl.append((c+cc)%2)
        if self.degre()>pother.degre():
            resl=resl+self.lcoef[pother.degre()+1:]
        elif self.degre()<pother.degre():
            resl=resl+pother.lcoef[self.degre()+1:]
        return PolF2(resl)
    def monome(k):
        """ X**k
        >>> print(PolF2.monome(5)+PolF2.monome(4)+PolF2.monome(1)+PolF2.monome(0))
        X⁵+X⁴+X+1
        """
        return PolF2(2**(k))

    def __mul__(self,other):
        """
        >>> print(PolF2.monome(2)*PolF2.monome(1))
        X³
        >>> PolF2(0b1100011)*PolF2(0b100011)
        PolF2(0b110011000101)
        >>> print(PolF2([0,0, 1])*PolF2([1, 1]))
        X³+X²
        """
        pother=PolF2(other)
        res=PolF2(0)
        for k,c in enumerate(pother.lcoef):
            if c==1:#res+=X^k*self
                res+=PolF2([0]*k+self.lcoef)
        return res

    def estNul(self):
        return self.degre()==0 and self.lcoef[0]==0

    def __eq__(self,other):
        """
        >>> PolF2.monome(7)+PolF2.monome(3)+PolF2.monome(1)==0
        False
        """
        if isinstance(other,int) :
            return self.degre()==0 and self.lcoef[0]==other

        return (self-other).estNul()
    def __neg__(self):
        """
        """
        return PolF2(self)
    def __sub__(self,other):
        """
        >>> PolF2(0b100011)-PolF2(0b100011)==0
        True
        """
        return self+(-other)
    def __mod__(self,other):
        """
        >>> PolF2(0b11000101)%PolF2(0b11000)
        PolF2(0b101)
        """
        Ptmp,Pquot=PolF2(self),PolF2(0)
        while Ptmp.degre()>=other.degre():
            Xq=PolF2.monome(Ptmp.degre()-other.degre())
            Pquot= Pquot +Xq
            Ptmp =Ptmp - other*Xq
        return Ptmp
    def __floordiv__(self,other):
        """
        >>> PolF2(0b11000101)//PolF2(0b11000)
        PolF2(0b1000)
        """
        Ptmp,Pquot=PolF2(self),PolF2(0)
        while Ptmp.degre()>=other.degre():
            Xq=PolF2.monome(Ptmp.degre()-other.degre())
            Pquot= Pquot +Xq
            Ptmp =Ptmp - other*Xq
        return Pquot

    def __int__(self):
        """
        >>> int(PolF2([1, 0, 1]))
        5
        """
        res=0
        for c in reversed(self.lcoef):
            res=res*2+c
        return res
    def __xor__(self, other):
        """
        Opérateur de XOR (^) entre deux polynômes dans F2.
        """
        if isinstance(other, PolF2):
            result = []
            for c1, c2 in zip(self.lcoef, other.lcoef):
                result.append(c1 ^ c2)
            # Si l'un des polynômes a un degré plus grand, ajoutez les coefficients restants
            if len(self.lcoef) > len(other.lcoef):
                result += self.lcoef[len(other.lcoef):]
            elif len(other.lcoef) > len(self.lcoef):
                result += other.lcoef[len(self.lcoef):]
            return PolF2(result)
        else:
            raise TypeError("Impossible de faire un XOR avec un type différent de PolF2")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    p=PolF2(0b100011)+PolF2(0b1100011)
    print(f"({PolF2(0b100011)})+({PolF2(0b1100011)})={PolF2(0b100011)+PolF2(0b1100011)} : {PolF2(0b100011)+PolF2(0b1100011)==PolF2(0b1000000)}")
    print(f"({PolF2(0b100001)})*({PolF2(0b1100011)})={PolF2(0b100001)*PolF2(0b1100011)}")
    print(f"({PolF2(0b1100011)})-({PolF2(0b1000011)})={PolF2(0b1100011)-PolF2(0b1000011)}")
    print(f"({PolF2(0b100001)})*({PolF2(0b0001010)})+({PolF2(0b0000011)})={PolF2(0b100001)*PolF2(0b0001010)+PolF2(0b0000011)}")
    print(f"({PolF2(0b1100011)})//({PolF2(0b101)})={PolF2(0b1100011)//PolF2(0b101)}")
    print(f"({PolF2(0b1100011)})%({PolF2(0b101)})={PolF2(0b100011)%PolF2(0b101)}")
    print(f"({PolF2(0b1100011)})=({PolF2(0b1100011)//PolF2(0b101)})*({PolF2(0b101)})+({PolF2(0b1100011)%PolF2(0b101)})")
    print(f"({PolF2(0b100011)})=({PolF2(0b100011)//PolF2(0b1001)})*({PolF2(0b1001)})+({PolF2(0b100011)%PolF2(0b1001)})")
    Ps=PolF2(0b11011011)
    Pg=PolF2(0b1011)
    Xr=PolF2.monome(3)
    print(f"Pour envoyer Ps={Ps=}")
    print(f"         avec {Pg=}={Pg}")
    print(f"Ps*Xr={Ps*Xr}=({(Ps*Xr)//Pg})*({Pg})+{(Ps*Xr)%Pg}")
    Pc=Ps*Xr+(Ps*Xr)%Pg
    print(f"On envoie donc Pc={Pc} avec {Pc=}")
    print(f"A la réception on vérifie : Pc%Pg={Pc%Pg} : ce message est donc valide")
    Pcp=Pc+PolF2.monome(5)

    print(f"Si on avait reçu le message erroné Pcp={Pcp} avec {Pcp=}")
    print(f"Pcp%Pg={Pcp%Pg} : ce message est donc erroné")
    import doctest
    doctest.testmod()
