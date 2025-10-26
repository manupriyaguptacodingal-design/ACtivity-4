import re,random
from colorama import Fore, Style

init(autoreset=True)
destinations = ["Paris", "New York", "Tokyo", "Sydney", "Cairo"]
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts!"
]

def normalize_input(text):
    return re.sub(r'[^a-zA-Z0-9 ]', '', text).strip().lower()

def recomment():
    print(Fore.CYAN + "Welcome to the Travel Recommender!")
    preference = input(Fore.YELLOW + "Enter your travel preferences or type 'joke' for a joke: ")
    preference = normalize_input(preference)

if preference in destinations:
    suggestion = random.choice(destinations[destinations.index(preference):])
    print(Fore.GREEN + f"Based on your preferences, we recommend you visit: {suggestion}")
    print(Fore.CYAN + "Do you like it? (yes/no)")
    answer = input(Fore.YELLOW + "Your answer: ").lower()

    if answer == 'yes':
        print(Fore.GREEN + "Great! Have a wonderful trip!")
    elif answer == 'no':
        print(Fore.RED + "Sorry to hear that. Maybe try another destination next time!")
        recomment()
    else:
        print(Fore.RED + "Invalid response. Please answer with 'yes' or 'no'.")
        recomment()
else:
 print(Fore.RED + "Sorry, we couldn't find a matching destination.")

show_help()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + " Pack versatile clothes.")
    print(Fore.GREEN + " Bring chargers/adapters.")
    print(Fore.GREEN + " Check the weather forecast.")

# Tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

# Display help menu
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + " Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + " Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name?")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif user_input in ["exit", "bye", "quit"]:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    chat()