import unittest

#write import statements for exam functions
#from src.midterm.exam import get_miles_per_hour
from src.midterm.exam import get_miles_per_hour, get_bonus_pay_amount, reverse_string, get_list_min_max

class Test_Midterm(unittest.TestCase):

    def test_get_miles_per_hour(self):
        '''
        5 points
        Test with arguments kilometers 32 and minutes 60 return value should be 19.883872
        '''
        self.assertEqual(19.883872,get_miles_per_hour(32,60))

    def test_get_miles_per_hour_w_Neg_kilometers(self):
        self.assertEqual('Invalid arguments',get_miles_per_hour(-5,60))

    def test_get_miles_per_hour_w_Neg_minutes(self):
        self.assertEqual('Invalid arguments',get_miles_per_hour(32,-5))


    def test_get_bonus_pay_amount_w_good_value (self):
        '''
        5 points
        Test with value 1000 return value should be 70
        '''
        self.assertEqual(70,get_bonus_pay_amount(1000))


    def test_get_bonus_pay_amount_w_bad_value(self):
        '''
        5 points
        Test with -5 return value should be 'Invalid arguments'
        '''
        self.assertEqual('Invalid arguments',get_bonus_pay_amount(-5))


    def test_reverse_string(self):
        '''
        5 points
        Test with value My String Data return value should be ataD gnirtS yM
        '''
        self.assertEqual('ataD gnirtS yM', reverse_string('My String Data')) 


    def test_get_list_min_max(self):
        '''
        5 points
        Test with ['joe', 10, 15, 20, 30, 40]    Returns:    [10, 40]
        '''
        self.assertEqual([10, 40], get_list_min_max(['joe', 10, 15, 20, 30, 40]))


    def test_get_list_min_max_file(self):
        '''
        5 points
        Test with quiz.data file the return value should be [2,89]
        '''
unittest.main(verbosity=2)
    
