#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:14:40 2024

@author: beatrice
"""

import hashlib

# Fonction pour calculer le hash SHA-256 d'une chaîne de texte
def sha256_hash(text):
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    return sha256.hexdigest()

# Critère 1: Consistance - Le hash doit être le même pour la même entrée
input_text = "Hello, World!"
hash1 = sha256_hash(input_text)
hash2 = sha256_hash(input_text)

print(f"Critère 1: Consistance - Le hash pour la même entrée est identique:")
print(f"Hash 1: {hash1}")
print(f"Hash 2: {hash2}")
print()

# Critère 2: Sensibilité à la casse - Des entrées avec des cas différents doivent produire des hash différents
input_text_upper = "HELLO, WORLD!"
hash_upper = sha256_hash(input_text_upper)

print(f"Critère 2: Sensibilité à la casse - Des entrées avec des cas différents produisent des hash différents:")
print(f"Hash pour 'Hello, World!': {hash1}")
print(f"Hash pour 'HELLO, WORLD!': {hash_upper}")
print()

# Critère 3: Résistance aux collisions - Deux entrées différentes ne devraient pas produire le même hash
input_text_1 = "This is a test."
input_text_2 = "This is another test."
hash_1 = sha256_hash(input_text_1)
hash_2 = sha256_hash(input_text_2)

print(f"Critère 3: Résistance aux collisions - Deux entrées différentes produisent des hash différents:")
print(f"Hash pour 'This is a test.': {hash_1}")
print(f"Hash pour 'This is another test.': {hash_2}")
