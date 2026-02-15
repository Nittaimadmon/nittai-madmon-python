"""
SMART CHATBOT PROJECT
=====================

Student Name: [YOUR NAME HERE]
Bot Name: [YOUR BOT NAME]
Bot Purpose: [e.g., Study Helper, Gaming Buddy, Quiz Master]

PROJECT GOAL:
Build a chatbot that can have conversations, respond to questions,
tell jokes, play games, and interact with users in a fun way.

WHAT YOU NEED TO BUILD:
✓ Bot responds to different types of messages
✓ Bot can tell jokes
✓ Bot can play at least one game
✓ Bot remembers user's name
✓ At least 5 functions
✓ Natural conversation flow

TIME: 3 lessons to complete
"""

import random

# =============================================================================
# UNDERSTANDING LISTS & RANDOM (Brief Review)
# =============================================================================

"""
LISTS:
A list stores multiple items in order.

SYNTAX:
my_list = ["item1", "item2", "item3"]

EXAMPLE:
jokes = ["Joke 1", "Joke 2", "Joke 3"]

# Access items by index (starts at 0):
print(jokes[0])  # Prints: Joke 1
print(jokes[1])  # Prints: Joke 2

# Add items:
jokes.append("Joke 4")

# Remove items:
jokes.remove("Joke 1")

RANDOM.CHOICE:
Picks a random item from a list

EXAMPLE:
import random
jokes = ["Joke 1", "Joke 2", "Joke 3"]
random_joke = random.choice(jokes)
print(random_joke)  # Prints random joke from list

STRING METHODS:
- message.lower() - makes text lowercase
- message.strip() - removes extra spaces
- "word" in message - checks if word is in message
"""

# =============================================================================
# STEP 1: BOT PERSONALITY DATA
# =============================================================================

"""
TODO: Create lists of responses for your bot

These lists will make your bot feel more natural and varied.
The bot will use random.choice() to pick from these lists.
"""

# TODO: Choose your bot's name
bot_name = "BotName"  # Change this!


# TODO: Create a list of at least 5 greetings
# When user says "hello", bot picks one randomly
greetings = [
    # Add at least 5 greetings here
    # Example: "Hi!", "Hello!", "Hey there!"
]


# TODO: Create a list of at least 5 goodbyes
# When user says "bye", bot picks one randomly  
goodbyes = [
    # Add at least 5 goodbyes here
    # Example: "Bye!", "See you!", "Goodbye!"
]


# TODO: Create a list of at least 5 jokes
# When user asks for a joke, bot picks one randomly
jokes = [
    # Add at least 5 jokes here
    # Example: "Why did the chicken cross the road?"
]


# TODO: Create lists for other responses (optional)
# Examples:
# - compliments = ["You're awesome!", "Great job!", ...]
# - facts = ["Did you know...", "Fun fact: ...", ...]
# - tips = ["Tip: ...", "Remember to ...", ...]


# =============================================================================
# STEP 2: HELPER FUNCTIONS
# =============================================================================

"""
Helper functions make your code cleaner.
"""

# TODO: Write a function that prints a separator line
# Function name: print_separator
# What it does: Prints "=========================================="
# Parameters: none
# Returns: nothing

def print_separator():
    # TODO: Print a line of = signs
    pass


# TODO: Write a function that prints bot's message
# Function name: print_bot
# What it does: Prints message with bot's name
# Example: "🤖 BotName: Hello!"
# Parameters: message (string)
# Returns: nothing

def print_bot(message):
    # TODO: Print bot's message with formatting
    # Use: print(f"🤖 {bot_name}: {message}")
    pass


# TODO: Write a function that shows what bot can do
# Function name: show_help
# What it does: Lists all bot capabilities
# Parameters: none
# Returns: nothing

def show_help():
    # TODO: Print a list of things your bot can do
    # Example: "I can chat, tell jokes, play games..."
    pass


# =============================================================================
# STEP 3: GREETING FUNCTION
# =============================================================================

"""
This function starts the conversation and gets user's name.
"""

# TODO: Write a function that greets user and gets their name
# Function name: greet_user
# What it does:
#   1. Print welcome message with bot name
#   2. Ask for user's name
#   3. Return the name
# Parameters: none
# Returns: user_name (string)

