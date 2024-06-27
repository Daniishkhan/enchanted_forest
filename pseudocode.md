# Import necessary modules (json, random, etc.)

# Define Room class
Class Room:
    Initialize with name, description, exits (dictionary), items (list)
    Method to add exit
    Method to add item
    Method to remove item

# Define Item class
Class Item:
    Initialize with name, description
    Method to use item (can be overridden in subclasses)

# Define Player class
Class Player:
    Initialize with name, inventory (list), current_room
    Method to add item to inventory
    Method to remove item from inventory
    Method to move to a new room

# Define Game class
Class Game:
    Initialize with rooms (dictionary), player, game_over (boolean)

    Method load_game(filename):
        Load game data from JSON file
        Create rooms, items, and set up initial game state

    Method save_game(filename):
        Convert current game state to JSON
        Save to file

    Method create_player(name):
        Create new Player object
        Set starting room

    Method display_current_room():
        Print current room name, description, available exits, and visible items

    Method get_user_input():
        Prompt user for input
        Convert to lowercase and return

    Method process_command(command):
        Split command into words
        If first word is:
            "go" or "move": attempt to move player
            "look" or "examine": provide details about room or specific item
            "take" or "pick": attempt to take item
            "drop": attempt to drop item
            "use": attempt to use item
            "inventory": display player's inventory
            "save": save game
            "load": load game
            "quit" or "exit": set game_over to True
            "help": display available commands
        Else: print "I don't understand that command"

    Method play():
        While not game_over:
            Display current room
            Get user input
            Process command
        Print farewell message

# Main function
Function main():
    Create Game object
    Load initial game data
    Get player name
    Create player
    Start game loop (call play method)

# Run main function if this is the main script
If this is the main script:
    Call main()