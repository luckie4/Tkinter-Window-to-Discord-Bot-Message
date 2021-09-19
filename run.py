# This script permanantly keeps the other two scripts running.
# As there is an exit() function in the the discord bot script, it must be rerun through a terminal window, hence the os import.

import os

while True:
    os.system("python3 tkinter_window.py") # Can be replaced with "python 'name of run file'"
    
