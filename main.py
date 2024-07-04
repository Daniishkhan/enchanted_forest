"""
# The Enchanted Forest

## Setting
The game takes place in a mysterious, magical forest. The player finds themselves at the edge of this forest, tasked with finding a legendary artifact hidden deep within its depths.

## Objective
The main goal is to navigate through the forest, solve puzzles, collect items, and ultimately find the "Crystal of Eternity" - a powerful magical artifact.
"""
import json

class Map:
    def __init__(self, rooms: list[Room]):
        self.rooms = rooms

class Room:
    """
    A room in the game.
    """
    def __init__(self, name, description, exits, items):
       self.name = name
       self.description = description
       self.exits = exits
       self.items = items
       
    def add_exit(self, direction, room):
       self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Players:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    
    # Method to use item (can be overridden in subclasses)
    def use_item(self, item): 
        print(f"{self.name} uses {item.name}")
        self.remove_item(item)
        
class Game: 
    def __init__(self, player: str, inventory: list[Item], current_room: Room):
        self.player = player
        self.inventory = inventory
        self.current_room = current_room
    
    def load_game(self, file_path: str):
        #load game from json file
        # Create rooms, items, and set up initial game state
        with open(file_path, "r") as file:
            data = json.load(file)
            self.player = data["player"]
            self.inventory = data["inventory"]
            self.current_room = data["current_room"]

def main():
    pass

if __name__ == "__main__":
    main()