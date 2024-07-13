import unittest
from src.homework.i_dictionaries_sets.dictionary import get_p_distance, get_p_distance_matrix

class Test_Config(unittest.TestCase):

    def test_p_distance(self):
        s1 = ['T','T','T','C','C','A','T','T','T','A']
        s2 = ['G','A','T','T','C','A','T','T','T','C']
        self.assertAlmostEqual(get_p_distance(s1, s2), 0.4, places=3)

    def test_get_p_distance_matrix(self):
        dna_strings = [
            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A']
        ]
        expected_matrix = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]
        result_matrix = get_p_distance_matrix(dna_strings)
        for i in range(len(expected_matrix)):
            for j in range(len(expected_matrix[i])):
                self.assertAlmostEqual(result_matrix[i][j], expected_matrix[i][j], places=3)

if __name__ == '__main__':
    unittest.main()
