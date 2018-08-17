# Work-in-progress text-based game.
# The idea is to build a game similar to the one I plan to build for IRC for practice.
# I can test ideas in this and improve my coding skills before I start taking it to the IRC RPG.
# I will probably put this up on Github in case anyone wants to mess around with it / test it / play it.
# I plan to at least have the game be playable, but probably at a shallow level.
# This will be shared on Github in case anyone wants to mess around with the code or make their own game from it.

# Necessary for clearing the screen and the save system. Will simplify this at a later date.
from os import system, name, walk, path

# For some reason I have to have this here... will investigate the cause at some point to reduce imports.
import os

import sys

# Used for save files and other configuration files.
import json
import get
import put
import common

# This function displays the main menu for the game. The user is able to start or load a game, view credits, edit game-wide settings, and exit the game from here.
def main_menu():
	common.clear_screen()
	print(" _____         _    ____________ _____ ")
	print("|_   _|       | |   | ___ \\ ___ \\  __ \\")
	print("  | | _____  _| |_  | |_/ / |_/ / |  \\/")
	print("  | |/ _ \\ \\/ / __| |    /|  __/| | __ ")
	print("  | |  __/>  <| |_  | |\\ \\| |   | |_\\ \\")
	print("  \\_/\\___/_/\\_\\\\__| \\_| \\_\\_|    \\____/")
	print("1. New Game")
	print("2. Load Game")
	print("3. Credits")
	print("4. Help")
	print("5. Exit Game")
	selection = input("> ")
	# As it turns out, Python lacks a switch-case system. Odd. If / elif / else it is then.
	if selection == "1":
		start_game()
	elif selection == "2":
		load_game()
	elif selection == "3":
		credits()
	elif selection == "4":
		game_help("start")
	elif selection == "5":
		common.clear_screen()
		sys.exit(0)
	elif selection == "318":
		secret_menu()
	else:
		print("Incorrect selection. Please choose one of the options.")
		print("Press any key to continue.")
		input("?")
		main_menu()

# Displays credits related to development of the game.
def credits():
	common.clear_screen()
	print("This \"game\" was made by Aesthemic.")
	print("Twitter: https://www.twitter.com/aesthemic")
	print("Discord: Aesthemic#0573")
	print("IRC: Aesthemic in #lounge on irc.digibase.ca")
	print("Email: aesthemic@digitalcyon.com")
	print("Press any key to continue.")
	input("?")
	main_menu()

# This function will display the in-game main menu. From here, they have a number of different options to progress the game.
def game_menu():
	common.clear_screen()
	print("Game Menu")
	global location_data
	with open("data/locations.json", 'r') as f:
		location_data = json.load(f)
	global shops_data
	with open("data/shops.json", 'r') as f:
		shops_data = json.load(f)
	curr_loc_id = character_data["travel"]
	curr_loc_nm = location_data[curr_loc_id]["text-name"]
	print("You're currently in " + str(curr_loc_nm) + ".")
	print("Select an Option")
	print("1. Travel")
	print("2. Explore")
	print("3. Shopping")
	print("4. Stats")
	print("5. Inventory")
	print("6. Help")
	print("7. Save Game")
	print("8. Exit Game")
	selection = input("> ")
	if selection == "1":
		travel_menu()
	elif selection == "2":
		explore()
	elif selection == "3":
		shop_menu()
	elif selection == "4":
		view_stats("player", character_data["character_name"])
	elif selection == "5":
		print("This game is still under construction.")
		print("Press any key to continue.")
		selection = input("> ")
		game_menu()
	elif selection == "6":
		game_help("game")
	elif selection == "7":
		save_game()
	elif selection == "8":
		main_menu()
	else:
		print("Incorrect selection. Please choose from one of the options.")
		print("Press any key to continue.")
		selection = input("> ")
		game_menu()

# Function to save the game to a JSON file. Files are stored in the 'save' folder.
def save_game():
	common.clear_screen()
	print(character_data["character_name"])
	character_name = character_data["character_name"]
	savename = "save/" + character_name + ".json"
	with open(savename, 'w') as f:
		json.dump(character_data, f)
	print("You successfully saved the game.")
	print("Press return to continue.")
	input("?")
	game_menu()

# Function to load the game from a JSON file. Files are stored in the 'save' folder.
def load_game():
	common.clear_screen()
	print("Please type the name of the save file you would like to load.")
	print("Save files:")
	global character_data
	for files in os.walk('save'):
		for filename in files:
			if ".json" in str(filename):
				print(str(filename)[2:-7])
	character_name = input("> ")
	character_filename = "save/" + character_name + ".json"
	with open(character_filename, 'r') as f:
		character_data = json.load(f)
	if character_data is None:
		print("Invalid character name. Please choose one from the list.")
		print("Press return to continue.")
		input("?")
		load_game() 
	print("Save loaded.")
	print("Press return to continue.")
	input("?")
	game_menu()

