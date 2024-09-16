from math import log
from random import randint
from arithmetiqueDansZ import ElementDeZnZ
import matplotlib.pyplot as plt
class LBinaire603(list):
    # Liste d'octets adapter au cours de cryptographie.
    #On passe facilement dun texte/image ou autre à un LBinaire603 et vice versa
    lchr=[chr(k) for k in range(256)] #List des 256 caractères imprimables
    for k in list(range(32))+list(range(0x7f,0xa1))+[0xad]:  lchr[k]=chr(k+256)
    #dict pour transformer un caractère en octet
    dbin=dict()
    for k in range(256):
        dbin[lchr[k]]=k  #Dictionnaire faisant correspondre un caractère à un octet
    #Le mieux est d'éviter les caractères suivants dans les fichiers à traiter
    dbin['’']=dbin["'"] ; dbin['\n']=13 ; dbin['œ']=dbin['æ'] ; dbin['—']=dbin['-'] ; dbin['…']=dbin['.'];

    def __init__(self,param=[]):
        """lbin est une liste ne contenant que :
            des entiers de [0..255] qui sont donc assumés comme des octets"
        ou bien une liste de ElementDeZnZ(..,256)
        lbin peut aussi être une chaine de caractère
        >>> LBinaire603([ElementDeZnZ(2,256),3])
        LBinaire603([ 0x02, 0x03])
        >>> LBinaire603("Trop tôt !")
        LBinaire603([ 0x54, 0x72, 0x6f, 0x70, 0x20, 0x74, 0xf4, 0x74, 0x20, 0x21])
        """
        if isinstance(param,str):
            #bc=param.encode('ascii', 'ignore') #byte
            #super().__init__([b for b in param.encode('ascii', 'ignore')])
            lb=[]
            for k,c in enumerate(param):
                if c in LBinaire603.dbin:
                    lb.append(LBinaire603.dbin[c])
                else:
                    lb.append(LBinaire603.dbin[' '])
                    print(f"{c=}:{ascii(c)}",end=' | ')
            super().__init__(lb)
            #super().__init__( [LBinaire603.dbin[c] for c in chaine] )
        else:
            lb=[]
            for b in param:
                assert LBinaire603.estOctet(b),"Les éléments d'un LBinaire603 doivent convertible en octets"
                lb.append(int(b))
            super().__init__(lb )
    def toString(self):
        """
        >>> LBinaire603("Trop tôt !").toString()
        'Trop tôt !'
        """
        ch=""
        for b in self:
                if b==13:
                     ch+="\n"
                else:
                    ch+=LBinaire603.lchr[b]
        return ch
    def __hash__(self):
        res=len(self)
        for b in self[:10]:
            res=256*res+b
        return res
    def sauvegardeDansFichier(self,nomFic,verbose=False):
        "Enregistre dans un fichier nommé nomFic"
        if verbose:print(f"lecture du fichier :{nomFic}")

        if nomFic[-4:].upper()==".TXT":
            with open(nomFic,"wt") as f:
                    f.write(self.toString())
        else:
            with open(nomFic,"wb") as f:
                    for b in self:
                        f.write(bytes([b]))

    def bin603DepuisFichier(nomFic,verbose=False):
        """renvoie un LBinaire603 d'après les données d'un fichier
        #>>> b1=LBinaire603.exBin603(taille=10,num=5)
        #>>> b1.sauvegardeDansFichier("MonBin.bin")
        #>>> b2=LBinaire603.bin603DepuisFichier("MonBin.bin")
        #>>> print(b2)
        # 10 octets :00ff00ff00ff00ff00ff
        #>>> lb=LBinaire603.bin603DepuisFichier("Les Miserables.TXT")
        """
        if verbose:print(f"lecture du fichier :{nomFic}")

        if nomFic[-4:].upper()==".TXT":
            with open(nomFic, 'r') as f:
                txt = f.read()
            return LBinaire603(txt)
        else:
            with open(nomFic,"rb") as f:
                data = f.read()
                if verbose:print(f"data est de type : {type(data)}")
                b=LBinaire603(data)
                if verbose:print(f"data : {b}")
            return b

    def exBin603(taille=1000,num=0):
        """Renvoie une instance Exemples de cette classe avec pour num :
        0: 255 fois 255 puis 254 fois 254 etc...
        1: un octet de chaque
        2: octets aléatoires
        3: 254 13 puis 255 14 puis 254 13 puis 255 14 ...
        4: 254 13 puis 255 14 puis 256 15 répétés
        5: et plus: 1000 fois un octet sur deux à 255
        """
        if num==0:
            data=[]
            for i in range(255,0,-1):
                data+=[i]*i
        elif num==1:
            data=[k for k in range(256)]
        elif num==2:
            data=[randint(0,255) for k in range(256)]
        elif num==3:
            data=[13]*254+[14]*255
        elif num==4:
            data=[13]*254+[14]*255+[15]*256
        else:
            data=[(k%2)*255 for k in range(256)]
        while len(data)<taille:
            data+=data
        return LBinaire603(data[:taille])

    def estOctet(val):
        """Renvoie true si val est un entier et si il se trouve dans [0..255]
        >>> LBinaire603.estOctet(255) and not(LBinaire603.estOctet(256))
        True
        >>> not(LBinaire603.estOctet(-1))and not(LBinaire603.estOctet("coucou")) and not(LBinaire603.estOctet([128,12]))
        True
        """
        res=False
        if isinstance(val, ElementDeZnZ) and val.n==256:
            res=True

        elif isinstance(val,int) and val>=0 and val <=255:
            res=True

        return res

    def ajouteOctet(self,data):
        """Ajoute un octet ou une liste d'octets tout en vérifiant la validité des données
        >>> a=LBinaire603([1,2,3,4]); a.ajouteOctet(10); a
        LBinaire603([ 0x01, 0x02, 0x03, 0x04, 0x0a])
        >>> a.ajouteOctet([11,12]);a
        LBinaire603([ 0x01, 0x02, 0x03, 0x04, 0x0a, 0x0b, 0x0c])
        """
        if isinstance(data,list):
            for oc in data:
                assert LBinaire603.estOctet(oc)
                self+=[oc]
        else:
            assert LBinaire603.estOctet(data)
            self+=[data]
    def ajouteMot64Bits(self,mot):
        """Ajoute un mot entier de 64bits
        >>> lb=LBinaire603([1,2,3,4]); lb.ajouteMot64Bits(65537);lb.ajouteMot64Bits(0x56789abc56789abc); lb
        LBinaire603([ 0x01, 0x02, 0x03, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x01, 0x56, 0x78, 0x9a, 0xbc, 0x56, 0x78, 0x9a, 0xbc])
        """
        if isinstance(mot,ElementDeZnZ):mot=mot.rep
        assert isinstance(mot,int) and mot>=0 and mot<0x10000000000000000,"Erreur mot de 32 bits exigé"
        val=mot
        l=[]
        for _ in range(8):
            l=[val%256]+l
            val//=256
        self+=l
    def ajouteMot32Bits(self,mot):
        """Ajoute un mot entier de 32bits
        >>> lb=LBinaire603([1,2,3,4]); lb.ajouteMot32Bits(65537);lb.ajouteMot32Bits(0x56789abc); lb
        LBinaire603([ 0x01, 0x02, 0x03, 0x04, 0x00, 0x01, 0x00, 0x01, 0x56, 0x78, 0x9a, 0xbc])
        """
        if isinstance(mot,ElementDeZnZ):mot=mot.rep
        assert isinstance(mot,int) and mot>=0 and mot<4294967296,"Erreur mot de 32 bits exigé"
        div=256
        val=mot
        l=[]
        for _ in range(4):
            l=[val%256]+l
            val//=256
        self+=l

    def lisOctet(self,pos):
        """Lis un octet et incrémente pos
            Utilisation val,pos=monBin.lisOctet(pos) comme suit
            >>> a,pos = LBinaire603.exBin603(10,1) ,5

            >>> val,pos = a.lisOctet(5)

            >>> val,pos
            (5, 6)
            """
        return self[pos],pos+1
    def lisMot32Bits(self,pos):
        """Lis un mot de 32bits et incrémente pos de 4
            Complète éventuellement par des 0
            >>> val,pos = LBinaire603([1,2,3,4 , 0,1,0,0 , 0,1]).lisMot32Bits(4)

            >>> val,pos
            (65536, 8)
            >>> LBinaire603([0xab,0xcd,0xab,0xcd,0xab,0xcd,0xab,0xcd]).lisMot32Bits(4)
            (2882382797, 8)
            """
        l=self[pos:pos+4]
        if len(l)<4:l+=[0]*(4-len(l))
        return l[3]+256*(l[2]+256*(l[1]+256*l[0])),pos+4
    def lisMot64Bits(self,pos):
        """Lis un mot de 64bits et incrémente pos de 8
            Complète éventuellement par des 0
            >>> LBinaire603([1,2,3,4 , 0,0,0,0 , 0,1,0,0]).lisMot64Bits(4)
            (65536, 12)
            >>> hex(LBinaire603([0xab,0xcd,0xab,0xcd,0xab,0xcd,0xab,0xcd,0xab,0xcd,0xab,0xcd]).lisMot64Bits(4)[0])
            '0xabcdabcdabcdabcd'
            """
        l=self[pos:pos+8]
        if len(l)<8:l+=[0]*(8-len(l))
        res=0
        for v in l:
            res=(res<<8)+v
        return res,pos+8
    def __str__(self):
        """Renvoie une chaine de caractère permettant de visualiser LBinaire603 self
        >>> str(LBinaire603([12,128]))
        '2 octets : 0c80'
        """
        s=f"{len(self)} octets : "

        def octetStr(oc):
            """
            >>> octetStr(12)
            0x0c
            >>> octetStr(ElementDeZnZ(17,256))
            0x11

            """

            if isinstance(oc,ElementDeZnZ):
                val=oc.rep
            else:
                val=oc
            return f"{val:02x}"

        if len(self)<=150 :
            for oc in self:
                s+=octetStr(oc)
        else:
            for oc in self[:100]:
                s+=" "+octetStr(oc)
            s+="........"
            for oc in self[-50:-1]:
                s+=" "+octetStr(oc)
        return s
    def __repr__(self):
        """Renvoie une chaine de caractère représentant TOUTES les données du LBinaire603 self
        sous la forme d'un appel à son constructeur ex: LBinaire603([ 0x57, 0x26, 0xfd]) """
        s="LBinaire603(["
        for oc in self:
            if isinstance(oc, ElementDeZnZ):
                s+=" "+oc.__repr__()+","
            else:
                s+=" "+f"0x{oc:02x}," # https://docs.python.org/fr/3/library/string.html
        return s[:-1]+ "])"
    def __eq__(self,other):
        """Renvoie True lorsque les octets sont égaux deux à deux
        >>> LBinaire603([ 0xcb, 0xba])==LBinaire603([ 0xcb, 0xba])
        True
        >>> LBinaire603([ ElementDeZnZ(1,256), ElementDeZnZ(2,256)])==LBinaire603([1,2])
        True
        >>> LBinaire603([ 0xcb, 0xba])==LBinaire603([ 0xcb])
        False
        >>> LBinaire603([ 0xcb, 0xba])==LBinaire603([ 0xcb, 0xbb])
        False
        """
        #todo:  voir le super pour comparé les références
        if len(self)!=len(other): return False
        k,n = 0, len(self)
        res= True
        while res and k<n:
            res= (self[k]==other[k])
            k+=1
        return res



    def nbOctets(val):
        """Renvoie le nb d'octets nécessaire pour coder l'entier val
        >>> LBinaire603.nbOctets(12)
        1
        >>> LBinaire603.nbOctets(0)
        1
        >>> LBinaire603.nbOctets(110000)
        3
        """
        if val==0:return 1
        return  int(log(val,256)+1)
    def ajouteLongueValeur(self,val):
        """Ajoute une valeur entière de taille qulconque de telle façon qu'elle
        puisse être récupérable par lisLongueValeur"""
        nbo=LBinaire603.nbOctets(val)
        self.ajouteOctet(nbo) #Nb d 'octets de la longueur du fichier
        l=val
        for k in range(nbo):
            self.ajouteOctet(l%256)
            l=l//256
    def lisLongueValeur(self,pos):
        """Renvoie tout ce qu'il faut pour enregistrer/ajouter une valeur entière
        de taille qulconque"à la position pos
        Renvoie cette valeur et la nouvelle valeur de pos
        >>> monBin=LBinaire603([12,13])
        >>> monBin.ajouteOctet(15)
        >>> monBin.ajouteLongueValeur(1000)
        >>> monBin.ajouteLongueValeur(100000)
        >>> pos=2
        >>> v0,pos=monBin.lisOctet(pos)
        >>> v1,pos=monBin.lisLongueValeur(pos)
        >>> v2,pos=monBin.lisLongueValeur(pos)
        >>> v0,v1,v2
        (15, 1000, 100000)
        """
        nbo=self[pos]
        pos+=1
        val=0
        for k in range(nbo):
            val+=self[pos]*256**k
            pos+=1
        return val,pos

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    lb=LBinaire603([1,2,3,3,3,3,4,8,8,128,253,253,253,253,253,253,254,254,254,255])
    lb=LBinaire603.bin603DepuisFichier("Germinal.txt")
    print(lb)