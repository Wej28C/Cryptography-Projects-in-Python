
from CodeurCA import CodeurCA

def bit(mot, indice, taille):
    """
    >>> bit(0b1010, 2, 4)
    0
    >>> bit(0b1010, 3, 4)
    1
    """
    return (mot >> (taille - indice)) & 1

def left(mot, taille):
    """
    >>> bin(left(0b11000011, 8))
    '0b1100'
    """
    return (mot >> int(taille / 2))

def right(mot, taille):
    """
    >>> right(0b11000011, 8)
    3
    """
    taille_masque = int(taille / 2)
    masque = 0
    for i in range(0, taille_masque):
        masque = (masque << 1) + 1
    return mot & masque

def leftShift(mot, taille):
    """
    >>> leftShift(0b100001, 6)
    3
    >>> bin(leftShift(0b010011, 6))
    '0b100110'
    """
    masque = 0
    for i in range(0, taille):
        masque = (masque << 1) + 1
    return ((mot << 1) + bit(mot, 1, taille)) & masque

def leftShiftIt(mot, taille, shift):
    """
    >>> bin(leftShiftIt(0b100001, 6, 3))
    '0b1100'
    """
    result = mot
    for i in range(0, shift):
        result = leftShift(result, taille)
    return result

def mergeLeftRight(left, right, tailleLeft):
    """
    >>> bin(mergeLeftRight(0b1100, 0b0011, 4))
    '0b11000011'
    """
    return (left << tailleLeft) + right

def bitPartie(mot, taille, indiceDebut, indiceFin):
    """
    >>> bin(bitPartie(0b011000010001011110111010100001100110010100100111, 48, 19, 24))
    '0b111010'
    """
    result = 0
    for i in range(indiceDebut, indiceFin + 1):
        result = (result << 1) + bit(mot, i, taille)
    return result