# This function starts the process of creating a new character.
def start_game():
	common.clear_screen()
	print("Welcome to the strange world of GameWars.")
	print("May I ask your name?")
	character_name = input("> ")
	print(f"Hello, {character_name}, it is a pleasure to meet you.")
	if len(character_name) > 20:
		print("Your name needs to be less than 20 characters. Please choose another name.")
		print("Press any key to continue.")
		input("?")
		start_game()
	else: 
		global character_data
		character_data = {"character_name":character_name,"level":1,"current_health":100,"current_magic":100,"attributes":{"health":100,"magic":100,"strength":10,"dexterity":10,"endurance":10,"agility":10,"intelligence":10,"spirit":10,"vitality":10,"luck":0},"temp_attributes":{"health":0,"magic":0,"strength":0,"dexterity":0,"endurance":0,"agility":0,"intelligence":0,"spirit":0,"vitality":0,"luck":0},"item_attributes":{"health":0,"magic":0,"strength":0,"dexterity":0,"endurance":0,"agility":0,"intelligence":0,"spirit":0,"vitality":0,"luck":0},"progress":{"exp":0,"exp_to_level":100},"currencies":{"gold":0,"honor":0},"items":{},"bank":{},"quests":{},"travel":"starting-village"}
		game_menu()

# Function to view the stats of either the playable character or an NPC.
# a = 'npc' or 'player' depending on whether the target is the playable character or an NPC.
# b = name of the character or NPC.
def view_stats(a, b):
	if a == "player":
		common.clear_screen()
		character_filename = "save/" + b + ".json"
		with open(character_filename, 'r') as f:
			character_data = json.load(f)
			f.close()
		print("Character stats for: " + character_data["character_name"])
		print("Basic Information:")
		print("Experience: " + str(get.exp(a, b)) + " \\ " + str(get.toexp(a, b)))
		print("Press enter to continue.")
		input("?")
		game_menu()
	else:
		common.clear_screen()
		npc_filename = "save/" + b + ".json"
		with open(npc_filename, 'r') as f:
			npc_data = json.load(f)
			f.close()
		print("Character stats for: " + npc_data["character_name"])
		print("Basic Information:")
		print("Experience: " + str(get.exp(a, b)) + " \\ " + str(get.toexp(a, b)))
		print("Press enter to continue.")
		input("?")
		game_menu()

# This function provides an in-game help menu for the player. To some extent, I feel like this could be improved upon. I'll have to look into a better way to handle the in-game help files.
def game_help(a):
	common.clear_screen()
	print("Help Menu")
	print("Which topic would you like help with?")
	print("1. How to Play")
	print("2. Menus")
	print("3. Attributes")
	print("4. Combat")
	print("5. Bug Report")
	print("Press return to return to previous menu.")
	selection = input("> ")
	if selection == "1":
		game_help_general(a)
	elif selection == "2":
		game_help_menues(a)
	elif selection == "3":
		game_help_attributes(a)
	elif selection == "4":
		game_help_combat(a)
	elif selection == "5":
		game_help_bug(a)
	else:
		if a == "game":
			game_menu()
		elif a == "combat":
			combat_menu()
		elif a == "start":
			main_menu()
		else:
			main_menu()


# This help screen gives the player information on what the game is about and how to play.
def game_help_general(a):
	common.clear_screen()
	print("The main objective of the game is to explore the world and defeat the four major bosses.")
	print("Over the course of the game you'll recruit new characters to help you, find new gear, and complete quests to unlock new abilities.")
	print("Press return to continue.")
	input("?")
	game_help(a)

# This help screen explains what all of the primary menus do.
def game_help_menus(a):
	common.clear_screen()
	print("This help menu is coming soon.")
	print("Press return to continue.")
	input("?")
	game_help(a)

