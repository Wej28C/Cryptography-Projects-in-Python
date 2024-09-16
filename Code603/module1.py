#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      utilisateur
#
# Created:     15/12/2023
# Copyright:   (c) utilisateur 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import unittest
import numpy as np
import matplotlib.pyplot as plt
import random

class FBijection8bitsCA:
    # Abstract class definition as provided in the question
    # ...


class AffineBijection(FBijection8bitsCA):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"AffineBijection(a={self.a}, b={self.b})"

    def __call__(self, octet):
        return (self.a * octet + self.b) % 256

    def valInv(self, octetC):
        return ((octetC - self.b) * self.modinv(self.a, 256)) % 256

    # Additional methods for modular inverse and other necessary functions
    # ...

    # Unit tests for the AffineBijection class
class TestAffineBijection(unittest.TestCase):
    def test_bijection_property(self):
        # Test the bijection property for a specific input
        a = 3
        b = 7
        bijection = AffineBijection(a, b)
        x = 42
        self.assertEqual(bijection.valInv(bijection(x)), x)

    def test_diffusion_confusion(self):
        # Test the diffusion and confusion properties
        a = 5
        b = 3
        bijection = AffineBijection(a, b)
        bijection.construitGraphique()
        bijection.construitGraphiqueDifferentielle()

if __name__ == '__main__':
    unittest.main()
