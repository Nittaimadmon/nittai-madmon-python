"""
TEXT-BASED ADVENTURE GAME PROJECT
==================================

Student Name: [YOUR NAME HERE]
Game Title: [YOUR GAME NAME]
Game Theme: [e.g., Castle Adventure, Space Escape, Haunted House]

PROJECT GOAL:
Build a text-based game where players explore locations, collect items, 
and try to reach a goal (find treasure, escape, solve mystery, etc.)

WHAT YOU NEED TO BUILD:
✓ At least 5 different locations
✓ At least 5 items to collect
✓ Player can move between locations
✓ Player can pick up items
✓ A way to win the game
✓ At least 5 functions

TIME: 3 lessons to complete
"""

# =============================================================================
# UNDERSTANDING DICTIONARIES (Brief Review)
# =============================================================================

"""
WHAT IS A DICTIONARY?
A dictionary stores information using KEY-VALUE pairs.
Think of it like a real dictionary: you look up a WORD (key) to find its DEFINITION (value).

SYNTAX:
my_dict = {
    "key1": "value1",
    "key2": "value2"
}

EXAMPLE - Storing information about a person:
person = {
    "name": "David",
    "age": 15,
    "city": "Tel Aviv"
}

# Access values using keys:
print(person["name"])    # Prints: David
print(person["age"])     # Prints: 15

NESTED DICTIONARIES:
You can put dictionaries inside dictionaries!

locations = {
    "forest": {
        "description": "A dark forest",
        "items": ["sword", "key"]
    },
    "cave": {
        "description": "A mysterious cave",
        "items": ["treasure"]
    }
}

# Access nested values:
print(locations["forest"]["description"])  # Prints: A dark forest
print(locations["forest"]["items"])        # Prints: ['sword', 'key']
"""

# =============================================================================
# STEP 1: DESIGN YOUR GAME WORLD
# =============================================================================

"""
TODO: Create a dictionary of locations for your game

STRUCTURE:
locations = {
    "location_name": {
        "description": "What the player sees",
        "exits": {"direction": "location_name"},
        "items": ["item1", "item2"]
    }
}

EXAMPLE:
locations = {
    "entrance": {
        "description": "You stand at a large wooden door",
        "exits": {"north": "hallway"},
        "items": []
    },
    "hallway": {
        "description": "A long dark hallway",
        "exits": {"south": "entrance", "east": "kitchen"},
        "items": ["key"]
    }
}

TIPS:
- Create 5-7 locations minimum
- Connect them with exits (north, south, east, west)
- Put items in some locations
- Make sure all locations are reachable
- One location should have the "winning item" (treasure, exit key, etc.)
"""

# TODO: Create your locations dictionary here
locations = {
    # Add your locations here!
}


# =============================================================================
# STEP 2: HELPER FUNCTIONS
# =============================================================================

"""
Helper functions are small functions that do simple tasks.
They make your code cleaner and easier to read.
"""

# TODO: Write a function that prints a decorative line
# Function name: print_separator
# What it does: Prints something like "=========================================="
# Parameters: none
# Returns: nothing (just prints)

def print_separator():
    # TODO: Write your code here
    pass


# TODO: Write a function that shows available commands
# Function name: show_commands
# What it does: Prints a list of commands player can use
# Commands should include: look, go, take, inventory, quit
# Parameters: none
# Returns: nothing (just prints)

def show_commands():
    # TODO: Write your code here
    pass


# =============================================================================
# STEP 3: GAME DISPLAY FUNCTIONS
# =============================================================================

"""
These functions show information to the player.
"""

# TODO: Write a function that shows the game introduction
# Function name: show_intro
# What it does: 
#   - Welcomes player to your game
#   - Explains the story/goal
#   - Tells player what they need to do to win
# Parameters: none
# Returns: nothing (just prints)

def show_intro():
    # TODO: Write your code here
    # Use print() to show your story
    # Use print_separator() to make it look nice
    pass


# TODO: Write a function that displays current location
# Function name: show_location
# What it does:
#   - Shows location name
#   - Shows location description
#   - Shows available exits
#   - Shows items in the location
# Parameters: current_location (string), locations (dictionary)
# Returns: nothing (just prints)
#
# HINT: Use locations[current_location] to get location info
# HINT: Use locations[current_location]["description"] to get description

def show_location(current_location, locations):
    # TODO: Get the location dictionary from locations
    # TODO: Print the location name
    # TODO: Print the description
    # TODO: Print available exits
    # TODO: Print items in this location (if any)
    pass


# TODO: Write a function that shows player's inventory
# Function name: show_inventory
# What it does: Prints all items the player is carrying
# Parameters: inventory (list)
# Returns: nothing (just prints)
#
# HINT: Check if inventory is empty first
# HINT: Use a for loop to print each item, OR just print the list

def show_inventory(inventory):
    # TODO: Check if inventory is empty
    # TODO: If empty, print "Your inventory is empty"
    # TODO: If not empty, print all items
    pass


# =============================================================================
# STEP 4: GAME ACTION FUNCTIONS
# =============================================================================

"""
These functions handle player actions.
"""

