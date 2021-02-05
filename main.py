import pathlib
from menu import mainMenu
from pref.preferencesManager import PreferencesManager
from data.scoresFile import ScoresFileHandler

print("Hello. Welcome to Penalty Shootout.")
print()

# Make run/ configuration directory if it doesn't exist.
pathlib.Path('run').mkdir(exist_ok=True)

# Load preferences manager
prefManager = PreferencesManager()
prefManager.load_preferences()

# Load scores file manager
scoresFile = ScoresFileHandler()

# Infinitely display the main menu until the user quits. (Option 5 or Ctrl+C)
while True:
    mainMenu.do_menu(prefManager, scoresFile)
