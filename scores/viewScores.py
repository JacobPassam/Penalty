from data.scoresFile import ScoresFileHandler


# Utility method to view recorded scores.
def view_all_scores(handler: ScoresFileHandler):
    scores = handler.read_all_scores()

    if len(scores) == 0:
        print('There are no scores to be displayed. Play a game first!')

    # Show unordered (in the order they were added to the file)
    for score in scores:
        print(
            score.playerName + " scored " + score.playerScore + " and the keeper scored " + score.keeperScore + " at " + str(
                score.time))


def view_sorted_scores(handler: ScoresFileHandler, keeper: bool, descending: bool):
    scores = handler.read_all_scores()

    if len(scores) == 0:
        print('There are no scores to be displayed. Play a game first!')

    scores = sorted(scores,

                    # If keeper is True (user wants sorted by keeper scores) then use finalScore.keeperScore,
                    # else use the player score.
                    key=lambda sc: sc.keeperScore if keeper else sc.playerScore,

                    reverse=descending)  # Whether or not the user chose the descending format, provided as a parameter

    for score in scores:
        print(
            score.playerName + " scored " + score.playerScore + " and the keeper scored " + score.keeperScore + " at " + str(
                score.time))
