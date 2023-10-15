import random

# Define the stories as dictionaries with "path," "text," and "question"
story1 = {
    "start": {
        "path": "explore",
        "text": "You wake up in a mysterious cave. Do you want to explore deeper? (yes/no)",
        "question": "",
    },
    "explore": {
        "path": "open_chest",
        "text": "You venture deeper into the cave and find a hidden treasure chest. Do you want to open it? (yes/no)",
        "question": "",
    },
    "open_chest": {
        "path": "win",
        "text": "You open the chest and discover a valuable gem. You win the game!",
        "question": "",
    },
    "win": {
        "path": "end",
        "text": "Congratulations! You've won the game.",
        "question": "",
    },
    "end": {
        "path": "end",
        "text": "Game Over.",
        "question": "",
    },
    "lose": {
        "path": "end",
        "text": "You decide not to open the chest and continue exploring. You get lost and lose the game.",
        "question": "",
    },
}

story2 = {
    "start": {
        "path": "join_crew",
        "text": "You find yourself on a pirate ship. Do you want to join the crew? (yes/no)",
        "question": "",
    },
    "join_crew": {
        "path": "win",
        "text": "You become a pirate and have many adventures. You win the game!",
        "question": "",
    },
    "win": {
        "path": "end",
        "text": "Congratulations! You've won the game.",
        "question": "",
    },
    "look_for_exit": {
        "path": "end",
        "text": "You decide not to join the crew and look for a way off the ship. You get caught and walk the plank. You lose the game.",
        "question": "",
    },
    "end": {
        "path": "end",
        "text": "Game Over.",
        "question": "",
    },
}

story3 = {
    "start": {
        "path": "follow_leads",
        "text": "You are a detective investigating a murder. Do you want to follow the leads? (yes/no)",
        "question": "",
    },
    "follow_leads": {
        "path": "win",
        "text": "You follow the leads and catch the killer. You win the game!",
        "question": "",
    },
    "win": {
        "path": "end",
        "text": "Congratulations! You've won the game.",
        "question": "",
    },
    "request_backup": {
        "path": "end",
        "text": "You decide not to follow the leads and request backup. Unfortunately, it takes too long, and the killer escapes. You lose the game.",
        "question": "",
    },
    "end": {
        "path": "end",
        "text": "Game Over.",
        "question": "",
    },
}

# Store the stories in a list
stories = [story1, story2, story3]

# Randomly select a story
selected_story = random.choice(stories)
current_location = "start"

# Play the game
print("Welcome to the Randomized Choose Your Own Adventure Game!")

while current_location in selected_story:
    segment = selected_story[current_location]
    
    print(segment["text"])
    choice = input(f"{segment['question']} ").strip().lower()
    
    if choice == "yes":
        current_location = selected_story[current_location]["path"]
    elif choice == "no":
        current_location = "end"
    else:
        print("Invalid choice. Please answer 'yes' or 'no'.")

