#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      utilisateur
#
# Created:     08/03/2024
# Copyright:   (c) utilisateur 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from LBinaire603 import *
from CodeurCA import CodeurCA
from PolF2 import PolF2
class CodeurCRC8(CodeurCA):
 """CodeurCRC codant en 40bits des blocs 32bits avec CRC sur 8bits"""
 def __init__(self,Pg=PolF2(0b110011011) ):
     assert Pg.degre()<=8
     self.Pg=Pg
 def __str__(self):
    return f'CodeurCRC avec {self.Pg=}'
 def __repr__(self):
    return f"CodeurCRC8(Pg=PolF2(0b{int(self.Pg):b}))"

# bloc code prend un mot de 32 bit et retourne mot de 40 bits

#blocCode(mot32bit): B=PolF2(mot32bit) X.Ps+(X^y.Ps)%Pg
 def blocCode(self,M,verbose=False):
     '''Renvoie M codé en CRC avec un octet de plus"
     >>> print(f"0x{CodeurCRC8().blocCode(0xab345678):x}")
     0xab34567821
     '''
     #pass
     B = PolF2(M)
     for i in range(8):
        if int(B) & (1 << (31 - i)):
            B ^= PolF2(int(self.Pg) << i)
     return int(B)
 def estBlocValide(self,valc):
     """
     >>> CodeurCRC8().estBlocValide(0xab34567821)
     True
     >>> CodeurCRC8().estBlocValide(0xab34567820)
     False
     """
     B = PolF2(valc)
     return int(B) == 0
 def blocValideLePlusProche(self,valc,verbose=False):
     """
     >>> print(f"0x{CodeurCRC8().blocValideLePlusProche(0xab34567821):x}")
     0xab34567821
     >>> print(f"0x{CodeurCRC8().blocValideLePlusProche(0xab35567821):x}")
     0xab34567821
     """
     B = PolF2(valc)
     for i in range(8):
        if int(B) & (1 << i):
            B ^= PolF2(int(self.Pg) << (31 - i))
     return int(B)

 def binCode(self,monBinD,verbose=True,nbErreurs=0):
     bc=LBinaire603()
     bd=LBinaire603(monBinD)
     bc.ajouteLongueValeur(len(bd))
     if len(bd)%4!=0: bd+=[0]*(4-len(bd)%4) #On complète pour avoir une liste de 4*N
     pos=0
     while pos<len(bd):
         M,pos =bd.lisMot32bits(pos)
         bc.ajouteMot(self.blocCode(M),5)
     return bc
 def blocDecode(self, block):
    """
    Décode un bloc de 40 bits codé avec le CRC8.

    Args:
        block (LBinaire603): Le bloc de 40 bits à décoder.

    Returns:
        int: Le bloc décodé.

    Raises:
        ValueError: Si le bloc contient des erreurs et ne peut pas être décodé.

    """
    B = PolF2(int(block.toString(), 16))
    remainder = B % self.Pg
    if remainder.estNul():
        return int(B // self.Pg)
    else:
        raise ValueError("Le bloc contient des erreurs et ne peut pas être décodé.")
 def binDecode(self, bc):
     pos = 0  # Initialiser la position de lecture
     length, pos = bc.lisLongueValeur(pos)  # Lire la longueur du message
     message_decode = 0  # Initialiser le message décodé

        # Lire chaque mot de 32 bits dans le message binaire
     for _ in range(length):
         mot, pos = bc.lisMot32Bits(pos)
         message_decode = mot  # Mettre à jour le message décodé

     return message_decode
if __name__ == "__main__":
    codeur = CodeurCRC8()

    # Test de la méthode blocCode
    mot_code = codeur.blocCode(0xAB345678)
    print(f"Mot codé : 0x{mot_code:x}")  # Devrait afficher : 0xab34567821

    # Test de la méthode estBlocValide
    bloc_valide = 0xAB34567821
    bloc_invalide = 0xAB34567820
    print("Le bloc valide est-il correct ?", codeur.estBlocValide(bloc_valide))  # Devrait afficher : True
    print("Le bloc invalide est-il correct ?", codeur.estBlocValide(bloc_invalide))  # Devrait afficher : False

    # Test de la méthode blocValideLePlusProche
    bloc_proche = codeur.blocValideLePlusProche(0xAB35567821)
    print(f"Bloc valide le plus proche : 0x{bloc_proche:x}")

    codeur2 = CodeurCRC8()

    # Créer un message binaire codé avec le CRC8
    message_binaire = LBinaire603()
    message_binaire.ajouteLongueValeur(1)
    message_binaire.ajouteOctet(0xab)
    message_binaire.ajouteMot32Bits(0x345678)

    # Décoder le message binaire
    message_decode = codeur2.binDecode(message_binaire)

    # Afficher le message décodé
    print("Message décodé:", message_decode)