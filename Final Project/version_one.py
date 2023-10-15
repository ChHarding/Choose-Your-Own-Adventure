# add imports necessary for the app

import sys
import random
from PIL import Image

# filename = "C:\Users\14075\Documents\HCI 574\Final Project\driving.jpg"
# img = Image.open(filename)

#structure for game text and choices
story_one = [
    {
        "path": 1,
        # "image": img,
        "text": "You are on the way to work when you all of a sudden you get a flat tire",
        "question": "Do you want to call a friend to come help? (yes/no): ",
        "choices": {"yes": 2, "no": 3}
    },
    {
        "path": 2,
        "text": "You are waiting for your friend when all of a sudden you get a phone call from your boss",
        "question": "You hesitate and then look at your phone again. Do you want to pick up the call? (yes/no): ",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "path": 3,
        "text": "You decide not to call your friend and now you don't know what to do. All of a sudden you get a call from your boss.",
        "question": "Do you want to pick up? (yes/no): ",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "path": 4,
        "text": "Your boss is upset and tells you that there is an emergency at work. You panick and think there has to be a way to get there.",
        "question": "Do you want to hitch a ride with someone? (yes/no): ",
        "choices": {"yes": 6, "no": 7}
    },
    {
        "path": 5,
        "text": "You didn't pick up and now your phone is blowing up.",
        "question": "Game Over - You didn't get to work. Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "path": 6,
        "text": "Your friend is taking too long and you decide to get a ride with someone. After 5 minutes of trying, a car finally stops and asks where you're going.",
        "question": "Do you want to tell them where you're going? (yes/no): ",
        "choices": {"yes": 8, "no": None}
    },
    {
        "path": 7,
        "text": "You keep waiting and all of a sudden your friend shows up",
        "question": "Should you tell them to go straight to work? (yes/no): ",
        "choices": {"yes": 8, "no": 9}
    },
    {
        "path": 8,
        "text": "You tell them where you're going and that you need to get there immediately. They agree and takes you to work",
        "question": "Good job! You managed to get to work! Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "path": 9,
        "text": "You tell your friend you need to go back home",
        "question": "Game Over - You couldn't get to work on time. (yes/no): ",
        "choices": {"yes": None, "no": None}
    }
]

story_two = [
    {
        "path": 1,
        "text": "It's late at night and you're on your way to get some food. You're walking alongside the curb when all of a sudden it starts raining and lightning heavily",
        "question": "Should you find some cover and wait it out? (yes/no): ",
        "choices": {"yes": 2, "no": 3}
    },
    {
        "path": 2,
        "text": "You look ahead and see a building with an awning that you can use to wait out the rain",
        "question": "As you're waiting, you hear a noise from inside the building. Should you investigate? (yes/no): ",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "path": 3,
        "text": "You decide to keep walking and all of a sudden a car stops next to you asking you some questions.",
        "question": "Should you stop and see what they want? (yes/no): ",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "path": 4,
        "text": "You go inside to investigate and see a bunch of people together, eating and playing games.",
        "question": "Should you go up to them and see what is happening? (yes/no): ",
        "choices": {"yes": 6, "no": 7}
    },
    {
        "path": 5,
        "text": "You decide to ignore them and keep walking towards the restaurant you were headed to.",
        "question": "Game Over - You didn't have an adventure. Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "path": 6,
        "text": "You go up to everyone and they just stare at you wondering where you came from.",
        "question": "Do you want to start the conversation? (yes/no): ",
        "choices": {"yes": 8, "no": None}
    },
    {
        "path": 7,
        "text": "You leave the building and see that it is still raining and thundering out",
        "question": "Should you go back inside and meet some people? (yes/no): ",
        "choices": {"yes": 8, "no": 9}
    },
    {
        "path": 8,
        "text": "You tell everyone you were on the way to get some food but it started raining outside and needed a place to wait it out. It turns out they are a club that meets weekly to hang out and play games. They invite you to stay",
        "question": "Good job! You went on an adventure and had a great night out! Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "path": 9,
        "text": "You decide to walk in the rain anyways and eventually you get to the restaurant you were headed to.",
        "question": "Game Over - You didn't have an adventure. Play again?. (yes/no): ",
        "choices": {"yes": None, "no": None}
    }
]

story_three = [
    {
        "path": 1,
        "text": "You are looking for a new job and have a very important job interview at 9am that you have to get to. It's currently 7am and you get in the car to start driving there.",
        "question": "Should you stop to get some food first? (yes/no): ",
        "choices": {"yes": 2, "no": 3}
    },
    {
        "path": 2,
        "text": "You stop to get food but as soon as you order you realize they are backed up",
        "question": "You have been waiting already for 20 minutes. Should you cancel your order and leave? (yes/no): ",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "path": 3,
        "text": "You decide to keep driving but then you remembered that you have a pick up order from your sister to get. ;",
        "question": "Should you forget about the order and keep driving? (yes/no): ",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "path": 4,
        "text": "You cancel the order and get back in your car. ",
        "question": "Should you just drive straight to your interview? (yes/no): ",
        "choices": {"yes": 6, "no": 7}
    },
    {
        "path": 5,
        "text": "You decide to pick up the order and when you get there, there are 15 cars ahead of you.",
        "question": "Game Over - You didn't make it to the itnerview. Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "path": 6,
        "text": "As you're driving, you realize there is a big traffic jam on the highway.",
        "question": "Should you take the local roads? (yes/no): ",
        "choices": {"yes": 8, "no": None}
    },
    {
        "path": 7,
        "text": "You try to find a new place to get some food. You see another fast food restaurant across the street and go there.",
        "question": "Should you get the food and leave? (yes/no): ",
        "choices": {"yes": 8, "no": 9}
    },
    {
        "path": 8,
        "text": "You take the local route and get to your location with 15 minutes to spare.",
        "question": "Good job! You made it to the interview! Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "path": 9,
        "text": "You decide to get the food and eat it there",
        "question": "Game Over - You didn't make it to the interview (yes/no): ",
        "choices": {"yes": None, "no": None}
    }
]

stories = [story_one, story_two, story_three]

random_story = random.choice(stories)
current_location = 1

print("Welcome to The Random Story of the Day!")


while current_location in range(1, len(random_story) + 1):
    segment = [s for s in random_story if s["path"] == current_location][0]

    print(segment["text"])
    choice = input(f"{segment['question']} ").strip().lower()

    if choice == "yes" and "yes" in segment["choices"]:
        current_location = segment["choices"]["yes"]
    elif choice == "no" and "no" in segment["choices"]:
        current_location = segment["choices"]["no"]
    else:
        print("Invalid choice. Please answer 'yes' or 'no'.")

    if current_location is None:
        print("Thanks for playing!")
        continue





# Print out functions
# close out class
# deploy app