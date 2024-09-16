#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:50:25 2024

@author: beatrice
"""

import random
import matplotlib.pyplot as plt

def generate_birthdays(num_people):
    birthdays = [random.randint(1, 365) for _ in range(num_people)]
    return birthdays

def has_collision(birthdays):
    unique_birthdays = set()
    for day in birthdays:
        if day in unique_birthdays:
            return True
        unique_birthdays.add(day)
    return False

def birthday_paradox_simulation(num_simulations, num_people):
    collision_count = 0

    for _ in range(num_simulations):
        birthdays = generate_birthdays(num_people)
        if has_collision(birthdays):
            collision_count += 1

    probability = collision_count / num_simulations
    return probability

def plot_birthday_paradox(num_people_range, num_simulations):
    probabilities = []

    for num_people in num_people_range:
        probability = birthday_paradox_simulation(num_simulations, num_people)
        probabilities.append(probability)

    plt.plot(num_people_range, probabilities, marker='o')
    plt.title('Probabilité du Paradoxe des Anniversaires')
    plt.xlabel('Nombre de personnes')
    plt.ylabel('Probabilité de collision')
    plt.show()

# Paramètres de la simulation
num_simulations = 1000
num_people_range = range(2, 101)  # Vous pouvez ajuster la plage selon vos besoins

# Exécution de la simulation et tracé de la courbe
plot_birthday_paradox(num_people_range, num_simulations)