# TODO: Write a function that handles picking up items
# Function name: take_item
# What it does:
#   1. Check if item exists in current location
#   2. If yes: remove from location, add to inventory, print success
#   3. If no: print error message
# Parameters: current_location (string), item_name (string), 
#             inventory (list), locations (dictionary)
# Returns: nothing
#
# HINT: Use "if item_name in locations[current_location]['items']:"
# HINT: Use .remove() to remove from location
# HINT: Use .append() to add to inventory

def take_item(current_location, item_name, inventory, locations):
    # TODO: Check if item exists in this location
    # TODO: If yes, move it from location to inventory
    # TODO: Print appropriate message
    pass


# TODO: Write a function that handles movement
# Function name: go_direction
# What it does:
#   1. Check if direction is valid from current location
#   2. If yes: return the new location
#   3. If no: print error and return current location
# Parameters: current_location (string), direction (string), 
#             locations (dictionary)
# Returns: new location (string)
#
# HINT: Check if direction exists in locations[current_location]["exits"]
# HINT: If yes, return locations[current_location]["exits"][direction]

def go_direction(current_location, direction, locations):
    # TODO: Check if direction is valid
    # TODO: If valid, return new location
    # TODO: If not valid, print error and return current location
    pass


# TODO: Write a function that checks if player won
# Function name: check_win
# What it does: Checks if player has the winning item(s)
# Parameters: inventory (list)
# Returns: True if won, False if not
#
# EXAMPLE: If winning item is "treasure"
# return "treasure" in inventory

def check_win(inventory):
    # TODO: Decide what item(s) player needs to win
    # TODO: Check if player has it
    # TODO: Return True or False
    pass


# =============================================================================
# STEP 5: MAIN GAME LOOP
# =============================================================================

"""
This is the heart of your game!
The main loop keeps running until player quits or wins.

STRUCTURE:
1. Setup (create starting variables)
2. Show intro
3. Loop:
   - Show location
   - Get command from player
   - Process command (go, take, look, etc.)
   - Check if won
4. Show end message
"""

def play_game():
    """Main game function"""
    
    # TODO: Setup game variables
    # - current_location = "start" (or whatever your first location is)
    # - inventory = [] (empty list)
    # - moves = 0 (to count moves)
    
    
    # TODO: Show introduction
    # Call show_intro()
    # Call show_commands()
    
    
    # TODO: Main game loop
    # Use: while True:
    
    while True:
        
        # TODO: Show current location
        # Call show_location()
        
        
        # TODO: Get player command
        # Use: command = input("> ").lower().strip()
        # .lower() makes it lowercase
        # .strip() removes extra spaces
        
        
        # TODO: Process command with if/elif/else
        
        # If command is "quit":
        #   - Print goodbye message
        #   - break (exits the loop)
        
        
        # If command is "look":
        #   - Just show location again
        #   - use: continue (skips to next loop)
        
        
        # If command is "inventory":
        #   - Call show_inventory()
        
        
        # If command is "help":
        #   - Call show_commands()
        
        
        # If command starts with "go ":
        #   - Split command to get direction
        #   - Use: parts = command.split()
        #   - direction = parts[1]
        #   - Call go_direction() and update current_location
        
        
        # If command starts with "take ":
        #   - Split command to get item name
        #   - Use: parts = command.split()
        #   - item = parts[1]
        #   - Call take_item()
        
        
        # Else (unknown command):
        #   - Print "Unknown command. Type 'help' for commands"
        
        
        # TODO: Check win condition
        # Call check_win()
        # If True:
        #   - Print congratulations message
        #   - break (exits the loop)
        
        
    # TODO: Show end message
    # Print final stats (moves, items collected, etc.)
    


# =============================================================================
# STEP 6: RUN THE GAME
# =============================================================================

if __name__ == "__main__":
    play_game()


# =============================================================================
# TESTING CHECKLIST
# =============================================================================

"""
Test each feature as you build it!

STAGE 1 TESTING:
[ ] Dictionary of locations created
[ ] Can access location descriptions
[ ] All locations are connected

STAGE 2 TESTING:
[ ] Helper functions work
[ ] show_location displays correctly
[ ] show_inventory displays correctly

STAGE 3 TESTING:
[ ] Can move between locations
[ ] Can pick up items
[ ] Items move to inventory correctly

STAGE 4 TESTING:
[ ] All commands work (go, take, look, inventory, quit)
[ ] Win condition works
[ ] Game doesn't crash on wrong input

FINAL TESTING:
[ ] Play through entire game
[ ] Make sure you can win
[ ] Check all locations are reachable
[ ] Test with wrong commands
"""


# =============================================================================
# BUILDING TIPS
# =============================================================================

"""
HOW TO BUILD THIS STEP BY STEP:

LESSON 1 - Start Simple:
1. Create locations dictionary with 2-3 locations
2. Write show_intro() and print_separator()
3. Test that you can print location info

LESSON 2 - Add Movement:
1. Write show_location()
2. Write go_direction()
3. Test moving between locations
4. Add more locations (aim for 5-7)

LESSON 3 - Add Features:
1. Write take_item()
2. Write show_inventory()
3. Write check_win()
4. Complete main game loop
5. Test everything!

DEBUGGING TIPS:
- Print variables to see their values
- Test one function at a time
- If you get an error, read it carefully
- Ask for help if stuck!

COMMON MISTAKES:
- Spelling location names wrong
- Forgetting to use .lower() on commands
- Not checking if key exists in dictionary
- Infinite loops (make sure you can quit!)
"""