# This help screen gives the player information on what the different attributes in the game do.
def game_help_attributes(a):
	common.clear_screen()
	print("Health: This is how much damage you can take before your character dies.")
	print("Magic: This is how much magic you can use. Spells in the game take magic to cast.")
	print("Strength: This influences how much damage you deal with physical attacks. The higher the strength, the more damage you deal.")
	print("Dexterity: This determines your chance to hit an enemy. The higher the dexterity, the better the chance to hit.")
	print("Endurance: This determines how much physical damage you can absorb. The higher the endurance, the less damage you take from physical attacks.")
	print("Agility: This determines your chance to dodge an incoming attack. The higher the agility, the better the chance that a physical attack will miss you.")
	print("Intelligence: This determines how powerful your attack spells are. The higher the intelligence, the more potent your attack spells are.")
	print("Spirit: This determines how much magic you receive when you level up. Increase this to improve your health.")
	print("Vitality: This determines how much health you receive when you level up. Increase this to improve your magic.")
	print("Luck: This determines your chance for lucky things to happen. Don't think too much about it. :)")
	print("Press return to continue.")
	input("?")
	game_help(a)

# This help screen gives the player information on what combat is like.
def game_help_combat(a):
	common.clear_screen()
	print("This menu is under construction since the combat system is under construction.")
	print("Press return to continue.")
	input("?")
	game_help(a)

# This help screen gives the player information on how to file a bug report.
def game_help_bug(a):
	common.clear_screen()
	print("If you've run into a bug, please send an email to aesthemic@inpixelit.com.")
	print("Thank you for helping with testing the game.")
	print("Press return to continue.")
	input("?")
	game_help(a)

# :)
def secret_menu():
	common.clear_screen()
	print("Welcome to the secret menu! This doesn't do anything right now, but feel free to make yourself at home.")
	print("Press return to go back to the main menu.")
	input("?")
	main_menu()

# Function used to allow players to travel to new areas.
def travel_menu():
	common.clear_screen()
	curr_loc_id = character_data["travel"]
	curr_loc_nm = location_data[curr_loc_id]["text-name"]
	travel_to = location_data[curr_loc_id]["travel"]
	print("You're currently in " + curr_loc_nm + ".")
	print("Where would you like to go?")
	for key in travel_to:
		print(location_data[key]["text-name"] + " - Level: " +  str(location_data[key]["area-level"]))
	print("Type the name of the area you would like to go.")
	print("If you change your mind, simply type nothing and hit return.")
	selection = input("> ")
	selection = selection.lower()
	selection = selection.replace(" ", "-")
	if selection in location_data[curr_loc_id]["travel"]:
		character_data["travel"] = selection
		common.clear_screen()
		print("You have successfully traveled to " + location_data[selection]["text-name"] + ".")
		print("Press return to continue.")
		input("?")
		game_menu()
	else:
		common.clear_screen()
		print("Invalid selection.")
		print("Press return to continue.")
		input("?")
		game_menu()

# Function used to allow players to explore the area they are in.
def explore():
	common.clear_screen()
	curr_loc_id = character_data["travel"]
	if location_data[curr_loc_id]["explore"] == 0:
		print("You explore the area, yet find nothing. It seems there isn't much to see here. Try traveling somewhere else.")
		print("Press return to continue.")
		input("?")
		game_menu()
	else:
		print("This part of the game is currently under construction.")
		print("Press return to continue.")
		input("?")
		game_menu()

# Function used to allow players to buy from shops and sell items. I feel like this could be simplified. I'll look into it at some point, but it works for now. I think.
def shop_menu():
	common.clear_screen()
	curr_loc_id = character_data["travel"]
	if not location_data[curr_loc_id]["shops"]:
		print("There are no shops here to find.")
		print("Try visiting a town or village.")
		print("Press return to continue.")
		input("?")
		game_menu()
	else:
		print("Please choose from the following shops by number.")
		shop_number = 1
		for shops in location_data[curr_loc_id]["shops"]:
			print(str(shop_number) + ". " + shops_data[shops]["text-name"])
			shop_number = shop_number + 1
		selection = input("> ")
		if selection.isdigit() == False:
			common.clear_screen()
			print("Your selection should be a number.")
			print("Example: 1")
			print("Press return to continue.")
			input("?")
			shop_menu()
		selection = int(selection)
		all_shops = location_data[curr_loc_id]["shops"]
		shop_names = all_shops.keys()
		shop_number = len(all_shops.keys())
		if selection < 1:
			print("You've selected an invalid shop.")
			print("Press return to continue.")
			input("?")
			shop_menu()
		if selection <= shop_number:
			selection = selection - 1
			selection = list(shop_names)[selection]
			go_shop(selection)
		else:
			common.clear_screen()
			print("You've selected an invalid shop.")
			print("Press return to continue.")
			input("?")
			shop_menu()

# Function to enable players to buy and sell items from a shop.
def go_shop(id):
	common.clear_screen()

# Have to actually invoke the main menu for it to show up.
main_menu()