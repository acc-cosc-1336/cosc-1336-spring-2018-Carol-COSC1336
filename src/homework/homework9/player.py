#write import statement for Die class
from src.homework.homework9.die import Die

'''
Create a Player class.

'''

class Player:

    def __init__(self):
        '''
        Constructor method creates two Die attributes die1 and die2
        '''
        self.die1 = Die()
        self.die2 = Die()

    def roll_doubles(self):
        '''
        The roll_doubles method that will roll die1 and die2 (attributes from constructor method),
        display rolled values,and continue iterating until a double is rolled.
        '''
        dice1 = 1
        dice2 = 2
        while dice1 != dice2:
            dice1 = self.die1.roll()
            print('Dice 1: ', dice1)
            dice2 = self.die2.roll()
            print('Dice 2: ', dice2)
            
        if dice1 == dice2:
            print('Doubles rolled! Both die = ', dice1)
            


