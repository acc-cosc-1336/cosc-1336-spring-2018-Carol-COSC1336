import unittest
from practice import get_km_per_hour, get_shipping_charge, get_total_of_numbers_squared, \
     get_quiz_list, get_quiz_list_file

class Test_Practice(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1,1)

    def test_get_km_per_hour(self):
        self.assertEqual(32, get_km_per_hour(20, 60))

    def test_get_km_per_hour_w_120(self):
        self.assertEqual(16, get_km_per_hour(20, 120))

    def test_get_km_per_hour_w_90(self):
        self.assertEqual(21.33, get_km_per_hour(20, 90))

    def test_get_km_per_hour_w_dec_miles_30(self):
        self.assertEqual(4.8, get_km_per_hour(1.5, 30))        

    #Write a test case for function get_shipping_charge with argument 2
    #return value should be 2.5
    def test_get_shipping_charge_w_2and_a_half(self):
        self.assertEqual(2.75, get_shipping_charge(2.5))

    def test_get_shipping_charge_w_Negative_1(self):
        self.assertEqual('Invalid weight range', get_shipping_charge(-1))


    #Write a test case for function get_total_of_numbers_squared with argument 5
    #return value should be 30
    def test_get_total_of_numbers_squared(self):
        self.assertEqual(30, get_total_of_numbers_squared(5))

    #Write a test case for function get_quiz_list with argument
    '''
    [
    ['joe', 10, 15, 20, 30, 40],
    ['bill', 23, 16, 19, 22],
    ['sue', 8, 22, 17, 14, 32, 17, 24, 21, 2, 9, 11, 17],
    ['grace', 12, 28, 21, 45, 26, 10, 11],
    ['john', 14, 32, 25, 16, 89]
    ]
    '''
    #return value should be
    '''
    ['sue', 'grace']
    '''
    def test_get_quiz_list(self):
        list_arg = [
                ['joe', 10, 15, 20, 30, 40],
                ['bill', 23, 16, 19, 22],
                ['sue', 8, 22, 17, 14, 32, 17, 24, 21, 2, 9, 11, 17],
                ['grace', 12, 28, 21, 45, 26, 10, 11],
                ['john', 14, 32, 25, 16, 89]
            ]
        
        self.assertEqual(['sue', 'grace'], get_quiz_list(list_arg))

    def test_get_quiz_list_file(self):
        self.assertEqual(['sue', 'grace'], get_quiz_list_file())


unittest.main(verbosity=2)