def greet_user():
    # TODO: Print welcome message
    # TODO: Ask "What's your name?"
    # TODO: Get user input with input()
    # TODO: Print personalized greeting
    # TODO: Return the name
    pass


# =============================================================================
# STEP 4: RESPONSE FUNCTIONS
# =============================================================================

"""
These functions make your bot interactive.
"""

# TODO: Write a function that tells a joke
# Function name: tell_joke
# What it does: Returns a random joke from jokes list
# Parameters: none
# Returns: joke (string)
#
# HINT: Use random.choice(jokes)

def tell_joke():
    # TODO: Pick random joke from jokes list
    # TODO: Return it
    pass


# TODO: Write a function for a number guessing game
# Function name: play_guess_game
# What it does:
#   1. Bot thinks of number between 1-20
#   2. User keeps guessing
#   3. Bot says "too high" or "too low"
#   4. Count attempts
#   5. Return result message
# Parameters: none
# Returns: result message (string)
#
# HINT: Use random.randint(1, 20)
# HINT: Use a while loop
# HINT: Use try/except for invalid input

def play_guess_game():
    # TODO: Generate random number
    # TODO: Initialize attempts counter
    # TODO: Loop until correct:
    #   - Get user guess
    #   - Compare with number
    #   - Give hint (too high/low)
    # TODO: Return final message with attempts
    pass


# TODO: Write a function that detects mood
# Function name: analyze_mood
# What it does: Checks if message contains happy or sad words
# Parameters: message (string)
# Returns: "happy", "sad", or "neutral"
#
# HINT: Create lists of happy_words and sad_words
# HINT: Use "word in message.lower()" to check

def analyze_mood(message):
    # TODO: Create list of happy words
    # happy_words = ["happy", "great", "awesome", ...]
    
    # TODO: Create list of sad words
    # sad_words = ["sad", "bad", "terrible", ...]
    
    # TODO: Check message for happy words
    # If found, return "happy"
    
    # TODO: Check message for sad words
    # If found, return "sad"
    
    # TODO: Otherwise return "neutral"
    pass


# =============================================================================
# STEP 5: MAIN RESPONSE FUNCTION
# =============================================================================

"""
This is the BRAIN of your bot!
It decides how to respond based on what user said.
"""

# TODO: Write the main response function
# Function name: get_response
# What it does: Analyzes user message and returns appropriate response
# Parameters: message (string), user_name (string)
# Returns: response (string)
#
# THIS IS THE MOST IMPORTANT FUNCTION!
# You need to add MANY if/elif checks for different types of messages.

def get_response(message, user_name):
    """
    Analyze user message and generate response.
    Add as many response patterns as you can!
    """
    
    # TODO: Convert message to lowercase for easier checking
    # message_lower = message.lower()
    
    
    # TODO: Check for greetings
    # If message contains "hello", "hi", or "hey":
    #   - Return random greeting from greetings list
    #   - Add user's name: f"{greeting}, {user_name}!"
    
    
    # TODO: Check for "how are you"
    # If message contains "how are you":
    #   - Return something like "I'm great! How are you?"
    
    
    # TODO: Check for bot name question
    # If message contains "your name" or "who are you":
    #   - Return bot's name
    
    
    # TODO: Check for joke request
    # If message contains "joke" or "funny":
    #   - Call tell_joke() and return the joke
    
    
    # TODO: Check for game request
    # If message contains "game" or "play":
    #   - Return "game_menu" (special signal)
    
    
    # TODO: Check for help request
    # If message contains "help" or "commands":
    #   - Call show_help()
    #   - Return "What else can I help with?"
    
    
    # TODO: Check for math
    # If message contains "+", "-", or "*":
    #   - Try to calculate with eval()
    #   - Return result
    #   - Use try/except in case it fails
    
    
    # TODO: Add YOUR OWN response patterns here!
    # Think about what you want your bot to respond to:
    # - Favorite color?
    # - Hobbies?
    # - School subjects?
    # - Music?
    # - Sports?
    # Add at least 5 more response patterns!
    
    
    # TODO: Use mood detection
    # Call analyze_mood(message)
    # If mood is "happy": return happy response
    # If mood is "sad": return sympathetic response
    
    
    # TODO: Default responses (when bot doesn't understand)
    # Create list of generic responses:
    # default_responses = [
    #     "That's interesting!",
    #     "Tell me more!",
    #     "I see...",
    #     "Cool!",
    #     f"Thanks for sharing, {user_name}!"
    # ]
    # Return random choice from list
    
    pass


