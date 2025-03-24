import random
import datetime

# Function to print a welcome message
def welcome_message():
    print("===================================")
    print("Welcome to Your Simple Chatbot!")
    print("===================================")
    print("Hello! I'm here to chat with you. \n")

# Function to get the current time
def show_time():
    now = datetime.datetime.now()
    print(f"The current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

# Function to suggest a random activity
def suggest_activity():
    activities = [
        "Go for a walk ",
        "Read a book ",
        "Listen to music ",
        "Try learning Python ",
        "Watch a movie ",
        "Exercise for 10 minutes ",
        "Meditate for a while ",
        "Write a short journal entry"
    ]
    print(f"How about this? {random.choice(activities)}\n")

# Function to get user input and respond
def chat():
    name = input("👤 What's your name? \n")
    print(f"Nice to meet you, {name}! \n")

    while True:
        print("🔹 Menu:")
        print("1. Show the current time ")
        print("2. Suggest an activity ")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            show_time()
        elif choice == "2":
            suggest_activity()
        elif choice == "3":
            print("Goodbye! Have a great day! \n")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Main function
def main():
    welcome_message()
    chat()

# Run the program
if __name__ == "main":
    main()
