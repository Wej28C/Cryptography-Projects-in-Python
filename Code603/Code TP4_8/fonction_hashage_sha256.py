#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:25:43 2024

@author: beatrice
"""
import hashlib

def simple_hash(data):
    """Fonction de hachage simple utilisant SHA-256"""
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

# Exemple d'utilisation
data_to_hash = "Bonjour tout le monde!"
hashed_value = simple_hash(data_to_hash)
print(f"Data: {data_to_hash}\nHash: {hashed_value}")

