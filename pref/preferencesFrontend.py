from util import menuUtil
from pref.preferencesManager import PreferencesManager

MENU_OPTIONS = ["View your preferences", "Edit a preference",
                "Return to main menu"]  # Constant representing preference menu options.


# Method to output the preferences menu.
def do_menu(prefManager: PreferencesManager):
    while True:  # Loop infinitely until the user chooses to return to the Main Menu.
        menuUtil.send_menu(MENU_OPTIONS)
        opt = menuUtil.receive_option(len(MENU_OPTIONS))  # Receive validated menu option.

        if opt == 1:
            # View your preferences

            prefs = prefManager.get_preferences()

            print()
            print('Showing your preferences:')
            print()
            for key, value in prefs.items():
                print(key + ": " + str(value))
            print()

        elif opt == 2:

            name = input('Enter the name of the preference you wish to edit: ')
            if name not in prefManager.prefMap:
                print('That is not a valid preference name.')
                print()
            else:
                valid = False
                value = input('Enter the value you wish to set (or -1 to exit): ')

                while not valid:  # Loop until the value inputted is valid.
                    if str(value) != "-1":
                        # Get the (casted?) value and the needed type for that preference from check_type().
                        value, pref_type = prefManager.check_type(name, value)

                        if pref_type is None: # This shouldn't happen, but you never know.
                            print('Error whilst finding type of preference?')
                            exit(1)
                        else:

                            # The value could not be successfully changed into the needed type.
                            if value is None:
                                value = input(
                                    'The value should be of type ' + pref_type.__name__ + ". Please try again: ")
                            else:
                                # The value is valid! Update the preference and inform the user.

                                valid = True
                                prefManager.set_preference(name, value)
                                print('You set the value of ' + name + ' to ' + str(value) + ".")
                                print()
                    else:
                        # -1; exit and re-print the preferences menu.

                        print()
                        break

        elif opt == 3:
            # Return to Main Menu. Break from the loop and allow main to re-output the Main Menu.

            break
