#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      utilisateur
#
# Created:     22/12/2023
# Copyright:   (c) utilisateur 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import random
from FBijection8bitsCA import FBijection8bitsCA

class fBijParDecallage(FBijection8bitsCA):
    def __init__(self, shift):
        self.shift = shift

    def __repr__(self):
        return f"FBijParDecallage(shift={self.shift})"

    def __call__(self, octet):
        return (octet + self.shift) % 256

    def valInv(self, octetC):
        return (octetC - self.shift) % 256

def main():
    # Test sur une fonction affine
    f_affine = fBijParDecallage(5)
    f_affine.afficheGraphiquesDeDiffusionConfusion()

    # Test sur une bijection inventée
    f_inventee = fBijParDecallage(10)
    f_inventee.afficheGraphiquesDeDiffusionConfusion()

    # Test sur une fonction appliquant un masque
    f_masque = fBijParDecallage(3)
    f_masque.afficheGraphiquesDeDiffusionConfusion()


import random

class FeistelCipher8bits:
    def __init__(self, num_rounds=16):
        self.num_rounds = num_rounds
        self.subkey_generator = None

    def set_seed(self, seed):
        random.seed(seed)

    def generate_subkeys(self):
        return [random.randint(0, 255) for _ in range(self.num_rounds)]

    def feistel_function(self, half_block, subkey):
        # Exemple de fonction de Feistel (vous pouvez la remplacer par votre propre fonction)
        return (half_block + subkey) % 256

    def encrypt(self, block):
        left_half = block >> 4
        right_half = block & 0x0F

        subkeys = self.generate_subkeys()

        for round_num in range(self.num_rounds):
            new_right_half = left_half ^ self.feistel_function(right_half, subkeys[round_num])
            left_half = right_half
            right_half = new_right_half

        encrypted_block = (left_half << 4) | right_half
        return encrypted_block

    def decrypt(self, block):
        left_half = block >> 4
        right_half = block & 0x0F

        subkeys = self.generate_subkeys()

        for round_num in reversed(range(self.num_rounds)):
            new_right_half = left_half ^ self.feistel_function(right_half, subkeys[round_num])
            left_half = right_half
            right_half = new_right_half

        decrypted_block = (left_half << 4) | right_half
        return decrypted_block

# Exemple d'utilisation
def main():
    cipher = FeistelCipher8bits(num_rounds=4)
    cipher.set_seed(123)  # Vous pouvez changer la graine ici

    plaintext = 0b11011010
    ciphertext = cipher.encrypt(plaintext)
    decrypted_text = cipher.decrypt(ciphertext)

    print(f"Plaintext: {bin(plaintext)}")
    print(f"Ciphertext: {bin(ciphertext)}")
    print(f"Decrypted text: {bin(decrypted_text)}")

if __name__ == "__main__":
    main()

