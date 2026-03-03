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
def default_response(user_name):
    return ["That's interesting",
             "Tell me more!",
             "I see...",
             "Cool!",
             f"Thanks for sharing, {user_name}!"
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

def get_response(message, user_name):
    message = message.lower()
    if any(word in message for word in ["hello", "hi", "hey"]):
        return random.choice(greetings)
    elif any(word in message for word in ["favorite color", ]) :
        return "My favorite color is blue! What's yours?"
    elif "Hobbies" in message:
        return "I love telling jokes and playing games! What about you?"
    elif "School subjects" in message:
        return "I enjoy learning about science and history! What about you?"
    elif "music" in message:
        return "I love all kinds of music! Do you have a favorite band or artist?" 
    elif "sports" in message:
        return "I enjoy watching soccer and basketball! Do you have a favorite team?"
    elif "mood" in message or "feel" in message:
        mood_result = analyze_mood(message)

        happy_responses = [
            "That's amazing to hear!",
            "I'm so glad you're having a good day!",
            "Keep that positive energy going!"
    ]

        sad_responses = [
            "I'm sorry you're feeling this way.",
            "I'm here for you if you want to talk.",
            "Hang in there, things will get better."
    ]

        neutral_responses = [
            "I see. Thanks for sharing that with me.",
            "Got it. Tell me more if you'd like.",
            "I'm listening."
    ] 
        if mood_result == "happy":
            return random.choice(happy_responses)
        elif mood_result == "sad":
            return random.choice(sad_responses)
        else:
            return random.choice(neutral_responses)
    elif "how are you" in message:
        return "I'm great! How are you?"
    elif "what's your name" in message:
        return "I'm Piter, your funning buddy!"
    elif "bye" in message:
        return random.choice(goodbyes)
    elif "joke" in message or "funny" in message:
        return random.choice(jokes)
    elif "help" in message or "commands" in message:
        show_help()
        return "What else can I help with?"
    elif any(op in message for op in ["+", "-", "*", "/"]):
        try:
            result = eval(message)
            return f"The result is: {result}"
        except:
            return "I couldn't calculate that. Try: 10 + 5"

    elif "game" in message or "play" in message:
        play_guess_game()
    else:
        return random.choice(default_response(user_name))
def chat():
    print_separator()
    greet_user()
    user_name = input("What's your name? ")
    print(f"Nice to meet you, {user_name}!")
    show_help()
    while True:
        user_input = input(f"\n{user_name}: ").strip()
        if not user_input:
            continue
        elif user_input.lower() in ["bye", "goodbye", "quit", "exit"]:
            bot_message(f"{random.choice(goodbyes)} {user_name}!")
            break
        else:
            # Get bot response
            response = get_response(user_input, user_name)

        # Check if response is "game_menu"
        if response == "game_menu":
            print("1. Number Guessing Game")
            print("2. Never mind")
            
            choice = input("Enter choice: ")
            if choice == "1":
                result = play_guess_game()
                print(result)
            elif choice == "2":   
                print("No problem! What else would you like to talk about?")
            else:
                print(response)
        if __name__ == "__main__":
            chat()
        


