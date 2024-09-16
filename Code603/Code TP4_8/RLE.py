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


from LBinaire603 import *
from CodeurCA import*

class RLE(CodeurCA):
    """Un codeur doit surcharger les méthodes __init__ __repr__ __str__
    binCode, binDecode et codeurTest
    renvoyant et recevant un LBinaire603
    C'est une forme de classe abstraites"""
    def __init__(self ):
       super().__init__()

    def __str__(self):
       return "CodeurRLE"
    def __repr__(self):
       return "CodeurRLE()"

    def binCode(self,monBinD:LBinaire603)->LBinaire603:
       """
        Compresses the input LBinaire603 using Run-Length Encoding (RLE).

        Args:
        monBinD (LBinaire603): Input binary data.

        Returns:
        LBinaire603: Compressed binary data.
        """

        # Initialize an empty LBinaire603 for compressed data
       compressed_data = LBinaire603()
       current_run = monBinD[0]  # Initialize the current run with the first bit of input data
       count = 1  # Initialize the count for the current run

        # Iterate through the input data starting from the second bit
       for bit in monBinD[1:]:
        if bit == current_run:
                # If the current bit is equal to the previous one, increment the count
            count += 1
        else:
                # If the current bit is different, append the run to the compressed data
            compressed_data += LBinaire603([count, current_run])
                # Reset the count and update the current run
            count = 1
            current_run = bit

        # Append the last run to the compressed data
       compressed_data += LBinaire603([count, current_run])

       return compressed_data

    def binDecode(self,monBinC:LBinaire603)->LBinaire603:
        """
        Decompresses the input LBinaire603 using Run-Length Decoding (RLD).

        Args:
        monBinC (LBinaire603): Compressed binary data.

        Returns:
        LBinaire603: Decompressed binary data.
        """
        decompressed_data = LBinaire603()  # Initialize an empty LBinaire603 for decompressed data

        # Iterate through the compressed data
        for i in range(0, len(monBinC), 2):
            count, bit = monBinC[i], monBinC[i + 1]
            # Append the run to the decompressed data
            decompressed_data += LBinaire603([bit] * count)

        return decompressed_data




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    monCompresseur=RLE() #A modifier si repris dans une classe en héritant
    for k in range(5):
       monBin=LBinaire603.exBin603(num=k,taille=25)
       print("Bin:",monBin)
       monBinCr=monCompresseur.binCode(monBin)
       print("Bin Codée:",monBinCr)
       print("monBinCr décodé est égal à Monbin ?",monCompresseur.binDecode(monBinCr)==monBin)


