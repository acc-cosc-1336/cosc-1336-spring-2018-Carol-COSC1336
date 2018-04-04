#write import statements for Player and Die class
from src.homework.homework9.die import Die
from src.homework.homework9.player import Player

#Create an instance of the Main class and call/execute the roll_doubles method

class Main:

    def run_game(self):
        self.player = Player()
        self.player.roll_doubles()
        
main = Main()
main.run_game()
