# Functions used to write data to JSON files.

import json

# Function to write attributes.
# a = 'npc' or 'player' depending on whether the target is the playable character or an NPC.
# b = name of the character or NPC.
# c = name of the attribute being written
# d = value of that attribute
def atr(a, b, c, d):
	if a == "player":
		character_filename = "save/" + b + ".json"
		with open(character_filename, 'r') as f:
			character_data = json.load(f)
		character_data["attributes"][c] = d
		character_filename.close()
	else:
		npc_filename = "npcs/" + b + ".json"
		with open(npc_filename, 'w') as f:
			npc_data = json.load(f)
		npc_data["attributes"][c] = d
		npc_filename.close()

# Function used to write current health value.
# a = 'npc' or 'player' depending on whether the target is the playable character or an NPC.
def health(a, b, c):
	if a == "player":
		character_filename = "save/" + b + ".json"
		with open(character_filename, 'r') as f:
			character_data = json.load(f)
		character_data["current_health"] = c
		character_filename.close()
	else:
		npc_filename = "npcs/" + b + ".json"
		with open(npc_filename, 'w') as f:
			npc_data = json.load(f)
		npc_data["current_health"] = c
		npc_filename.close()

# Function used to write current magic value.
# a = 'npc' or 'player' depending on whether the target is the playable character or an NPC.
def magic(a, b, c):
	if a == "player":
		character_filename = "save/" + b + ".json"
		with open(character_filename, 'r') as f:
			character_data = json.load(f)
		character_data["current_magic"] = c
		character_filename.close()
	else:
		npc_filename = "npcs/" + b + ".json"
		with open(npc_filename, 'w') as f:
			npc_data = json.load(f)
		npc_data["current_magic"] = c
		npc_filename.close()