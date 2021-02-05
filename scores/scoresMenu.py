from util import menuUtil
from scores import viewScores
from data.scoresFile import ScoresFileHandler

MENU_OPTIONS = ["Unordered",
                "Ordered by player score",
                "Ordered by keeper score",
                "Return to main menu"]

ASC_DEC_OPTIONS = ["Ascending", "Descending"]


# Show menu for displaying scores.
def do_menu(scoresHandler: ScoresFileHandler):
    while True:  # Loop infinitely until the user chooses to 'Return to main menu'.
        menuUtil.send_menu(MENU_OPTIONS)
        opt = menuUtil.receive_option(len(MENU_OPTIONS))

        if opt == 1:
            # View all scores, unordered

            print()
            viewScores.view_all_scores(scoresHandler)
            print()
        elif opt == 2:
            # Ordered by player score.

            print()
            menuUtil.send_menu(ASC_DEC_OPTIONS)
            order_opt = menuUtil.receive_option(len(ASC_DEC_OPTIONS))

            print()

            # Show sorted scores.
            viewScores.view_sorted_scores(scoresHandler, False,
                                          order_opt == 2)  # NOT by keeper and if user chose Option #2 (descending)
            print()
        elif opt == 3:
            # Ordered by player score.

            print()
            menuUtil.send_menu(ASC_DEC_OPTIONS)
            order_opt = menuUtil.receive_option(len(ASC_DEC_OPTIONS))

            print()

            # Show sorted scores.
            viewScores.view_sorted_scores(scoresHandler, True,
                                          order_opt == 2)  # YES by keeper and if user chose Option #2 (descending)
            print()
        elif opt == 4:
            # Return to main menu

            break
