import unittest
#write import statements for required classes or functions

from hourly_employee import HourlyEmployee
from salaried_employee import SalariedEmployee
from player import Player
from motif import non_contiguous_motif

class TestFinalExam(unittest.TestCase):

    #3 points
    #Create a test case to test the non_contiguous_motif  function with values
    #['A', 'C','G','T','A','C','G','T','G','A','C','G'] that returns three values 3, 8, and 10
    def test_non_contiguous_motif_w_ACG_dna_list(self):
        self.assertEqual((2,5,4), non_contiguous_motif('ACG', [ 'T','A','T','G','C','T','A','A','G','A','T','C'] ))
    
    #3 points
    #For the Player class create a test case, to test the check_come_out_roll
    #with argument values True, 8, and 9 the result should be 'Invalid range'
    player1 = Player(True, 8,9)
    def test_check_come_out_roll_w_True_8_9(self):
        self.assertEqual('Invalid range', self.player1.check_come_out_roll())
    #3 points
    #For the Player class create a test case, to test the check_come_out_roll
    #with argument values False, 4 and 3 should return 'Loser'
    player2 = Player(False,4,3)
    def test_check_come_out_roll_w_False_4_3(self):
        self.assertEqual('Loser', self.player2.check_come_out_roll())

    #3 points
    #For the Player class create a test case, to test the check_come_out_roll
    #with argument values False, 4 and 3 should return 'Loser'
    player3 = Player(True,5,6)
    def test_check_come_out_roll_w_True_5_6(self):
        self.assertEqual('Winner', self.player3.check_come_out_roll())
    
    #3 points
    #Add a test case for HourlyEmployee that calls the calculate method with values 10 and 80 to yield a result of 800.
    he = HourlyEmployee(1,'joe',10,80)
    def test_HourlyEmployee_w_10_80(self):
        self.assertEqual(800, self.he.calculate())

    #3 points
    #Add a test case for SalariedEmployee that calls the calculate method with values 260000 to yield a result of 10000.
    sal_employee = SalariedEmployee(2, 'Mike',260000)
    def test_SalariedEmployee_w_260000_10000(self):
        self.assertEqual(10000, self.sal_employee.calculate())
       

unittest.main(verbosity=2)
        
