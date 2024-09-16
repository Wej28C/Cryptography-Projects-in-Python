#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 22:45:35 2024

@author: beatrice
"""

import random
import math

def estPremier(n, k=5):
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

def generer_cles_RSA(taille):
    """
    Génère une paire de clés RSA.
    La taille est la taille en bits du module RSA.
    Retourne une paire de clés (clé publique, clé privée).
    """
    p = generer_nombre_premier(taille // 2)
    q = generer_nombre_premier(taille // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = choisir_exposant_public(phi)
    d = inverser_modulo(e, phi)
    return ((e, n), (d, n))

def generer_nombre_premier(taille):
    """
    Génère un nombre premier aléatoire de la taille spécifiée en bits.
    """
    while True:
        nombre = random.getrandbits(taille)
        if estPremier(nombre):
            return nombre

def choisir_exposant_public(phi):
    """
    Choix d'un exposant public e.
    """
    e = random.randrange(2, phi)
    while math.gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    return e

def inverser_modulo(a, m):
    """
    Calcule l'inverse modulaire de a modulo m.
    """
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def chiffreur_RSA(message, cle_publique):
    """
    Chiffre un message avec la clé publique RSA.
    """
    e, n = cle_publique
    chiffre = [pow(ord(char), e, n) for char in message]
    return chiffre

def dechiffrer_RSA(chiffre, cle_privee):
    """
    Déchiffre un message chiffré avec la clé privée RSA.
    """
    d, n = cle_privee
    message = ''.join([chr(pow(char, d, n)) for char in chiffre])
    return message

# Exemple d'utilisation
taille_cle = 1000
cle_publique, cle_privee = generer_cles_RSA(taille_cle)
message_original = "Coucou, c'est moi Beatrice, ca va Wejdene?"
print("Message original:", message_original)

message_chiffre = chiffreur_RSA(message_original, cle_publique)
print("Message chiffré:", message_chiffre)

message_dechiffre = dechiffrer_RSA(message_chiffre, cle_privee)
print("Message déchiffré:", message_dechiffre)