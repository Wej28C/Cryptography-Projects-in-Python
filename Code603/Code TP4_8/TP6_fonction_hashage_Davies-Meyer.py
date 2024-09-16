#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:26:27 2024

@author: beatrice
"""

from LBinaire603 import LBinaire603
from CodeurCA import CodeurCA


def davies_meyer_hash(codeur: CodeurCA, data: LBinaire603) -> LBinaire603:
    # Utilisation de la construction de Davies-Meyer
    padded_data = _pad_data(data)
    hashed_data = codeur.binCode(padded_data)
    return hashed_data

def _pad_data(data: LBinaire603) -> LBinaire603:
    # Par exemple, ajouter un padding pour atteindre une taille spécifique
    padded_data = data  
    return padded_data

# Exemple d'utilisation
if __name__ == "__main__":
    # Supposons que vous ayez déjà une instance de CodeurCA, par exemple:
    monCodeur = CodeurCA()

    # Données à hacher
    data_to_hash = LBinaire603.exBin603(num=42, taille=128)

    # Utilisation de la fonction de hachage
    hashed_value = davies_meyer_hash(monCodeur, data_to_hash)

    print(f"Data to hash: {data_to_hash}")
    print(f"Hashed value: {hashed_value}")

