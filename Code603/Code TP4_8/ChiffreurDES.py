from FBij64BitsDES import *
from LBinaire603 import LBinaire603
from CodeurCA import CodeurCA

tPI = [58, 50, 42, 34, 26, 18, 10, 2,60, 52, 44, 36, 28, 20, 12, 4,62, 54, 46, 38, 30, 22, 14, 6,64, 56, 48, 40, 32, 24, 16, 8,57, 49, 41, 33, 25, 17, 9, 1,59, 51, 43, 35, 27, 19, 11, 3,61, 53, 45, 37, 29, 21, 13, 5,63, 55, 47, 39, 31, 23, 15, 7]
tPIm1=[40, 8, 48, 16, 56, 24, 64, 32,39, 7, 47, 15, 55, 23, 63, 31,38, 6, 46, 14, 54, 22, 62, 30,37, 5, 45, 13, 53, 21, 61, 29,36, 4, 44, 12, 52, 20, 60, 28,35, 3, 43, 11, 51, 19, 59, 27,34, 2, 42, 10, 50, 18, 58, 26,33, 1, 41, 9, 49, 17, 57, 25]
SBOX = [
# Box-1
[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],
[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],
[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],
[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],
[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],
[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]]

F_PBox =   [16, 7, 20, 21, 29, 12, 28, 17,1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9,19, 13, 30, 6, 22, 11, 4, 25 ]
key_PBox = [14,17, 11,24, 1,5,3,28, 15, 6,21, 10,23,19, 12, 4,26,8, 16, 7, 27,20,13,2,41,52, 31,37,47, 55,30,40, 51,45,33, 48,44,49, 39,56,34,53, 46,42, 50,36,29, 32]

tPC1=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
tPC2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
tv=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

tEBox = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
tP = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

def bit(mot, indice, nbBits):
    """renvoie le bit à l'indice donné
    >>> bit(12,1,4)
    1
    """
    return (mot>>(nbBits-indice))&1


def intImage(mot,tPermutation,nbBits):
    """
    Renvoie l'image d'un entier par une permutation
    >>> intImage(36,[2,4,6,1,3,5],6)
    20
    """
    # nbBits=len(tPermutation)
    # tailleMot=mot.bit_length()
    # if(tailleMot>56):
    #     tailleMot=64
    # else:
    #     tailleMot=56


    # if(tailleMot>len(tPermutation)):
    #     nbBits=tailleMot

    res=0
    for indice in tPermutation:
        res = (res<<1) + bit(mot,indice,nbBits)
    return res



def liste16Cles(intKey,verbose=False):
    """
    Renvoie un tableau de 17 éléments mais seules les clés 1 à 17 sont initialisées
    >>> liste16Cles(0x123556789ABDDEF0)[16]
    223465186400245
    >>> liste16Cles(0x123556789ABDDEF0)[0]
    'Pas de valeur'"""
    lkeys=['Pas de valeur']*17
    ci,di= intImage(intKey,tPC1[:28],64),intImage(intKey,tPC1[28:],64)
    for i in range(1,17):
        # On applique une rotation circulaire de tv[i-1] bits à ci et di
        ci = ((ci << tv[i-1]) | (ci >> (28 - tv[i-1]))) & 0xFFFFFFF
        di = ((di << tv[i-1]) | (di >> (28 - tv[i-1]))) & 0xFFFFFFF
        # On calcule Ki
        ciDi = (ci<<28) + di
        ki=0
        for indice in tPC2:
            ki = ki<<1
            ki = ki + bit(ciDi,indice,56)
        lkeys[i]=ki
    return lkeys




def intSImage(mot6bits, sBoxNum):
    """ Image d'un mot de 6bits par la Sbox numéro sBoxNum
    >>> intSImage(24,0)
    5
    >>> intSImage(39, 7)
    7
    """
    iLigne=(bit(mot6bits,1,6) << 1)+ bit(mot6bits,6,6)
    iColonne=0
    for i in range(2,6):
        iColonne = (iColonne<<1)+ bit(mot6bits,i,6)
    return SBOX[sBoxNum][iLigne][iColonne]



def functionF(int32, key48bits):
    """ Image d'un mot de 32bits par la fonction f avec une clé de 48bits
    >>> functionF(0xff0000ff,0x36146478e1e1)
    2744379512
    """
    # Application de la boîte d'expansion E
    er = intImage(int32, tEBox, 32)
    # XOR avec la clé de 48 bits
    erx = er ^ key48bits
    # Application des S-Boxes
    res = 0
    for i in range(8):
        # Extraction de 6 bits pour la S-Box
        sixBits = (erx >> (6 * (7 - i))) & 0x3F
        row = ((sixBits & 0x20) >> 4) | (sixBits & 0x01)
        col = (sixBits & 0x1E) >> 1
        sboxValue = SBOX[i][row][col]
        res = (res << 4) | sboxValue
    # Application de la permutation P
    res = intImage(res, F_PBox, 32)
    return res


