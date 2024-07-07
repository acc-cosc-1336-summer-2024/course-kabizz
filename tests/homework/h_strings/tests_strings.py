import unittest

from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import complement_sequence

class Test_Config(unittest.TestCase):
    #Tests The DNA sequence hamming distance
    def test_get_hamming_distance(self):
        self.assertEqual(7, get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))
        #Test DNA complement sequence
    def test_complement_sequence(self):
        self.assertEqual(complement_sequence("AAAACCCGGT"), "TTTTGGGCCA")

