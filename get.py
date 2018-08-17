# Functions used to obtain information from JSON files.

import json

# Function to return attributes.
# a = 'npc' or 'player' depending on whether the target is the playable character or an NPC.
# b = name of the character or NPC.
# c = name of the attribute.
def atr(a, b, c):
	if a == "player":
		character_filename = "save/" + b + ".json"
		with open(character_filename, 'r') as f:
			character_data = json.load(f)
			f.close()
		attribute = character_data["attributes"][c] + character_data["temp_attributes"][c] + character_data["item_attributes"][c]
		return attribute
	else:
		npc_filename = "npcs/" + b + ".json"
		with open(npc_filename, 'r') as f:
			npc_data = json.load(f)
			f.close()
		attribute = npc_data["attributes"][c] + npc_data["temp_attributes"][c] + npc_data["item_attributes"][c]
		return attribute

# Function to return real attributes.
# a = 'npc' or 'player' depending on whether the target is the playable character or an NPC.
# b = name of the character or NPC.
# c = name of the attribute.
def real_atr(a, b, c):
	if a == "player":
		character_filename = "save/" + b + ".json"
		with open(character_filename, 'r') as f:
			character_data = json.load(f)
			f.close()
		return character_data["attributes"][c]
	else:
		npc_filename = "npcs/" + b + ".json"
		with open(character_filename, 'r') as f:
			npc_data = json.load(f)
			f.close()
		return npc_data["attributes"][c]

# Function to return temporary attributes.
# a = 'npc' or 'player' depending on whether the target is the playable character or an NPC.
# b = name of the character or NPC.
# c = name of the temporary attribute.
def temp_atr(a, b, c):
	if a == "player":
		character_filename = "save/" + b + ".json"
		with open(character_filename, 'r') as f:
			character_data = json.load(f)
			f.close()
		return character_data["temp_attributes"][b]
	else:
		npc_filename = "npcs/" + b + ".json"
		with open(npc_filename, 'r') as f:
			npc_data = json.load(f)
			f.close()
		return npc_data["temp_attributes"][b]

# Function to return current level.
# a = 'npc' or 'player' depending on whether the target is the playable character or an NPC.
# b = name of the character or NPC.
def level(a, b):
	if a == "player":
		character_filename = "save/" + b + ".json"
		with open(character_filename, 'r') as f:
			character_data = json.load(f)
			f.close()
		return character_data["level"]
	else:
		npc_filename = "npcs/" + b + ".json"
		with open(npc_filename, 'r') as f:
			npc_data = json.load(f)
			f.close()
		return npc_data["level"]

# Function to return current health.
# a = 'npc' or 'player' depending on whether the target is the playable character or an NPC.
# b = name of the character or NPC.	
def health(a, b):
	if a == "player":
		character_filename = "save/" + b + ".json"
		with open(character_filename, 'r') as f:
			character_data = json.load(f)
			f.close()
		return character_data["current_health"]
	else:
		npc_filename = "npcs/" + b + ".json"
		with open(npc_filename, 'r') as f:
			npc_data = json.load(f)
			f.close()
		return npc_data["current_health"]

# Function to return current magic.
# a = 'npc' or 'player' depending on whether the target is the playable character or an NPC.
# b = name of the character or NPC.	
def magic(a, b):
	if a == "player":
		character_filename = "save/" + b + ".json"
		with open(character_filename, 'r') as f:
			character_data = json.load(f)
			f.close()
		return character_data["current_magic"]
	else:
		npc_filename = "npcs/" + b + ".json"
		with open(npc_filename, 'r') as f:
			npc_data = json.load(f)
			f.close()
		return npc_data["current_magic"]

# Function to return current experience.
# a = 'npc' or 'player' depending on whether the target is the playable character or an NPC.
# b = name of the character or NPC.	
def exp(a, b):
	if a == "player":
		character_filename = "save/" + b + ".json"
		with open(character_filename, 'r') as f:
			character_data = json.load(f)
			f.close()
		return character_data["progress"]["experience"]
	else:
		npc_filename = "npcs/" + b + ".json"
		with open(npc_filename, 'r') as f:
			npc_data = json.loaf(f)
			f.close()
		return npc_data["progress"]["experience"]

# Function to return current experience needed to gain a level.
# a = 'npc' or 'player' depending on whether the target is the playable character or an NPC.
# b = name of the character or NPC.	
def toexp(a, b):
	if a == "player":
		character_filename = "save/" + b + ".json"
		with open(character_filename, 'r') as f:
			character_data = json.load(f)
			f.close()
		return character_data["progress"]["experience_to_level"]
	else:
		npc_filename = "npcs/" + b + ".json"
		with open(npc_filename, 'r') as f:
			npc_data = json.loaf(f)
			f.close()
		return npc_data["progress"]["experience_to_level"]