def intRound(bloc64bits, cle48bits):
    """ Application d'un round de feistel au mot avec la clé intcle
    >>> intRound(0x123556789ABDDEF0,0x123556789ABDDEF0)
    11150313377424277506
    """
    # Masque pour isoler la partie droite de 32 bits
    masque32 = 0xFFFFFFFF
    # Séparation du bloc en deux parties : gauche (L) et droite (R)
    L = bloc64bits >> 32
    R = bloc64bits & masque32

    # Application de la fonction f sur R avec la clé cle48bits
    f_R = functionF(R, cle48bits)

    # XOR de L avec le résultat de la fonction f et échange de L et R
    newR = L ^ f_R
    newL = R

    # Combinaison des deux moitiés pour former le nouveau bloc de 64 bits
    nouveauBloc = (newL << 32) | newR

    return nouveauBloc



class FBij64BitsDES(object):
    """Une classe abstraite de bijection sur des mots de 64 bits"""

    def __init__(self, cle, verbose=False):
        self.cle = cle
        self.verbose = verbose
        self.cles = liste16Cles(self.cle, self.verbose)  # Génère les 16 clés de tour

    def __repr__(self):
        return "FBij64BitsDES(" + hex(self.cle) + ")"

    def __call__(self, mot64bits):
        """
        >>> hex(FBij64BitsDES(0x0e329232ea6d0d73)(0x8787878787878787))
        '0x0'
        >>> hex(FBij64BitsDES(0x123556789ABDDEF0)(0x0123456789ABCDEF))
        '0x85e813540f0ab405'
        """
        # Permutation initiale
        mot_permute = intImage(mot64bits, tPI, 64)
        L, R = mot_permute >> 32, mot_permute & 0xFFFFFFFF

        # 16 rounds de Feistel
        for i in range(1, 17):
            L, R = R, L ^ functionF(R, self.cles[i])

        # Combinaison de R et L (Note: L et R sont inversés dans la dernière étape)
        mot_combine = (R << 32) | L

        # Permutation finale
        mot_final = intImage(mot_combine, tPIm1, 64)
        return mot_final

    def valInv(self, mot64bitsChiffre):
        """
        >>> hex(FBij64BitsDES(0x0e329232ea6d0d73).valInv(0x0000000000000000))
        '0x8787878787878787'
        >>> hex(FBij64BitsDES(0x123556789ABDDEF0).valInv(0x85e813540f0ab405))
        '0x123456789abcdef'
        """
        # Permutation initiale inverse
        mot_permute = intImage(mot64bitsChiffre, tPI, 64)
        L, R = mot_permute >> 32, mot_permute & 0xFFFFFFFF

        # 16 rounds de Feistel en ordre inverse
        for i in range(16, 0, -1):
            L, R = R, L ^ functionF(R, self.cles[i])

        # Combinaison de R et L (Note: L et R sont inversés dans la dernière étape)
        mot_combine = (R << 32) | L

        # Permutation finale inverse
        mot_final = intImage(mot_combine, tPIm1, 64)
        return mot_final

class ChiffreurDES(CodeurCA):
    def __init__(self ,cle=0x123556789ABDDEF0,verbose=False):
        self.cle=int(cle)
        self.f=FBij64BitsDES(cle,verbose=verbose)

    def __str__(self):
        return f"Chiffreur DES de clé {self.cle:08x}"
    def __repr__(self):
        return f"ChiffreurDES({self.cle=:08x})"

    def binCode(self,monBin):
        monBinC=LBinaire603([])
        #On doit mémoriser la longueur totale de la liste à chiffrer
        monBinC.ajouteLongueValeur(len(monBin))
        pos=0
        while pos<len(monBin):
            x,pos=monBin.lisMot64Bits(pos)
            monBinC.ajouteMot64Bits( self.f(x) )
        return monBinC

    def binDecode(self,monBinC):
        monBinD=LBinaire603([])
        longueur,pos=monBinC.lisLongueValeur(0)

        while pos<len(monBinC):
            y,pos=monBinC.lisMot64Bits(pos)
            monBinD.ajouteMot64Bits( self.f.valInv(y) )
        return LBinaire603(monBinD[:longueur])

    def demo():
        monBin=LBinaire603("Bonjour les amis !! Vous allez bien ?")
        monChiffreur=ChiffreurDES(0x123556789ABDDEF0)
        print(f"Chiffrement avec {monChiffreur} :")
        print("   Bin           :",monBin.toString())
        monBinC=monChiffreur.binCode(monBin)
        print("   Bin Chiffré   :",monBinC.toString())
        monBinD=monChiffreur.binDecode(monBinC)
        print("   Bin Déchiffré :",monBinD.toString())
        print("   monBinD (déchiffré) est égal à Monbin ?",monBinD==monBin)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(bin(12))
    test = intImage(12,[4,3,2,1],4)
    print(test)

    l=liste16Cles(0x123556789ABDDEF0)
    print(l) #pas le résultat voulu

    mot32=1147483647
    mot32res=functionF(mot32,0x80a0a2049838)
    print(mot32res)

    # test demo
    ChiffreurDES.demo()



    #F=FBij64BitsDES(0x0e329232ea6d0d73)
    #print(F)

    #test2=F(0x123556789ABDDEF0)
    #print(test2)

