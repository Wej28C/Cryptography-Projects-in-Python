#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 22:15:56 2024

@author: beatrice
"""

import random

def estPremierOuPseudoPremierAvecA(n, a):
    """
    Renvoie le test de la pseudo-primalité d'un entier n selon Miller-Rabin
avec le nombre a => True si n est probablement premier ou pseudo-premier avec la base a,
    False sinon.
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    
    for _ in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    
    return False

def estPremierOuPseudoPremierAvecLA(n, la):
    """`
    Renvoie le test effectué sur n avec chacune des valeurs a de la liste la
    Renvoie True si n est probablement premier ou pseudo-premier avec toutes les bases de la liste la,
    False sinon.
    """
    for a in la:
        if not estPremierOuPseudoPremierAvecA(n, a):
            return False
    return True

def premierFauxPositif(la):
    """
    Renvoie le premier entier pour lequel la fonction estPremierOuPseudoPremierAvecLA renvoie un résultat différent de la fonction estPremier.
    """
    n = 4
    while True:
        if not estPremierOuPseudoPremierAvecLA(n, la) and estPremier(n):
            return n
        n += 1

def isPrime(n, k=5):
    """
    Test de primalité probabiliste de Miller-Rabin
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Trouver r et d tels que n-1 = 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Effectuer k tests
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def estPremier(n):
    """
    Vérifie si un nombre est premier.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Exemple d'utilisation

print(estPremierOuPseudoPremierAvecA(121, 2))
la = [2,3]
print(estPremierOuPseudoPremierAvecLA(120, la))
lb = [2,3,5]
print(" Fonction premierFauxPositif :", premierFauxPositif(lb))
#print(premierFauxPositif([2,3,5]))
