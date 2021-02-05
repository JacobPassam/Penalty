from util import menuUtil
from instructions import instructions
from pref import preferencesFrontend
from scores import scoresMenu
from game.game import Game

MENU_OPTIONS = ["Play the Game", "See instructions", "Edit your preferences", "View scores data",
                "Exit"]  # Constant representing main menu options.


# Method to output the main menu. Loop is controlled by main.
def do_menu(prefManager, scoresFile):
    menuUtil.send_menu(MENU_OPTIONS)
    option = menuUtil.receive_option(len(MENU_OPTIONS))  # Receive validated menu option.

    print()
    if option == 1:
        # Play the Game
        game = Game(prefManager, scoresFile)
        game.play()

    elif option == 2:
        # See instructions
        instructions.send_instructions()

    elif option == 3:
        # Edit your preferences
        preferencesFrontend.do_menu(prefManager)

    elif option == 4:
        # View scores data
        scoresMenu.do_menu(scoresFile)

    elif option == 5:
        # Exit
        print('Bye!')

        exit()

    print()
