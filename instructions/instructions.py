# Utility method to output game instructions.
def send_instructions():
    print('Instructions for penalty shootout:')
    print(' - You will play a variable number of rounds of this game. (5 by default)')
    print(' - In each round, you decide a direction to kick the ball.')
    print(' - If the goalkeeper saves your shot by diving in the same direction, you have lost that round.')
    print(' - If your ball does not get saved, you have won and you get one point.')
    print(' - After all rounds are completed, the game ends. Your scores are saved and the winner is announced.')
