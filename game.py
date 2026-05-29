import time
import random
import os

def clear():
    os.system('clear')

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

player = {
    "name": "",
    "health": 100,
    "inventory": [],
    "location": "entrance",
}

rooms = {
    "entrance": {
        "desc": "you're standing in the entrance of an abandoned building. dust floats in the dim light. there are doors to the NORTH and EAST.",
        "exits": {"north": "hallway", "east": "office"},
        "items": ["flashlight"],
    },
    "hallway": {
        "desc": "a long dark hallway stretches before you. something skitters in the walls. there's a door to the SOUTH and WEST.",
        "exits": {"south": "entrance", "west": "basement"},
        "items": ["key"],
    },
    "office": {
        "desc": "an old office. papers everywhere. a desk sits in the corner. exits: WEST.",
        "exits": {"west": "entrance"},
        "items": ["note"],
    },
    "basement": {
        "desc": "the basement. it smells like rust and old water. there's a locked door to the NORTH and stairs back EAST.",
        "exits": {"east": "hallway", "north": "exit"},
        "items": [],
        "locked": True,
    },
    "exit": {
        "desc": "you burst through the door into the cold night air. you escaped.",
        "exits": {},
        "items": [],
        "ending": True,
    }
}

item_descriptions = {
    "flashlight": "an old flashlight. the batteries still work.",
    "key": "a rusty key. it might open something.",
    "note": "a crumpled note that reads: 'the key is in the hallway. get out before dark.'",
}

def look():
    room = rooms[player["location"]]
    slow_print(f"\n[ {player['location'].upper()} ]")
    slow_print(room["desc"])
    if room["items"]:
        slow_print(f"\nyou see: {', '.join(room['items'])}")
    slow_print(f"health: {player['health']} | inventory: {player['inventory'] if player['inventory'] else 'empty'}")

def go(direction):
    room = rooms[player["location"]]
    if direction in room["exits"]:
        dest = room["exits"][direction]
        dest_room = rooms[dest]
        if dest_room.get("locked"):
            if "key" in player["inventory"]:
                slow_print("\nyou use the key to unlock the door...")
                dest_room["locked"] = False
                player["location"] = dest
                look()
            else:
                slow_print("\nthe door is locked. you need a key.")
        else:
            player["location"] = dest
            if dest_room.get("ending"):
                clear()
                slow_print("\n" + "="*40)
                slow_print("YOU ESCAPED.")
                slow_print("="*40)
                slow_print(f"\nwell done, {player['name']}.")
                return True
            look()
    else:
        slow_print("\nyou can't go that way.")
    return False

def take(item):
    room = rooms[player["location"]]
    if item in room["items"]:
        player["inventory"].append(item)
        room["items"].remove(item)
        slow_print(f"\npicked up: {item}")
        if item == "flashlight":
            slow_print("you feel a little safer.")
    else:
        slow_print(f"\nthere's no {item} here.")

def examine(item):
    if item in player["inventory"] or item in rooms[player["location"]]["items"]:
        slow_print(f"\n{item_descriptions.get(item, 'nothing special about it.')}")
    else:
        slow_print(f"\nyou don't see any {item}.")

# intro
clear()
slow_print("="*40, 0.01)
slow_print("  ABANDONED", 0.05)
slow_print("  a text adventure", 0.05)
slow_print("="*40, 0.01)
player["name"] = input("\nwhat's your name, stranger? ")
slow_print(f"\ngood luck, {player['name']}. you're going to need it.")
time.sleep(1)
clear()
look()

# game loop
while True:
    cmd = input("\n> ").lower().strip().split()
    if not cmd:
        continue
    
    action = cmd[0]
    arg = cmd[1] if len(cmd) > 1 else ""

    if action in ["go", "move", "walk"] and arg:
        if go(arg):
            break
    elif action in ["look", "l"]:
        look()
    elif action in ["take", "grab", "pick"] and arg:
        take(arg)
    elif action in ["examine", "inspect", "read"] and arg:
        examine(arg)
    elif action in ["inventory", "inv", "i"]:
        slow_print(f"\ninventory: {player['inventory'] if player['inventory'] else 'empty'}")
    elif action in ["quit", "exit", "q"]:
        slow_print("\nyou give up and walk away.")
        break
    elif action == "help":
        slow_print("\ncommands: go [direction], look, take [item], examine [item], inventory, quit")
    else:
        slow_print("\nhuh?")
