"""Module providingFunction printing python version."""
import random


class RockPaperScissors(object):

    """
    Class to handle an instance of a Rock-Paper-Scissors game
    with score and round
    """

    def __init__(self):
        """
        Initialize the variables for the class
        """
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.round = 0
        self.options = {'rock': 0, 'paper': 1, 'scissors': 2}

    def random_choice(self):
        """
        Chooses a choice randomly from the keys in self.options.
        :returns: String containing the choice of the computer.
        """
        return random.choice(list(self.options.keys()))

    def check_win(self, player, opponent):
        """
        Check if the player wins or loses.
        :player: Numeric representation of player choice from self.options
        :opponent: Numeric representation of computer choice from self.options
        :return: player or oppent who got point and number of rounds
        """
        result = (player - opponent) % 3
        if result == 0:
            self.ties += 1
            self.round += 1
            return ("The game is a tie! You are a most worthy opponent!")
        elif result == 1:
            self.wins += 1
            self.round += 1
            return ("You got one point!")
        elif result == 2:
            self.losses += 1
            self.round += 1
            return ("Computer got one point!")

    def print_score(self):
        """
        Prints a string reflecting the current player score.
        :return: Nothing, just prints current score.
        """
        return (f"{self.round} rounds. You have {self.wins} wins, {self.losses} losses, and "f"{self.ties} ties. ")
    
    def player_choice(self, player_choice):
        """
        Prompts player for choice of rock, paper, or scissors.
        :return: 'rock', 'paper', or 'scissors'
        """
        if player_choice in self.options.keys():
            return player_choice
        elif player_choice == 'quit':
            return 'quit'
        else:
            return ("Invalid input, try again!")

    def run_game(self):
        """
        Run the game: The first to get five points wins the game. 
        :return: player and computer's choice every round; 
                 Cumulative points per round;
                 The total number of rounds played in total.
        """
        while True:
            if self.losses < 5 and self.wins < 5:     
                # When no player or computer accumulated 5 points,\
                # the game continues
                user_choice = input("Choices are 'rock', 'paper', or 'scissors'.\n"
                                    "Which do you choose? Or 'quit' (Get 5 points to become a winner))").lower().strip()
                user_choice = self.player_choice(user_choice)
                if user_choice in self.options.keys():
                    computer_choice = self.random_choice()
                    print(f"You've picked {user_choice}, and computer picked {computer_choice}.")
                    print(self.check_win(self.options[user_choice], self.options[computer_choice]))
                    print(game.print_score())
                elif user_choice == 'quit':    #Player can also quit the game at any time.
                    print("Game over. Bye!")
                    exit()
                elif user_choice == "Invalid input, try again!":    #prompt for invalid input
                    print("Invalid input, try again!")
                    continue

            if self.losses == 5:
                print("Computer is the winner!")
                RockPaperScissors.__init__(self)
                break
            if self.wins == 5:
                print("You are the winner! Congrats!")
                RockPaperScissors.__init__(self)
                break


if __name__ == "__main__":
    game = RockPaperScissors()    #Call the game
    while True:
        game.run_game()

        while True:

            continue_prompt = input('\nDo you wish to play again? (y/n): ').lower() #Ask player play again or not?
            if continue_prompt == 'n':         
                print("Game over. Bye!")    
                exit()                       #Termination of the game
            elif continue_prompt == 'y':
                game = RockPaperScissors()   #Restart the game
                break
            else:
                print("Invalid input!\n")    #Invalid input and ask again
                continue
