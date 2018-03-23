import unittest

#write import statement for homework 7 file
from homework7 import get_p_distance, get_p_distance_matrix 


class TestHomework7(unittest.TestCase):

    def test_p_distance(self):
        self.assertEqual(.4,get_p_distance( \
             ['T','T','T','C','C','A','T','T','T','A'], \
             ['G','A','T','T','C','A','T','T','T','C']))

    def test_get_p_distance_matrix(self):
        dna = [
             ['T','T','T','C','C','A','T','T','T','A'],
             ['G','A','T','T','C','A','T','T','T','C'],
             ['T','T','T','C','C','A','T','T','T','T'],
             ['G','T','T','C','C','A','T','T','T','A']
            ]
        p_distance = [[0.0, 0.4, 0.1, 0.1], [0.4, 0.0, 0.4, 0.3],
                      [0.1, 0.4, 0.0, 0.2], [0.1, 0.3, 0.2, 0.0]]

        self.assertEqual(p_distance,get_p_distance_matrix(dna))

    #create a test for get p distance matrix with following data
    '''
    Sample Dataset
    [
     ['T','T','T','C','C','A','T','T','T','A'],
     ['G','A','T','T','C','A','T','T','T','C'],
     ['T','T','T','C','C','A','T','T','T','T'],
     ['G','T','T','C','C','A','T','T','T','A']
    ]
    
    Sample Output
    0.00000 0.40000 0.10000 0.10000
    0.40000 0.00000 0.40000 0.30000
    0.10000 0.40000 0.00000 0.20000
    0.10000 0.30000 0.20000 0.00000

    '''

unittest.main(verbosity=2)    
