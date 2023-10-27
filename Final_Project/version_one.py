# add imports necessary for the app

import sys
import random
from PIL import Image
import os

print("CWD:", os.getcwd())


#structure for game text and choices
story_one = [
    {
        "path": 1,
        "image": "Images\storyone_flat_tire.jpg",
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
        "image": "Images\storyone_road.jpg",
        "text": "Your friend is taking too long and you decide to get a ride with someone. After 5 minutes of trying, a car finally stops and asks where you're going.",
        "question": "Do you want to tell them where you're going? (yes/no): ",
        "choices": {"yes": 8, "no": None}
    },
    {
        "path": 7,
        "image": "Images\storyone_road.jpg",
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
        "image": "Images\storyone_house.jpg",
        "text": "You tell your friend you need to go back home",
        "question": "Game Over - You couldn't get to work on time. (yes/no): ",
        "choices": {"yes": None, "no": None}
    }
]

story_two = [
    {
        "path": 1,
        "image": "Images\storytwo_raining.jpg",
        "text": "It's late at night and you're on your way to get some food. You're walking alongside the curb when all of a sudden it starts raining and lightning heavily",
        "question": "Should you find some cover and wait it out? (yes/no): ",
        "choices": {"yes": 2, "no": 3}
    },
    {
        "path": 2,
        "image": "Images\storytwo_building.jpg",
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
        "image": "Images\storytwo_games.jpg",
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
        "image": "Images\storytwo_raining.jpg",
        "text": "You leave the building and see that it is still raining and thundering out",
        "question": "Should you go back inside and meet some people? (yes/no): ",
        "choices": {"yes": 8, "no": 9}
    },
    {
        "path": 8,
        "image": "Images\storytwo_games.jpg",
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
        "image": "Images\storythree_driving.jpg",
        "text": "You are looking for a new job and have a very important job interview at 9am that you have to get to. It's currently 7am and you get in the car to start driving there.",
        "question": "Should you stop to get some food first? (yes/no): ",
        "choices": {"yes": 2, "no": 3}
    },
    {
        "path": 2,
        "image": "Images\storythree_drivethru.jpg",
        "text": "You stop to get food but as soon as you order you realize they are backed up",
        "question": "You have been waiting already for 20 minutes. Should you cancel your order and leave? (yes/no): ",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "path": 3,
        "image": "Images\storythree_driving.jpg",
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
        "image": "Images\storythree_traffic.jpg",
        "text": "You decide to pick up the order and when you get there, there are 15 cars ahead of you.",
        "question": "Game Over - You didn't make it to the itnerview. Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "path": 6,
        "image": "Images\storythree_traffic.jpg",
        "text": "As you're driving, you realize there is a big traffic jam on the highway.",
        "question": "Should you take the local roads? (yes/no): ",
        "choices": {"yes": 8, "no": None}
    },
    {
        "path": 7,
        "image": "Images\storythree_drivethru.jpg",
        "text": "You try to find a new place to get some food. You see another fast food restaurant across the street and go there.",
        "question": "Should you get the food and leave? (yes/no): ",
        "choices": {"yes": 8, "no": 9}
    },
    {
        "path": 8,
        "image": "Images\storythree_driving.jpg",
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

story_four = [
    {
        "path": 1,
        "image": "Images\storythree_driving.jpg",
        "text": "You got invited to go over to a friend's house to play games.",
        "question": "Should you go? (yes/no): ",
        "choices": {"yes": 2, "no": 3}
    },
    {
        "path": 2,
        "image": "Images\storythree_drivethru.jpg",
        "text": "You get to your friends house and as soon as you get there you realize everyone is placing bets on who's going to win the most games by the end of the night",
        "question": "Should you participate in the bet? (yes/no): ",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "path": 3,
        "image": "Images\storythree_driving.jpg",
        "text": "You tell your friends you're not going but they insist and you decide to go for a little bit. When you get there, you realize everyone is placing bets on who can win the most games. . ;",
        "question": "Should you get involved? (yes/no): ",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "path": 4,
        "text": "You get really confident and tell everyone you are going to have the most wins. One of your friends challenges you and says they bet $1000 you won't ",
        "question": "Do you want to challenge back? (yes/no): ",
        "choices": {"yes": 6, "no": 7}
    },
    {
        "path": 5,
        "image": "Images\storythree_traffic.jpg",
        "text": "You decide not to place any bets and watch as your friends start placing bets and losing money",
        "question": "Game Over - You didn't get to participate in the game night. Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "path": 6,
        "image": "Images\storythree_traffic.jpg",
        "text": "You bet $2,000 and you all begin with card games. You win the first game but start losing the rest. Your friends start laughing knowing they are about to make some money. You get to the last game and your friends offers a way to redeem yourself. If you bet $1,000, you can make this last game be the only that counts which means if you win, you win the whole bet but if you lose, you'll owe $3,000.",
        "choices": {"yes": 8, "no": None}
    },
    {
        "path": 7,
        "image": "Images\storythree_drivethru.jpg",
        "text": "You counter back and say $500 you will. Your friend accepts and you all start playing card games. You get to the last game and your friend wants to bring up the bet to $1,000 ",
        "question": "Do you want to accept? (yes/no): ",
        "choices": {"yes": 8, "no": 9}
    },
    {
        "path": 8,
        "image": "Images\storythree_driving.jpg",
        "text": "Oof, you played that last game and unfortunately lost. You now owe money",
        "question": "Game Over - Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "path": 9,
        "text": "You ignore your friend and beginning playing the game. You win the last game and once everyone tallies the scores, you realize you won most of the games.",
        "question": "Congrats! You just won $500! Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    }
]

story_five = [
    {
        "path": 1,
        "image": "Images\storythree_driving.jpg",
        "text": "You are at the mall when all of a sudden you see one of your old friends",
        "question": "Do you want to say hi? (yes/no): ",
        "choices": {"yes": 2, "no": 3}
    },
    {
        "path": 2,
        "image": "Images\storythree_drivethru.jpg",
        "text": "You decide to dodge your friend but as you're trying to hide, you run into one of her family members who is also there. She calls over Megan, your friend, and the two of you start chatting. She is so thrilled to see you and invites you to her house to have dinner. ",
        "question": "Should you go? (yes/no): ",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "path": 3,
        "image": "Images\storythree_driving.jpg",
        "text": "You decide to keep driving but then you remembered that you have a pick up order from your sister to get. ;",
        "question": "Should you forget about the order and keep driving? (yes/no): ",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "path": 4,
        "text": "You decide to go and show up at your friends house. You pull up to a ginormous mansion and before you can even park, someone comes up and asks if you would like for your car to be parked. ",
        "question": "You are confused and don't even know if you're at the right house. Should you stay? (yes/no): ",
        "choices": {"yes": 6, "no": 7}
    },
    {
        "path": 5,
        "image": "Images\storythree_traffic.jpg",
        "text": "You decide to pick up the order and when you get there, there are 15 cars ahead of you.",
        "question": "Game Over - You didn't make it to the itnerview. Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "path": 6,
        "image": "Images\storythree_traffic.jpg",
        "text": "You say yes and hand over the keys. Once you step out of the car, your friend comes out of the door and greets you. You let her know that you are impressed by where she lives. She explains she is in tech and also has a couple of side hustles that help bring a lot of income. She even says she has a couple of well known celebrities who are coming over for dinner that she would love for you to meet.",
        "question": "You are shocked again and don't know what to say. Should you stay and see how the night goes? (yes/no): ",
        "choices": {"yes": 8, "no": None}
    },
    {
        "path": 7,
        "image": "Images\storythree_drivethru.jpg",
        "text": "You decide to leave and get in your car. As you're driving away, you get a call from your friend asking where are you. She asks for you to come back but you're not sure what to do.",
        "question": "Should you go back and stay for dinner? (yes/no): ",
        "choices": {"yes": 8, "no": 9}
    },
    {
        "path": 8,
        "image": "Images\storythree_driving.jpg",
        "text": "You decide to stay and begin the night by having a 10-course meel. You get to meet well-known authors and actors that have met your friend through the years through her Instagram and YouTube channels. They seem impressed with your line of work and even offer to work with you in the future. ",
        "question": "Good job! You had a once in a lifetime experience. Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "path": 9,
        "text": "You tell your friend you are so sorry, explaining that you have an emergency to take care off. Your friend says she understands and then ends the call. ",
        "question": "Game Over - You didn't get to experience the wonderful night your friend had planned for all the guests she had invited. Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    }
]

stories = [story_one, story_two, story_three, story_four, story_five]


random_story = random.choice(stories)
current_location = 1

print("Welcome to The Random Story of the Day!")

#loop the user to another random story and go through all the different paths for each of the stories
while True:
    random_story = random.choice(stories)
    current_location = 1

    while current_location in range(1, len(random_story) + 1):
        segment = [s for s in random_story if s["path"] == current_location][0]

        print(segment["text"])

        #display the image if a certain path in the story has one. 
        if "image" in segment:
            image_path = segment["image"]
            img = Image.open(image_path)
            img.show()

        choice = input(f"{segment['question']} ").strip().lower()

        if choice == "yes" and "yes" in segment["choices"]:
            current_location = segment["choices"]["yes"]
        elif choice == "no" and "no" in segment["choices"]:
            current_location = segment["choices"]["no"]
        else:
            print("Invalid choice. Please answer 'yes' or 'no'.")

        if current_location is None:
            play_again = input("Thanks for playing! Play again? (yes/no):").strip().lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                sys.exit()





# Print out functions
# close out class
# deploy app