class FBij64BitsDES(CodeurCA):

    tPI = [58, 50, 42, 34, 26, 18, 10, 2,60, 52, 44, 36, 28, 20, 12, 4,62,
    54, 46, 38, 30, 22, 14, 6,64, 56, 48, 40, 32, 24, 16, 8,57, 49, 41, 33,
    25, 17, 9, 1,59, 51, 43, 35, 27, 19, 11, 3,61, 53, 45, 37, 29, 21, 13,
    5,63, 55, 47, 39, 31, 23, 15, 7]

    tPIm1=[40, 8, 48, 16, 56, 24, 64, 32,39, 7, 47, 15, 55, 23, 63, 31,38, 6,
    46, 14, 54, 22, 62, 30,37, 5, 45, 13, 53, 21, 61, 29,36, 4, 44, 12, 52,
    20, 60, 28,35, 3, 43, 11, 51, 19, 59, 27,34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25]

    tableauDeveloppementE = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

    tableauDeveloppementP = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

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

    tableauPermutationClef=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]

    numberOfLeftShiftsClef=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

    tableauPermutationClef1 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]

    def permutation(self, mot):
        """
        >>> bin(FBij64BitsDES(2).permutation(0b0000000100100011010001010110011110001001101010111100110111101111))
        '0b1100110000000000110011001111111111110000101010101111000010101010'
        """
        result = 0
        for x in self.tPI:
            result = (result << 1) + bit(mot, x, 64)
        return result

    def permutationInv(self, mot):
        """
        >>> FBij64BitsDES(2).permutationInv(0b1100110000000000110011001111111111110000101010101111000010101010)
        81985529216486895
        """
        result = 0
        for x in self.tPIm1:
            result = (result << 1) + bit(mot, x, 64)
        return result

    def developpementE(self, mot):
        """
        >>> FBij64BitsDES(2).developpementE(0b11110000101010101111000010101010)
        134232046966101
        """
        result = 0
        for x in self.tableauDeveloppementE:
            result = (result << 1) + bit(mot, x, 32)
        return result

    def developpementP(self, mot):
        """
        >>> FBij64BitsDES(2).developpementP(0b01011100100000101011010110010111)
        592095675
        """
        result = 0
        for x in self.tableauDeveloppementP:
            result = (result << 1) + bit(mot, x, 32)
        return result

    def developpementClef(self, clef):
        """
        >>> bin(FBij64BitsDES(2).developpementClef(0b0001001100110100010101110111100110011011101111001101111111110001))
        '0b11110000110011001010101011110101010101100110011110001111'
        """
        result = 0
        for x in self.tableauPermutationClef:
            result = (result << 1) + bit(clef, x, 64)
        return result

    def sBox(self, mot):
        """
        >>> FBij64BitsDES(2).sBox(0b011000010001011110111010100001100110010100100111)
        1552070039
        """
        result = 0

        for i in range(0, 8):
            newMot = bitPartie(mot, 48, i*6 + 1, (i+1)*6)
            result = (result << 4) + self.sBoxI(i, newMot)

        return result

    def sBoxI(self, idBox, mot):
        """
        >>> FBij64BitsDES(2).sBoxI(0, 0b011000)
        5
        """
        ligne = (bit(mot, 1, 6) << 1) + bit(mot, 6, 6)
        colone = (bit(mot, 2, 6) << 3) + (bit(mot, 3, 6) << 2) + (bit(mot, 4, 6) << 1) + bit(mot, 5, 6)
        return self.SBOX[idBox][ligne][colone]

    def f(self, clef, mot):
        """
        >>> FBij64BitsDES(2).f(59461212889569, 4278190335)
        2744379512
        >>> FBij64BitsDES(2).f(0b000110110000001011101111111111000111000001110010, 0b11110000101010101111000010101010)
        592095675
        """
        er = self.developpementE(mot)
        m = er ^ clef

        c = self.sBox(m)

        return self.developpementP(c)

    def __call__(self, mot):
        """
        >>> FBij64BitsDES(0b0001001100110100010101110111100110011011101111001101111111110001)(0x0123456789ABCDEF)
        9648983453391827973
        >>> FBij64BitsDES(0x0e329232ea6d0d73)(0x8787878787878787)
        0
        >>> hex(FBij64BitsDES(0x123556789ABDDEF0)(0x0123456789ABCDEF))
        '0x85e813540f0ab405'
        """
        motPerm = self.permutation(mot)
        lclefs = self.lclefs(self.k)

        l = left(motPerm, 64)
        r = right(motPerm, 64)

        for i in range(0, 16):
            l, r = r, l ^ self.f(lclefs[i], r)

        return self.permutationInv(mergeLeftRight(r, l, 32))

    def valInv(self, motc):
        """
        >>> FBij64BitsDES(0b0001001100110100010101110111100110011011101111001101111111110001).valInv(9648983453391827973)
        81985529216486895
        >>> hex(FBij64BitsDES(0x0e329232ea6d0d73).valInv(0x0000000000000000))
        '0x8787878787878787'
        >>> hex(FBij64BitsDES(0x123556789ABDDEF0).valInv(0x85e813540f0ab405))
        '0x0123456789abcdef'
        """
        motInv = self.permutation(mot)
        l = left(motInv, 64)
        r = right(motInv, 64)
        lclefs = self.lclefs(self.k)

        for i in range(15, -1, -1):
            r, l = l, r ^ self.f(lclefs[i], l)

        return mergeLeftRight(l, r, 32)


    def lclefsCD(self, clef):
        """
        >>> FBij64BitsDES(2).lclefsCD(0b11110000110011001010101011110101010101100110011110001111)
        ([252496559, 236557663, 204679871, 13413119, 53652476, 214609904, 53133251, 212533004, 44825651, 89651302, 90169753, 92243557, 100538773, 133719637, 266443093, 260466007, 252496559], [89548687, 179097374, 89759293, 90601717, 93971413, 107450197, 161365333, 108590422, 165926233, 63417011, 253668044, 209365811, 32156879, 128627516, 246074609, 178992071, 89548687])
        """
        c0 = left(clef, 56)
        d0 = right(clef, 56)
        lc = list(range(17))
        ld = list(range(17))
        lc[0] = c0
        ld[0] = d0

        for i in range(1, 17):
            lc[i] = leftShiftIt(lc[i-1], 28, self.numberOfLeftShiftsClef[i-1])
            ld[i] = leftShiftIt(ld[i-1], 28, self.numberOfLeftShiftsClef[i-1])
        return lc, ld

    def clefPermutation1(self, c, d):
        """
        >>> FBij64BitsDES(2).clefPermutation1(0b1110000110011001010101011111, 0b1010101011001100111100011110)
        29699430183026
        """
        mot = mergeLeftRight(c, d, 28)
        result = 0
        for x in self.tableauPermutationClef1:
            result = (result << 1) + bit(mot, x, 56)
        return result

    def lclefs(self, clef):
        """
        >>> FBij64BitsDES(2).lclefs(0x133457799BBCDFF1)
        [29699430183026, 133791886330341, 94543139753881, 126090959598877, 137353186988968, 109561366215471, 260054766196924, 272173063289851, 247235160696705, 195658438559311, 36695460205446, 129132311898089, 166875887221313, 104744453596986, 210631860764426, 223465186400245]
        """
        clef = self.developpementClef(clef)
        lc, ld = self.lclefsCD(clef)
        lresult = list(range(16))
        for i in range(0, 16):
            lresult[i] = self.clefPermutation1(lc[i + 1], ld[i + 1])
        return lresult

    def __init__(self, k):
        self.k=k

    def __str__(self):
        return f"FBij64BitsDES avec k={self.k}"

    def __repr__(self):
        return f"FBij64BitsDES({self.k})"

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    chiffreur = FBij64BitsDES(2)
