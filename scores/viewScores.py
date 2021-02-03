from data.scoresFile import ScoresFileHandler


# Utility method to view recorded scores.
def view_all_scores(handler: ScoresFileHandler):
    scores = handler.read_all_scores()

    if len(scores) == 0:
        print('There are no scores to be displayed. Play a game first!')

    for score in scores:
        print(
            score.playerName + " scored " + score.playerScore + " and the keeper scored " + score.keeperScore + " at " + str(
                score.time))
