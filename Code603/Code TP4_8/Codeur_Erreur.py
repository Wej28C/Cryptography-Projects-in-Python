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

def TestErreur(binaire603):
    # Vérifier si la longueur du binaire603 est correcte
    if len(binaire603) != 64 + 8 + 8:
        return "Erreur: Taille incorrecte du binaire603"

    # Créer une matrice carrée à partir des 64 premiers octets
    matrice_carree = [binaire603[i:i+8] for i in range(0, 64, 8)]

    # Calculer les sommes des lignes et des colonnes
    sommes_lignes = [sum(row) for row in matrice_carree]
    sommes_colonnes = [sum(col) for col in zip(*matrice_carree)]

    # Vérifier si les sommes correspondent aux 8 octets suivants
    if sommes_lignes == binaire603[64:72] and sommes_colonnes == binaire603[72:]:
        return "Les sommes des lignes et des colonnes sont correctes"
    else:
        # Trouver l'erreur s'il y en a une
        erreur = None
        for i, row_sum in enumerate(sommes_lignes):
            if row_sum != binaire603[64 + i]:
                erreur = (i, "ligne")
                break
        if not erreur:
            for j, col_sum in enumerate(sommes_colonnes):
                if col_sum != binaire603[72 + j]:
                    erreur = (j, "colonne")
                    break

        return f"Erreur: L'erreur est à la {erreur[1]} {erreur[0]}"

def codeurCA(LBinaire603):
    result = []
    for i in range(0, len(LBinaire603), 64):
        sous_liste = LBinaire603[i:i+64]
        sommes_lignes = [sum(sous_liste[j:j+8]) for j in range(0, 64, 8)]
        sommes_colonnes = [sum(col) for col in zip(*[sous_liste[j:j+8] for j in range(0, 64, 8)])]
        result.extend(sous_liste + sommes_lignes + sommes_colonnes)

    return result


# Tester la fonction TestErreur
binaire603_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                   31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
                   # Les sommes des lignes correctes
                   # Les sommes des colonnes correctes
                   # Erreur dans la première ligne
                   # Erreur dans la deuxième colonne
                  ]
print(TestErreur(binaire603_test))

# Tester la fonction codeurCA
LBinaire603_test = [1] * (64 * 5) # Remplacer n par le nombre de sous-listes désiré
resultat_codeurCA = codeurCA(LBinaire603_test)
print(resultat_codeurCA)