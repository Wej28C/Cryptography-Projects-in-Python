#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      utilisateur
#
# Created:     28/02/2024
# Copyright:   (c) utilisateur 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from scipy.stats import chisquare
import hashlib

def calculate_byte_frequencies(data):
    """Calcule les fréquences des octets dans une liste de hash SHA256"""
    byte_frequencies = [0] * 256
    for hash_value in data:
        first_byte = int(hash_value[:2], 16)  # Convertit les deux premiers caractères hexadécimaux en décimal
        byte_frequencies[first_byte] += 1
    return byte_frequencies

def calculate_byte_order_frequencies(data, order):
    """Calcule les fréquences des ordres des premiers octets dans une liste de hash SHA256"""
    byte_order_frequencies = [0] * (256 ** order)
    for hash_value in data:
        byte_order = int(hash_value[:2 * order], 16)  # Convertit les premiers caractères hexadécimaux en décimal
        byte_order_frequencies[byte_order] += 1
    return byte_order_frequencies

# Générer des hash SHA256 pour des données factices (remplacez cela par vos données réelles)
data = [hashlib.sha256(f"Data{i}".encode('utf-8')).hexdigest() for i in range(1000)]

# Test de fréquence sur le premier octet
first_byte_frequencies = calculate_byte_frequencies(data)
expected_frequencies = [len(data) / 256] * 256  # Fréquence attendue pour un hachage uniforme
chi2_statistic_first_byte, p_value_first_byte = chisquare(f_obs=first_byte_frequencies, f_exp=expected_frequencies)

print(f"Test de fréquence sur le premier octet:")
print(f"Statistique du chi²: {chi2_statistic_first_byte}")
print(f"P-valeur: {p_value_first_byte}")
print()

# Test de fréquence sur les trois premiers octets
byte_order_frequencies = calculate_byte_order_frequencies(data, order=3)
expected_frequencies_order = [len(data) / (256 ** 3)] * (256 ** 3)  # Fréquence attendue pour un hachage uniforme
chi2_statistic_order, p_value_order = chisquare(f_obs=byte_order_frequencies, f_exp=expected_frequencies_order)

print(f"Test de fréquence sur les trois premiers octets:")
print(f"Statistique du chi²: {chi2_statistic_order}")
print(f"P-valeur: {p_value_order}")
