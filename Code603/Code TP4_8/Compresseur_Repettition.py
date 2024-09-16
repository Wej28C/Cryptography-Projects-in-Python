#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Wejdane
#
# Created:     28/02/2024
# Copyright:   (c) utilisateur 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from LBinaire603 import *
from CodeurCA import *


class RepetitionCompressor(CodeurCA):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "RepetitionCompressor"

    def __repr__(self):
        return "RepetitionCompressor()"

    def binCode(self, monBinD: LBinaire603) -> LBinaire603:
        """
        Compresses the input LBinaire603 using Repetition Compression.

        Args:
        monBinD (LBinaire603): Input binary data.

        Returns:
        LBinaire603: Compressed binary data.
        """
        compressed_data = LBinaire603()

        current_bit = monBinD[0]
        count = 1

        for bit in monBinD[1:]:
            if bit == current_bit:
                count += 1
            else:
                compressed_data += LBinaire603([count, current_bit])
                count = 1
                current_bit = bit

        compressed_data += LBinaire603([count, current_bit])

        return compressed_data

    def binDecode(self, monBinC: LBinaire603) -> LBinaire603:
        """
        Decompresses the input LBinaire603 using Repetition Decompression.

        Args:
        monBinC (LBinaire603): Compressed binary data.

        Returns:
        LBinaire603: Decompressed binary data.
        """
        decompressed_data = LBinaire603()

        for i in range(0, len(monBinC), 2):
            count, bit = monBinC[i], monBinC[i + 1]
            decompressed_data += LBinaire603([bit] * count)

        return decompressed_data


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    repetition_compressor = RepetitionCompressor()

    for k in range(5):
        monBin = LBinaire603.exBin603(num=k, taille=25)
        print("Bin:", monBin)

        monBinCr = repetition_compressor.binCode(monBin)
        print("Bin Codée:", monBinCr)

        print(
            "monBinCr décodé est égal à Monbin ?",
            repetition_compressor.binDecode(monBinCr) == monBin,
        )
