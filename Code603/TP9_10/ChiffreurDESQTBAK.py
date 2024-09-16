#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Quentin
#
# Created:     11/01/2024
# Copyright:   (c) Quentin 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

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



def txtH(lbits):
    """Une string représentant le nombre en hexa avec tous ses chiffres
    >>> txtH([0,0,0,0,1,0,1,1,0,0,1,1,1])
    '0167'
    """
    # Concatène une chaine vide et la liste transformé en une chaine
    chaine_binaire = ''.join(map(str, lbits))
    #print(chaine_binaire)

    # Convertit la chaîne binaire en un entier en base 2
    valeur_decimal = int(chaine_binaire, 2)

    # Convertit l'entier en hexadécimal et retire le préfixe "0x" (les 2 premiers caractères) puis ajoute les les 0 au début si nécessaire
    chaine_hexa = hex(valeur_decimal)[2:]
    chaine_hexa = chaine_hexa.rjust((len(chaine_hexa) + 1) // 2 * 2, '0')

    return chaine_hexa



# Prend un int et une taille pour le nombre d'octets de sortie
def intToListBits(val,taille):
    """
    >>> intToListBits(13,taille=6)
    [0, 0, 1, 1, 0, 1]
    """

    # Récupère le binaire de val, enlève 0b devant et rajoute les 0 nécessaires
    representation_binaire = bin(val)[2:].rjust(taille, '0')

    # Convertit chaque binaire en entier et stocke le résultat dans une liste.
    lbits = [int(bit) for bit in representation_binaire]

    return lbits


# Convertit une liste de bits en un entier
def listBitsToInt(lbits):
    """
    >>> listBitsToInt([1,1,0,1])
    13
    """
    entier = int(''.join(map(str, lbits)), 2)

    return entier


# Renvoie l'image d'une liste de bits par une permutation
def lbImage(lbits,tPermutation):
    """
    >>> lbImage([1,0,1,0,1,0,1,0],[2,4,6,8,1,3,5,7])
    [0, 0, 0, 0, 1, 1, 1, 1]
    """
    image = [lbits[indice - 1] for indice in tPermutation]

    return image


# Retourne le bit présent à l indice passé en param du mot de nbBits
def bit(mot, indice, nbBits):
    """Renvoie le bit à la position indice du mot
    >>> bit(0b0001,3,4)
    0
    """
    #if indice < 1 or indice > 6:
    #    raise ValueError("Erreur : indice doit être compris entre 1 et 6 inclus.")

    return (mot >> (nbBits - indice)) & 1


# Prend un mot en paramètre et un type de permutation
# Renvoie une liste de bits permutée
def permutation(lbKey, tPermutation):
    """ testPermutation
    >>> permutation([0, 1, 1, 0, 1],[3, 1, 2, 5, 4])
    [1, 0, 1, 1, 0]
    """
    res = []
    for indice in tPermutation:
        res.append(lbKey[indice - 1])
    return res


# Retourne un entier représentant la valeur de la sBox "numeroSBox"
# pour la ligne et la colonne suivant cette méthode sur le Lbin6bits :
# bit1 concat bit6 donne la ligne, bit2 à 5 concat donne la colonne
def lbSImage(Lbin6bits, numeroSBox):
    """ test lbSImage
    >>> lbSImage(0b011000,0)
    5
    """

    ligne_Sbox = (bit(Lbin6bits, 1, 6) << 1) + bit(Lbin6bits, 6, 6)
    colonne_Sbox = 0
    for i in range(2, 6):
        colonne_Sbox = (colonne_Sbox << 1) + bit(Lbin6bits, i, 6)

    return SBOX[numeroSBox][ligne_Sbox][colonne_Sbox]



def liste16Cles(lbKey,verbose=False):
    """ Renvoie un tableau de 17 éléments mais seules les clés 1 à 17 sont initialisées
    >>> txtH(liste16Cles(intToListBits(0x123556789ABDDEF0,64))[16])
    'cb3d8b0e17f5'
    >>> liste16Cles(intToListBits(0x123556789ABDDEF0,64))[0]
    'Pas de valeur'
    """

    # Initialisation du tableau de clés
    cles = ['Pas de valeur'] + [None] * 16

    # Permutation initiale de la clé
    lbKeyPermute = (permutation(lbKey, tPC1))

    # Division de la clé en deux parties
    L0 = lbKeyPermute[:28]
    R0 = lbKeyPermute[28:]

    # Génération des clés 1 à 16
    for i in range(1, 17):
        # Calcul des rotations
        rotations = tv[i - 1]

        # Rotation de Ci et Di
        L0 = ((L0[rotations:] + L0[:rotations])[:28])
        R0 = ((R0[rotations:] + R0[:rotations])[:28])

        # Concaténation de Ci et Di
        CDi = L0 + R0

        # Permutation PC2
        cle_i = permutation(CDi, tPC2)
        cles[i] = cle_i

    return cles



def functionF(lb32, lbkey48bits):
    """ Image d'un mot de 32bits par la fonction f avec une clé de 48bits
    >>> txtH(functionF(intToListBits(0xff0000ff,32), intToListBits(0x36146478e1e1,48)))
    'a393e878'
    """
    er = permutation(lb32, tEBox)
    erx = listBitsToInt(er) ^ listBitsToInt(lbkey48bits)
    C = []

    for i in range(8,0,-1):

        # Prend les 6 derniers bit de erx et les supprime de erx
        b = erx & 0b111111
        erx = erx >> 6

        # Cbox récupère la valeur dans la Sbox associée puis l'ajoute dans le mot C
        Cbox = lbSImage(b, i - 1)
        C = intToListBits(Cbox, 4) + C

    # Permutation finale
    ffinal = permutation(C, tP)
    return ffinal


# Fonction qui prend deux listes de bits de même taille, fait le xor et retourne la liste
def xor(lbits1, lbits2, taille):
    """
    >>> xor([0,0,1,1,0,1,0,1],[0,1,1,1,0,1,0,1],8)
    [0, 1, 0, 0, 0, 0, 0, 0]
    """
    for i in range(0, taille):
        lbits1[i] = lbits1[i] ^ lbits2[i]

    return lbits1


def lbround(lbits,lbcle):
    """ Application d'un round au mot lbits avec la clé lbcle
    >>> txtH(lbround(intToListBits(0x0123456789ABCDEF,64),intToListBits(0x133457799BBCDFF1,64)))
    '9abddef09ba90002'
    """
    lbits = permutation(lbits, tPI)
    # Préparation pour Feistel
    L = lbits[:32]
    R = lbits[32:]

    lcles = liste16Cles(lbcle)
    #for i in range(0,17) : print(lcles[i])
    #Valide jusque ici

    for i in range(1, 17):
        #if(i == 1):
        #    print("cle 1 ", lcles[i])
        #    print("L avant ", L)
        #    print("R avant ", R)
        # Copie des parties gauche et droite avant le tour
        L_prev, R_prev = L.copy(), R.copy()

        # Application du tour de Feistel
        F_result = functionF(R, lcles[i])

        # XOR entre la partie gauche (L) et le résultat de la fonction F
        tmp = xor(L_prev, F_result, 32)

        # Échange des parties gauche et droite pour le prochain tour
        L, R = R, tmp

    # Reconstruction du mot après les 16 tours de Feistel
    lbits = L + R

    # Permutation inverse pour finir le processus
    lbits = permutation(lbits, tPIm1)

    return lbits
print(txtH(lbround(intToListBits(0x0123456789ABCDEF,64),intToListBits(0x133457799BBCDFF1,64))))


def main():
    pass

if __name__ == '__main__':
    import doctest
    main()
    doctest.testmod()
