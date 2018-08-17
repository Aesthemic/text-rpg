# Common functions are placed here.

from os import system, name

# This function clears the screen in the terminal. Should work on Windows, Linux, and Mac systems using this logic.
def clear_screen():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')