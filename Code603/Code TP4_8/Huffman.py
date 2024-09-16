#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Wejdane
#
# Created:     28/02/2024
# Copyright:   (c) utilisateur 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from heapq import heapify, heappush, heappop
from collections import defaultdict
from typing import Dict
from CodeurCA import*

class NoeudHuffman:
    """Un noeud de l'arbre de Huffman"""

    def __init__(self, caractere=None, poids=None):
        self.caractere = caractere
        self.poids = poids
        self.gauche = None
        self.droite = None

    def __lt__(self, autre):
        return self.poids < autre.poids


class CompresseurHuffman(CodeurCA):
    """Implémentation du compresseur Huffman"""

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "CompresseurHuffman"

    def __repr__(self):
        return "CompresseurHuffman()"

    def construire_arbre_huffman(self, frequences: Dict[str, int]) -> NoeudHuffman:
        """Construit l'arbre de Huffman à partir d'un dictionnaire de fréquences."""
        file_priorite = [NoeudHuffman(caractere=char, poids=freq) for char, freq in frequences.items()]
        heapify(file_priorite)

        while len(file_priorite) > 1:
            gauche = heappop(file_priorite)
            droite = heappop(file_priorite)
            nouvel_arbre = NoeudHuffman(poids=gauche.poids + droite.poids)
            nouvel_arbre.gauche, nouvel_arbre.droite = gauche, droite
            heappush(file_priorite, nouvel_arbre)

        return file_priorite[0]

    def construire_codes_huffman(self, arbre: NoeudHuffman, code_actuel="", codes=None):
        """Construit les codes binaires associés à chaque caractère à partir de l'arbre de Huffman."""
        if codes is None:
            codes = {}

        if arbre.caractere is not None:
            codes[arbre.caractere] = code_actuel
        if arbre.gauche is not None:
            self.construire_codes_huffman(arbre.gauche, code_actuel + "0", codes)
        if arbre.droite is not None:
            self.construire_codes_huffman(arbre.droite, code_actuel + "1", codes)

        return codes

    def binCode(self, monBinD: LBinaire603) -> LBinaire603:
        """Compresses the input LBinaire603 using Huffman Coding."""
        frequences = defaultdict(int)

        # Calcul des fréquences des caractères dans la séquence d'entrée
        for char in monBinD:
            frequences[char] += 1
        print("Fréquences des caractères :", frequences)

        # Construction de l'arbre de Huffman
        arbre_huffman = self.construire_arbre_huffman(frequences)
        print("Arbre de Huffman :", arbre_huffman)

        # Construction des codes binaires associés à chaque caractère
        codes_huffman = self.construire_codes_huffman(arbre_huffman)
        print("Codes binaires de Huffman :", codes_huffman)

        # Création de la séquence binaire compressée
        sequence_compressée = LBinaire603()
        for char in monBinD:
            sequence_compressée += LBinaire603(list(map(int, codes_huffman[char])))
        print("Séquence binaire compressée :", sequence_compressée)
        return sequence_compressée

    def binDecode(self, monBinC: LBinaire603) -> LBinaire603:

        """Decompresses the input LBinaire603 using Huffman Coding."""
        if not hasattr(self, 'arbre_huffman'):
            raise ValueError("L'arbre de Huffman doit être construit avant la décompression.")

        sequence_originale = LBinaire603()
        noeud_actuel = self.arbre_huffman

        for bit in monBinC:
            if bit == 0:
                noeud_actuel = noeud_actuel.gauche
            else:
                noeud_actuel = noeud_actuel.droite

            if noeud_actuel.caractere is not None:
                sequence_originale += LBinaire603([noeud_actuel.caractere])
                noeud_actuel = self.arbre_huffman  # Retour à la racine de l'arbre

        return sequence_originale

if __name__ == "__main__":
    # Exemple d'utilisation avec le compresseur Huffman
    monCodeurHuffman = CompresseurHuffman()
    monBinHuffman = LBinaire603.exBin603(num=3, taille=25)
    print("Bin:", monBinHuffman)
    monBinHuffmanCr = monCodeurHuffman.binCode(monBinHuffman)
    print("Bin Codée:", monBinHuffmanCr)
    # TODO: Ajouter les étapes de décompression et de vérification
