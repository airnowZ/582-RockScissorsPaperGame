import unittest
from RockPaperScissors import RockPaperScissors

class MyTestCase(unittest.TestCase):
    Game = RockPaperScissors()
    
    def test_player_choice(self):
        self.assertTrue(self.Game.player_choice('rock'), 'rock') #Valid input and return itself
        self.assertTrue(self.Game.player_choice('paper'), 'paper')  #Valid input and return itself
        self.assertTrue(self.Game.player_choice('scissors'), 'scissors')  #Valid input and return itself
        self.assertTrue(self.Game.player_choice('ROCK'), 'ROCK') #Valid input and return itself

    def test_player_quit(self):
        self.assertTrue(self.Game.player_choice('quit'), 'quit') #Valid input and return quit

    def test_player_invalid_input(self):
        self.assertTrue(self.Game.player_choice('AbVD'), 'Invalid input, try again!') #Invalid input and return

    def test_game_rule(self):                   #'rock': 0, 'paper': 1, 'scissors': 2
        self.assertEqual(self.Game.check_win(0,0), "The game is a tie! You are a most worthy opponent!")  # Tie, rock vs. rock
        self.assertEqual(self.Game.check_win(1,1), "The game is a tie! You are a most worthy opponent!")  # Tie  scissors vs. scissors
        self.assertEqual(self.Game.check_win(2,2), "The game is a tie! You are a most worthy opponent!")  # Tie  paper vs. paper
        self.assertEqual(self.Game.check_win(1,0), "You got one point!")  #Player's rock smashes computer's scissors.
        self.assertEqual(self.Game.check_win(2,1), "You got one point!")  #Player's scissors cuts computer's paper.
        self.assertEqual(self.Game.check_win(0,2), "You got one point!")  #Player's rock paper covers computer's rock.
        self.assertEqual(self.Game.check_win(2,0), "Computer got one point!")  #Computer's rock smashes player's scissors.
        self.assertEqual(self.Game.check_win(1,2), "Computer got one point!")  #Computer's scissors cuts player's paper.
        self.assertEqual(self.Game.check_win(0,1), "Computer got one point!")  #Computer's paper covers player's rock.



if __name__ == '__main__':
    unittest.main()