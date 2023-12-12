from PIL import Image
import random

# Define a dictionary for the adventure game
adventure_data = {
    "start": {
        "text": "You find yourself at a crossroads. Do you want to go left or right?",
        "options": {
            "Left": "forest",
            "Right": "cave",
        },
        "image_path": "crossroads.jpg"
    },
    "forest": {
        "text": "You enter a dark forest. Continue deeper or turn back?",
        "options": {
            "Deeper": "treasure",
            "Turn back": "start",
        },
        "image_path": "forest.jpg"
    },
    "cave": {
        "text": "You stumble upon a mysterious cave. Enter or continue through the forest?",
        "options": {
            "Enter": "treasure",
            "Continue through the forest": "start",
        },
        "image_path": "cave.jpg"
    },
    "treasure": {
        "text": "You find a treasure chest! Open it or leave it?",
        "options": {
            "Open it": "win",
            "Leave it": "lose",
        },
        "image_path": "treasure.jpg"
    },
    "win": {
        "text": "Congratulations! You've found the treasure and won the game.",
        "options": {},
        "image_path": "win.jpg"
    },
    "lose": {
        "text": "Oops! You've lost the game. Better luck next time.",
        "options": {},
        "image_path": "lose.jpg"
    }
}

# Function to display images
def display_image(image_path):
    img = Image.open(image_path)
    img.show()

# Function to play the game
def play_game():
    current_location = "start"
    while current_location != "win" and current_location != "lose":
        segment = adventure_data[current_location]
        print(segment["text"])
        display_image(segment["image_path"])
        
        options = segment["options"]
        print("Choose your path:")
        for i, (choice, next_location) in enumerate(options.items(), 1):
            print(f"{i}: {choice}")
        
        choice = input("Enter the number of your choice: ")
        while not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
            print("Invalid choice. Please select a valid option.")
            choice = input("Enter the number of your choice: ")
        
        choices = list(options.keys())
        next_location = options[choices[int(choice) - 1]]
        current_location = next_location

# Start the game
print("Welcome to the Randomized Choose Your Own Adventure Game!")
play_game()