# =============================================================================
# STEP 6: MAIN CHAT LOOP
# =============================================================================

"""
This brings everything together.
The loop keeps running until user says goodbye.
"""

def chat():
    """Main chat function"""
    
    # TODO: Greet user and get their name
    # Call greet_user() and save name
    
    
    # TODO: Show what bot can do
    # Call show_help()
    
    
    # TODO: Main chat loop
    # Use: while True:
    
    while True:
        
        # TODO: Get user message
        # Use: user_message = input(f"\n{user_name}: ").strip()
        
        
        # TODO: Skip if message is empty
        # Use: if not user_message: continue
        
        
        # TODO: Check for goodbye
        # If message contains "bye", "goodbye", "quit", or "exit":
        #   - Pick random goodbye from goodbyes list
        #   - Print goodbye with user's name
        #   - break (exits loop)
        
        
        # TODO: Get bot response
        # Call get_response(user_message, user_name)
        # Save response in variable
        
        
        # TODO: Check if response is "game_menu"
        # If yes:
        #   - Print "What would you like to play?"
        #   - Print "1. Number Guessing Game"
        #   - Print "2. (Add another game if you want)"
        #   - Print "3. Never mind"
        #   - Get user choice
        #   - If "1": call play_guess_game()
        #   - Print result
        # If no:
        #   - Just print the response
        
        
    # TODO: Show chat statistics (optional)
    # Print how many messages were exchanged
    # Print "Thanks for chatting!"
    


# =============================================================================
# STEP 7: RUN THE CHATBOT
# =============================================================================

if __name__ == "__main__":
    chat()


# =============================================================================
# TESTING CHECKLIST
# =============================================================================

"""
Test each feature as you build it!

STAGE 1 TESTING:
[ ] Lists of responses created
[ ] Bot name set
[ ] greet_user() works
[ ] Bot can say hello

STAGE 2 TESTING:
[ ] tell_joke() works
[ ] Bot responds to greetings
[ ] Bot responds to simple questions
[ ] Help command works

STAGE 3 TESTING:
[ ] play_guess_game() works
[ ] get_response() has 10+ response patterns
[ ] Mood detection works
[ ] Bot handles unknown messages

STAGE 4 TESTING:
[ ] Full conversation flows naturally
[ ] Can chat and quit properly
[ ] All features work together
[ ] No crashes on weird input

FINAL TESTING:
[ ] Chat with bot for 5+ minutes
[ ] Try different types of messages
[ ] Play all games
[ ] Make sure it's fun!
"""


# =============================================================================
# BUILDING TIPS
# =============================================================================

"""
HOW TO BUILD THIS STEP BY STEP:

LESSON 1 - Start Simple:
1. Fill in bot_name and all lists (greetings, jokes, etc.)
2. Write greet_user()
3. Write tell_joke()
4. Test these work

LESSON 2 - Add Responses:
1. Write get_response() with 5-10 response patterns
2. Write analyze_mood()
3. Test different types of messages
4. Add more response patterns (aim for 15+)

LESSON 3 - Add Games & Polish:
1. Write play_guess_game()
2. Complete main chat loop
3. Add more features
4. Test everything thoroughly!

DEBUGGING TIPS:
- Print message to see what bot received
- Test one response pattern at a time
- Make sure lists aren't empty
- Use .lower() when checking messages

COMMON MISTAKES:
- Not using .lower() on messages
- Empty lists cause errors with random.choice()
- Forgetting to return values from functions
- Not handling empty input

MAKING IT BETTER:
- Add more response patterns (aim for 20+!)
- Make responses feel natural
- Add personality to your bot
- Include fun features (games, facts, etc.)
- Test with friends and improve based on feedback
"""