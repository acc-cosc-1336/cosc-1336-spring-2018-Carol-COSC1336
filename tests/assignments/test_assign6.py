import unittest

#write the import for function get_count_A_C_G_and_T_in_string
from src.assignments.assignment6 import get_count_A_C_G_and_T_in_string
#from assignment6 import get_count_A_C_G_and_T_in_string

class Test_Assign6(unittest.TestCase):

    def test_countACGT_w_string_ATGCTTCAGAAAGGTCTTACG(self):
        '''
        Create a test case to test the count of As, Cs, Gs, and Ts in string ATGCTTCAGAAAGGTCTTACG
        '''
        countA,countC,countG,countT = get_count_A_C_G_and_T_in_string('ATGCTTCAGAAAGGTCTTACG')

        self.assertEqual(6, countA)
        self.assertEqual(4, countC)
        self.assertEqual(5, countG)
        self.assertEqual(6, countT)
        
    def test_count_ACGT_w_stringAGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC(self):
        '''
        Create a test case to test the count of As, Cs, Gs, and Ts in string
        AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
        '''
        countA,countC,countG,countT = get_count_A_C_G_and_T_in_string('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')

        self.assertEqual(20, countA)
        self.assertEqual(12, countC)
        self.assertEqual(17, countG)
        self.assertEqual(21, countT)

#unittest.main(verbosity=2)
