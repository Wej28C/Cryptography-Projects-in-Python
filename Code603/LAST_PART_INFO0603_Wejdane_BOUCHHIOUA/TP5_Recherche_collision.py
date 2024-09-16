#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 01:42:49 2024

@author: beatrice
"""

import random
import matplotlib.pyplot as plt

def recherche_collision(liste):
    """
    Simule la recherche de collision dans une liste de MP3.
    Renvoie le nombre de tirages nécessaires pour obtenir une collision.
    """
    tirages = 0
    mp3_deja_tires = set()
    while True:
        mp3 = random.choice(liste)
        tirages += 1
        if mp3 in mp3_deja_tires:
            return tirages
        else:
            mp3_deja_tires.add(mp3)

def statistiques(taille_liste, nb_simulations):
    """
    Effectue nb_simulations de recherche de collision pour une liste de taille_liste.
    Renvoie la moyenne du nombre de tirages nécessaires pour obtenir une collision.
    """
    total_tirages = 0
    for _ in range(nb_simulations):
        liste_mp3 = [f"MP3_{i}" for i in range(taille_liste)]
        total_tirages += recherche_collision(liste_mp3)
    return total_tirages / nb_simulations

def generer_graphique(taille_max_liste, pas, nb_simulations):
    """
    Génère un graphique représentant en moyenne le nombre de tirages sans collision en fonction de la taille de la liste.
    """
    tailles_listes = range(1, taille_max_liste + 1, pas)
    moyennes_tirages = [statistiques(taille, nb_simulations) for taille in tailles_listes]

    plt.plot(tailles_listes, moyennes_tirages, marker='o')
    plt.title("Nombre moyen de tirages sans collision en fonction de la taille de la liste")
    plt.xlabel("Taille de la liste de MP3")
    plt.ylabel("Nombre moyen de tirages")
    plt.grid(True)
    plt.show()

# Paramètres
taille_max_liste = 1000  # Taille maximale de la liste de MP3
pas = 50  # Pas entre les tailles de liste
nb_simulations = 1000  # Nombre de simulations pour chaque taille de liste

# Générer le graphique
generer_graphique(taille_max_liste, pas, nb_simulations)
