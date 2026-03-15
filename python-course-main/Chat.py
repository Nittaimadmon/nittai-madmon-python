#Student Name: Nittai
#Bot Name: Piter
#Bot Purpose: Funning Buddy 
import random
from urllib import response
jokes = ["Why don’t skeletons fight each other? They don’t have the guts."
         , "Why did the scarecrow win an award? Because he was outstanding in his field.",
          "What do you call fake spaghetti? An impasta.","Why did the computer go to the doctor? Because it had a virus!",
        "Why doesn't the fish like soccer? Because it's afraid of the net!"]
        
  # Prints random joke from list
greetings = [
    "Hello! I'm Piter, your funning buddy. How can I assist you today?",
    "Hello!",
    "Hey there! Ready to have some fun with me?",
    "Hi!",
    "Hello! How are you feeling today?",
]
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
facts = [
    "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible!",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after just 38 minutes.",
    "Octopuses have three hearts and blue blood. Two hearts pump blood to the gills, while the third pumps it to the rest of the body.",
    "Bananas are berries, but strawberries are not. In botanical terms, a berry is a fruit produced from the ovary of a single flower with seeds embedded in the flesh.",
    "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion of the metal."
]
tips = [
    "To stay productive, try the Pomodoro Technique: work for 25 minutes, then take a 5-minute break.",
    "Drinking water can help improve your focus and energy levels throughout the day.",
    "Taking short breaks during work can help reduce stress and increase creativity.",
    "Getting enough sleep is crucial for maintaining good mental and physical health.",
    "Regular exercise can boost your mood and overall well-being."
]
# פונקציה שמחזירה רשימת תגובות ברירת מחדל למקרה שהבוט לא הבין את המשתמש
def default_response(user_name):
    return ["That's interesting",
             "Tell me more!",
             "I see...",
             "Cool!",
             f"Thanks for sharing, {user_name}!"
             ]
# פונקציה שמדפיסה קו מפריד מעוצב בטרמינל
def print_separator():
    print("-" * 20)  #
    # פונקציה עזר להדפסת הודעות מהבוט בפורמט קבוע עם השם "Piter"
def bot_message(message):
    print(f"Piter: {message}")
# פונקציה המציגה למשתמש את רשימת הפקודות והאפשרויות שהבוט מציע
def show_help():
    bot_message("I can tell jokes, give compliments, and have fun conversations! Just type 'joke', 'compliment', or 'help' to see what I can do!")
# פונקציה לניהול שלב הפתיחה: בחירת ברכה אקראית וקבלת שם המשתמש
def greet_user():
    greeting = random.choice(greetings)
    bot_message(greeting)
    
# פונקציה שבוחרת ומציגה בדיחה אקראית מתוך רשימת בדיחות
def tell_joke():
    joke = random.choice(jokes)
    bot_message(joke)
# פונקציה המריצה משחק "נחש את המספר" אינטראקטיבי מול המשתמש
def play_guess_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    bot_message("Welcome to the Guessing Game! I'm thinking of a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        try:
            user_guess = int(input("Your guess: "))
            attempts += 1
            if attempts == 10:
                return bot_message(f"Game over! You've used all 10 attempts. The number was {number_to_guess}. Better luck next time!")
            if user_guess < number_to_guess:
                bot_message("Too low! Try again.")
            elif user_guess > number_to_guess:
                bot_message("Too high! Try again.")
            else:
                guessed_correctly = True
                return bot_message(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
            
        except ValueError:
            bot_message("Invalid input. Please enter a number.")
# פונקציה המנתחת את הטקסט של המשתמש ומחזירה את מצב הרוח שלו (שמח, עצוב או ניטרלי)
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
# הפונקציה המרכזית לעיבוד הודעות: בודקת מילות מפתח ומחליטה איזו תשובה להחזיר למשתמש
def get_response(message, user_name):
    message = message.lower()
    if any(word in message for word in ["hello", "hi", "hey"]):
        return random.choice(greetings)
    elif any(word in message for word in ["favorite color", ]) :
        return "My favorite color is blue! What's yours?"
    elif "hobbies" in message:
        return "I love telling jokes and playing games! What about you?"
    elif "school subjects" in message:
        return "I enjoy learning about science and history! What about you?"
    elif "music" in message:
        return "I love all kinds of music! Do you have a favorite band or artist?" 
    elif "sports" in message:
        return "I enjoy watching soccer and basketball! Do you have a favorite team?"
    elif "mood" in message or "feel" in message:
        mood_result = analyze_mood(message) 
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
    elif any(word in message for word in ["bye", "goodbye", "quit", "exit"]):
        return random.choice(goodbyes)
    elif "joke" in message or "funny" in message:
        return random.choice(jokes)
    elif "help" in message or "commands" in message:
        show_help()
        return "What else can I help with?"
    elif "fact" in message:
        return random.choice(facts)
    elif "tip" in message:
        return random.choice(tips)
    elif any(op in message for op in ["+", "-", "*", "/"]):
        try:
            result = eval(message)
            return f"The result is: {result}"
        except:
            return "I couldn't calculate that. Try: 10 + 5"
 
    elif "game" in message or "play" in message:
            print("1. Number Guessing Game")
            print("2. Never mind")
            
            choice = input("Enter choice: ")
            if choice == "1":
                result = play_guess_game()
                print(result)
            elif choice == "2":   
                print("No problem! What else would you like to talk about?")
            else:
                print("Invalid choice. Please enter 1 or 2.")

    elif "compliment" in message:
        return random.choice(compliments)
    else:
        return random.choice(default_response(user_name))
    # פונקציית הלולאה הראשית שמנהלת את השיחה כולה עד שהמשתמש מחליט לצאת
def chat():
    print_separator()
    greet_user()
    user_name = input("what your name: ") 
    print(f"nice to meet you: {user_name}")
    show_help()
    while True:
        user_input = input(f"\n{user_name}: ").strip()
        if not user_input:
            continue
        elif user_input.lower() in ["bye", "goodbye", "quit", "exit"]:
            bot_message(f"{random.choice(goodbyes)} {user_name}!")
            break
        else:
            print("working on response...")
            # Get bot response
            response = get_response(user_input, user_name)
            print(response)

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
        


