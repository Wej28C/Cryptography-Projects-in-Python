#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:28:07 2024

@author: beatrice
"""

from LBinaire603 import LBinaire603

class DES:
    def __init__(self, key: LBinaire603):
        self.key = key
        self.round_keys = self.generate_round_keys(key)

    @staticmethod
    def initial_permutation(block: LBinaire603) -> LBinaire603:
        # Tableau de permutation initiale
        ip_table = [
            58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7
        ]
        return block.permute(ip_table)

    @staticmethod
    def final_permutation(block: LBinaire603) -> LBinaire603:
        # Tableau de permutation finale
        fp_table = [
            40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25
        ]
        return block.permute(fp_table)

    @staticmethod
    def expansion_permutation(block: LBinaire603) -> LBinaire603:
        # Tableau de permutation d'expansion
        ep_table = [
            32, 1, 2, 3, 4, 5, 4, 5,
            6, 7, 8, 9, 8, 9, 10, 11,
            12, 13, 12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21, 20, 21,
            22, 23, 24, 25, 24, 25, 26, 27,
            28, 29, 28, 29, 30, 31, 32, 1
        ]
        return block.permute(ep_table)

    @staticmethod
    def permutation(block: LBinaire603, table: list) -> LBinaire603:
        # Permutation d'un bloc selon une table donnée
        return block.permute(table)

    @staticmethod
    def substitution(box: list, block: LBinaire603) -> LBinaire603:
        # Substitution en utilisant les boîtes de substitution (S-boxes)
        result = LBinaire603([])
        for i in range(8):
            row = block[i * 6] * 2 + block[i * 6 + 5]
            col = int(block[i * 6 + 1:i * 6 + 5], 2)
            val = box[i][row * 16 + col]
            result += LBinaire603(format(val, '04b'))
        return result

    @staticmethod
    def generate_round_keys(key: LBinaire603) -> list:
        # Génération des clés de tour
        round_keys = []
        # Implémentez ici la génération des clés de tour
        return round_keys

    def feistel_round(self, block: LBinaire603, round_key: LBinaire603) -> LBinaire603:
        # Implémentez ici un tour de la structure de Feistel
        return block

    def encrypt_block(self, block: LBinaire603) -> LBinaire603:
        # Chiffrement d'un bloc
        block = self.initial_permutation(block)
        # Implémentez les 16 tours de Feistel avec les clés de tour
        for round_key in self.round_keys:
            block = self.feistel_round(block, round_key)
        block = self.final_permutation(block)
        return block

    def decrypt_block(self, block: LBinaire603) -> LBinaire603:
        # Déchiffrement d'un bloc
        block = self.initial_permutation(block)
        # Implémentez les 16 tours de Feistel avec les clés de tour inversées
        for round_key in reversed(self.round_keys):
            block = self.feistel_round(block, round_key)
        block = self.final_permutation(block)
        return block

    def encrypt(self, plaintext: LBinaire603) -> LBinaire603:
        # Chiffrement du texte
        ciphertext = LBinaire603([])
        for i in range(0, len(plaintext), 64):
            block = plaintext[i:i+64]
            ciphertext += self.encrypt_block(block)
        return ciphertext

    def decrypt(self, ciphertext: LBinaire603) -> LBinaire603:
        # Déchiffrement du texte
        plaintext = LBinaire603([])
        for i in range(0, len(ciphertext), 64):
            block = ciphertext[i:i+64]
            plaintext += self.decrypt_block(block)
        return plaintext


class TestDES:
    @staticmethod
    def test_encryption_decryption():
        key = LBinaire603([0, 1, 0, 1, 1, 0, 1, 0] * 8)  # Exemple de clé
        plaintext = LBinaire603("hello world")  # Message à chiffrer
        des = DES(key)

        # Chiffrement
        ciphertext = des.encrypt(plaintext)
        print("Cipher text:", ciphertext)

        # Déchiffrement
        decrypted_text = des.decrypt(ciphertext)
        print("Decrypted text:", decrypted_text)

        # Vérification
        assert plaintext == decrypted_text, "Erreur: Le texte déchiffré ne correspond pas au texte d'origine."
        print("Le chiffrement et le déchiffrement sont réussis.")

# Exécution des tests
if __name__ == "__main__":
    TestDES.test_encryption_decryption()
