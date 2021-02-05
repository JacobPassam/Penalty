import random
import time
from datetime import datetime

from data.scoresFile import ScoresFileHandler
from game.finalScore import FinalScore
from pref.preferencesManager import PreferencesManager

POSSIBLE_MOVES = ["left", "centre", "right"]  # Constant for player/keeper possible moves.


class Game:  # Class to represent a game being played.

    def __init__(self, prefManager: PreferencesManager, scoreHandler: ScoresFileHandler):
        self.playerScore = 0
        self.keeperScore = 0

        # Copy instances of managers into self. Ensures they are accessible by play() and game_end().
        self.prefManager = prefManager
        self.scoreHandler = scoreHandler

        self.rounds = prefManager.get_preference('Rounds')  # Set rounds to the preference set by the user.

    def play(self):  # Begins and plays the game.
        print()
        print('Welcome to the game! Player \'' + self.prefManager.get_preference('PlayerName') + '\' is playing.')

        for i in range(self.rounds):  # Execute each round.
            print()
            print('You are playing Round ' + str(i + 1) + "/" + str(self.rounds) + ".")

            keeper_move = POSSIBLE_MOVES[random.randint(0, (
                    len(POSSIBLE_MOVES) - 1))]  # Decide the keeper move beforehand, as requested in brief.
            player_move = ""

            # Enter the player's move. Loop until it is valid (inside POSSIBLE_MOVES).
            valid = False
            while not valid:
                player_move = input("Enter your move: ")
                if player_move not in POSSIBLE_MOVES:
                    print("That is not a valid move. (left, centre, or right)")
                else:
                    valid = True

            if keeper_move == player_move:  # If the keeper and the player moved in the same direction, the ball was
                # saved.
                self.keeperScore += 1
                print("The penalty was saved by the keeper.")
            else:  # Otherwise, the ball hit somewhere where the keeper was not at. A goal was scored.
                self.playerScore += 1
                print("You scored!")

            # If players want scores to be announced after every round, inform them of the current score.
            if self.prefManager.get_preference('AnnounceScoresAfterEachRound'):
                print("Your score is currently " + str(self.playerScore) + " and the "
                                                                           "keeper's score is currently " + str(
                    self.keeperScore) + ".")

        print()

        self.game_end()  # The round is finished; end the game.

    def game_end(self):

        # Output final scores.
        print("The game is over." + " You scored " + str(self.playerScore) + " and the keeper scored " + str(
            self.keeperScore) + ".")

        if self.playerScore > self.keeperScore:
            print("You won the game!")
        elif self.playerScore < self.keeperScore:
            print("You lost the game!")
        else:
            print("You drew with the keeper!")

        # Create a FinalScore and write it to the file.
        score = FinalScore(self.prefManager.get_preference('PlayerName'), self.playerScore, self.keeperScore,
                           datetime.now().strftime("%T %d-%b-%Y"))

        self.scoreHandler.write_score(score)

        print()
        print("Your results have been saved to the file. Returning to the main menu in 3 seconds...")
        time.sleep(3)
