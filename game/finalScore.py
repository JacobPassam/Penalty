class FinalScore:  # FinalScore class, representing the end result of a game.

    def __init__(self, playerName, playerScore, keeperScore, time):
        self.playerName = playerName  # PlayerName, as set in the user's preferences.
        self.playerScore = playerScore
        self.keeperScore = keeperScore
        self.time = time  # The time at which the game ended.

    # Returns a CSV-formatted string of the values in this object.
    def format(self):
        return self.playerName + "," + str(self.playerScore) + "," + str(self.keeperScore) + "," + str(self.time)
