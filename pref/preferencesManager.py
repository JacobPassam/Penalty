import json

PREFERENCES_FILE_PATH = 'run/preferences.dat'  # Constant for preferences file.


class PreferencesManager:

    def __init__(self):

        # Set default preferences
        self.prefMap = {
            "PlayerName": "Name not set",
            "Rounds": 5,
            "AnnounceScoresAfterEachRound": True
        }

    def load_preferences(self):
        # Load preferences from file into prefMap or create the default file and preferences.

        try:
            f = open(PREFERENCES_FILE_PATH)
            self.prefMap = json.loads(f.read())
        except FileNotFoundError:
            self.__write_preferences()

    def __write_preferences(self):
        # 'Private' method. Write the current prefMap object into the file.

        f = open(PREFERENCES_FILE_PATH, 'w')

        f.write(json.dumps(self.prefMap))
        f.close()

    def set_preference(self, pref_id, value):
        # Set preference to a value and write to file.

        self.prefMap[pref_id] = value
        self.__write_preferences()

    def get_preferences(self):
        # Returns all preferences.

        return self.prefMap

    def get_preference(self, pref):
        # Get a certain preference.

        return self.prefMap[pref]

    def check_type(self, pref, value):
        # Value type checking for a user editing their preferences.
        # For example, an integer field such as 'Rounds' should not be able to accept a
        # string as its input. This method checks the type of 'value' and, if necessary, casts them
        # to the correct type.
        #
        # Returns the casted value and the type that is needed.

        if pref not in self.prefMap:  # If, for some reason, an invalid preference name is provided within the code.
            return

        # Gets the (correct) current type of the value inside prefMap for comparison with the type
        # of the value provided.
        current_type = type(self.prefMap[pref])

        # If the value is already an instance of the needed type, return the value back as it is. No casting is needed.
        if isinstance(value, current_type):
            return value, current_type

        if current_type == int:
            # Special handling for integers. Attempt to cast the provided value to an integer.

            try:
                return int(value), current_type
            except ValueError:
                return None, current_type  # Return None, as the provided value was not successfully cast to an integer.
        elif current_type == bool:
            # Special handling for booleans. Attempt to figure out what the user wants - True or False.
            # Boolean True can be provided as strings "true" or "yes", and Boolean False as "false" or "no".

            true = value.lower() == "true" or value.lower() == "yes"
            false = value.lower() == "false" or value.lower() == "no"

            if true:
                return True, current_type
            elif false:
                return False, current_type
            else:
                return None, current_type # Return None, as the provided value was not successfully cast to a boolean.
