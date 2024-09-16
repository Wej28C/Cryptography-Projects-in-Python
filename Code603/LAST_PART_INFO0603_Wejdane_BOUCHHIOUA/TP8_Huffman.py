#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      utilisateur
#
# Created:     28/02/2024
# Copyright:   (c) utilisateur 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from typing import List, Tuple, Dict
from heapq import heappush, heappop, heapify
from collections import defaultdict
from LBinaire603 import LBinaire603
from CodeurCA import*
class NoeudHuffman:
    def __init__(self, caractere=None, poids=0, gauche=None, droite=None):
        self.caractere = caractere
        self.poids = poids
        self.gauche = gauche
        self.droite = droite
    def __lt__(self, other):
        return self.poids < other.poids

class CompresseurHuffman(CodeurCA):
    @staticmethod
    def arbreDepuisListePonderee(liste_ponderee: List[Tuple[str, float]]) -> NoeudHuffman:
        """Construit un arbre de Huffman à partir d'une liste pondérée."""
        file_priorite = [NoeudHuffman(caractere=char, poids=freq) for char, freq in liste_ponderee]
        heapify(file_priorite)

        while len(file_priorite) > 1:
            gauche = heappop(file_priorite)
            droite = heappop(file_priorite)
            nouvel_arbre = NoeudHuffman(poids=gauche.poids + droite.poids)
            nouvel_arbre.gauche, nouvel_arbre.droite = gauche, droite
            heappush(file_priorite, nouvel_arbre)

        return file_priorite[0]

    @staticmethod
    def construire_codes_huffman(arbre: NoeudHuffman, code_actuel="", codes=None):
        if codes is None:
            codes = {}

        if arbre.caractere is not None:
            codes[arbre.caractere] = code_actuel
        if arbre.gauche is not None:
            CompresseurHuffman.construire_codes_huffman(arbre.gauche, code_actuel + "0", codes)
        if arbre.droite is not None:
            CompresseurHuffman.construire_codes_huffman(arbre.droite, code_actuel + "1", codes)

        return codes

    @staticmethod
    def dicoHuffmanDepuisArbre(arbre):
        """Renvoie les dictionnaires associant les étiquettes à leur codage d'Huffman."""
        codes_binaires = CompresseurHuffman.construire_codes_huffman(arbre)
        inverse_codes = {v: k for k, v in codes_binaires.items()}
        return codes_binaires, inverse_codes

    @staticmethod
    def binCode(monBinD: LBinaire603, arbre: NoeudHuffman) -> LBinaire603:
        """Compresse la séquence d'entrée en utilisant le codage Huffman."""
       # codes_binaires, _ = CompresseurHuffman.dicoHuffmanDepuisArbre(arbre)
        codes_binaires = CompresseurHuffman.construire_codes_huffman(arbre)

        print("Codes binaires:", codes_binaires)
        texte_compressé = LBinaire603()

        for caractere in monBinD:
            code = codes_binaires.get(caractere,'')
            texte_compressé += LBinaire603(code)


        return texte_compressé

    @staticmethod
    def binDecode(monBinC: LBinaire603, arbre: NoeudHuffman) -> LBinaire603:
        """Décompresse la séquence binaire en utilisant le codage Huffman."""
        texte_original = LBinaire603()
        actuel_noeud = arbre

        for bit in monBinC:
            if bit == "0":
                actuel_noeud = actuel_noeud.gauche
            else:
                actuel_noeud = actuel_noeud.droite

            if actuel_noeud.caractere is not None:
                texte_original += LBinaire603(actuel_noeud.caractere)
                actuel_noeud = arbre

        return texte_original

if __name__ == "__main__":
    # Exemple d'utilisation
    liste_ponderee = [("B", 0.3), ("L", 0.2), ("E", 0.2),
                      ("I", 0.1), ("A", 0.1), ("T", 0.1), ("S", 0.1), ("N", 0.1)]

    arbre_huffman = CompresseurHuffman.arbreDepuisListePonderee(liste_ponderee)
    dico_binaires, dico_caracteres = CompresseurHuffman.dicoHuffmanDepuisArbre(arbre_huffman)

    print("Codes binaires :", dico_binaires)
    print("Codes caractères :", dico_caracteres)

    texte_original = LBinaire603("BANANAZ")
    texte_compresse = CompresseurHuffman.binCode(texte_original, arbre_huffman)

    print("Texte original :", texte_original)
    print("Text compresse:", texte_compresse)
