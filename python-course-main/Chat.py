#Student Name: Nittai
#Bot Name: Piter
#Bot Purpose: Funning Buddy 
import random
jokes = ["Why don’t skeletons fight each other? They don’t have the guts.", "Why did the scarecrow win an award? Because he was outstanding in his field.", "What do you call fake spaghetti? An impasta.","Why did the computer go to the doctor? Because it had a virus!",
 "Why doesn't the fish like soccer? Because it's afraid of the net!"]
random_joke = random.choice(jokes)
print(random_joke)
  # Prints random joke from list
greetings = [
    "Hello! I'm Piter, your funning buddy. How can I assist you today?",
    "Hello!",
    "Hey there! Ready to have some fun with me?",
    "Hi!",
    "Hello! How are you feeling today?",

]
goodbyes = [
    "Goodbye! Have a great day!",
    "See you later!",
    "Take care!",
    "Until next time!",
    "Farewell!"
]
compliments = [
    "You are amazing!",
    "jood job!",
    "you are a great person!",
    "you are so smart!",
    "you are so kind!"
]
def print_separator():
    print("=" * 20)  #

def bot_message(message):
    print(f"Piter: {message}")

def show_help():
    bot_message("I can tell jokes, give compliments, and have fun conversations! Just type 'joke', 'compliment', or 'help' to see what I can do!")

def greet_user():
    greeting = random.choice(greetings)
    bot_message(greeting)
    user_input = input("what your name: ") 
    print(f"nice to meet you: {user_input}")
      # User input for greeting
def tell_joke():
    joke = random.choice(jokes)
    bot_message(joke)

def play_guess_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    bot_message("Welcome to the Guessing Game! I'm thinking of a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        try:
            user_guess = int(input("Your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                bot_message("Too low! Try again.")
            elif user_guess > number_to_guess:
                bot_message("Too high! Try again.")
            else:
                guessed_correctly = True
                bot_message(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
        except ValueError:
            bot_message("Invalid input. Please enter a number.")
    
def analyze_mood(message):
    message = message.lower()
    happy_words = ["happy", "joy", "excited", "good", "great"]
    sad_words = ["sad", "angry", "upset", "bad", "terrible"]
    for word in happy_words:
        if word in message:
            return "happy"
    for word in sad_words:
        if word in message:
            return "sad"
    return "neutral"