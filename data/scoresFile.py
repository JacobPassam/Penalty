from game.finalScore import FinalScore

SCORES_FILE_PATH = 'run/scores.csv'  # Constant for scores file.


class ScoresFileHandler:

    def __init__(self):
        # Create file, if doesn't exist.
        try:
            f = open(SCORES_FILE_PATH, 'x')
            f.close()
        except FileExistsError:
            pass

    # Writes a given FinalScore object to the file.
    def write_score(self, final_score):
        f = open(SCORES_FILE_PATH, 'a')

        f.write(final_score.format() + "\n")
        f.close()

    # Reads all scores in the file and parses them into an array of FinalScore objects.
    # Returns an array of FinalScore objects.
    def read_all_scores(self):
        # Initialise scores array.
        scores = []

        # Loop through lines in file and parse into a FinalScore.
        f = open(SCORES_FILE_PATH, 'r')
        for line in f:
            data = line.replace("\n", "").split(",")
            scores.append(FinalScore(data[0], data[1], data[2], data[3]))

        f.close()

        return scores
