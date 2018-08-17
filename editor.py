# This tool is used to edit data and save files.
# This tool will be developed alongside the game.

from os import system, name

import sys

# This function clears the screen in the terminal. Should work on Windows, Linux, and Mac systems using this logic.
def clear_screen():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

# Main menu for the editor. Allows the user to access another editor.
def main_menu():
	clear_screen()
	print(" _____         _    ____________ _____ ")
	print("|_   _|       | |   | ___ \\ ___ \\  __ \\")
	print("  | | _____  _| |_  | |_/ / |_/ / |  \\/")
	print("  | |/ _ \\ \\/ / __| |    /|  __/| | __ ")
	print("  | |  __/>  <| |_  | |\\ \\| |   | |_\\ \\")
	print("  \\_/\\___/_/\\_\\\\__| \\_| \\_\\_|    \\____/\n\n")
	print("Select Your Editor:")
	print("1. Location Editor")
	print("2. Item Editor")
	print("3. Encounter Editor")
	print("4. NPC Editor")
	print("5. Skill Editor")
	print("6. Shop Editor")
	print("0. Exit Program")
	selection = input("> ")
	if selection == 1:
		loc_edit()
	elif selection == 2:
		itm_edit()
	elif selection == 3:
		enc_edit()
	elif selection == 4:
		npc_edit()
	elif selection == 5:
		skl_edit()
	elif selection == 6:
		shp_edit()
	else:
		sys.exit()

# Location editor. Enables the user to add, edit, and remove locations from the game.
# Can edit specifics about each location to connect it to other areas, encounters, etc.
def loc_edit():
	clear_screen()
	print("Location Editor")
	print("What would you like to do?")
	print("1. Create a Location")
	print("2. Edit a Location")
	print("3. Remove a Location")
	print("4. Link a Location")
	selection = input("> ")
	if selection == 1:
		clear_screen()
		print("What is the textual name of the location?")
		print("Example: Test Village")
		print("Leave blank to cancel.")
		textual_name = input("> ")
		if textual_name == None:
			loc_edit()
		clear_screen()
		print("What is the canonical name of the location?")
		print("Example: test-village")
		canonical_name = input("> ")
		if canonical_name == None:
			loc_edit()
		clear_screen()
		print("Will this area have random encounters?")
		print("Type '1' for Yes and '0' for No.")
		print("Leave blank to cancel.")
		encounter = input("> ")
		if encounter != 1 or encounter != 0:
			loc_edit()
		clear_screen()

	main_menu()

# Item editor. Enables the user to add, edit, and remove items from the game.
# Can edit specifics about each item.
def itm_edit():
	clear_screen()
	print("This is still under construction.")
	print("Press return to continue.")
	input("?")
	main_menu()

# Encounter editor. Enables the user to add, edit, and remove encounters from the game.
# Can edit specifics about an encounter and connect it to a different location.
def enc_edit():
	clear_screen()
	print("This is still under construction.")
	print("Press return to continue.")
	input("?")
	main_menu()

# NPC editor. Enables the user to add, edit, and remove NPCs from the game.
# Can edit specifics about the NPC including drop-rates.
def npc_edit():
	clear_screen()
	print("This is still under construction.")
	print("Press return to continue.")
	input("?")
	main_menu()

# Skill editor. Enables the user to add, edit, and remove skills from the game.
# Can edit the logic of the skills, values, etc.
def skl_edit():
	clear_screen()
	print("This is still under construction.")
	print("Press return to continue.")
	input("?")
	main_menu()

main_menu()