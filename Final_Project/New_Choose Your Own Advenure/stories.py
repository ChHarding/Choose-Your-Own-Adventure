stories = [
  [
    {
        "path": 1,
        "image": "Images\storyone_flat_tire.jpg",
        "text": "You are on the way to work when you all of a sudden you get a flat tire",
        "question": "What should you do?",
        "choices": {"Call friend": 2, "Pull to the side": 3, "Go home": 2, "Call your boss": 3}
    },
    {
        "path": 2,
        "sound": "Sounds\sos-morse-code_daniel-simion.wav",
        "text": "You are waiting for your friend when all of a sudden you get a phone call from your boss. You hesitate and then look at your phone again. ",
        "sound": "Sounds\phone ring.mp3",
        "question": "What do you want to do?",
        "choices": {"Pick Up": 4, "Decline": 5, "Text": 4, "Set your phone aside": 5}
    },
    {
        "path": 3,
        "text": "You decide not to call your friend and now you don't know what to do. All of a sudden you get a call from your boss.",
        "sound": "Sounds\phone ring.mp3",
        "question": "What do you want to do?",
        "choices": {"Pick up": 4, "Decline": 5, "Text": 4, "Set your phone aside": 5}
    },
    {
        "path": 4,
        "text": "Your boss is upset and tells you that there is an emergency at work. You panick and think there has to be a way to get there.",
        "question": "Do you want to hitch a ride with someone?",
        "choices": {"yes": 6, "no": 7}
    },
    {
        "path": 5,
        "text": "You didn't pick up and now your phone is blowing up.",
        "sound": "Sounds\message ring.mp3",
        "question": "Game Over - You didn't get to work. You can quit the game or click New Story to play again",
        "choices": {"Quit Game": None}
    },
    {
        "path": 6,
        "image": "Images\storyone_road.jpg",
        "text": "Your friend is taking too long and you decide to get a ride with someone. After 5 minutes of trying, a car finally stops and asks where you're going.",
        "sound": "Sounds\car skids.wav",
        "question": "Do you want to tell them where you're going?",
        "choices": {"yes": 8, "no": 7}
    },
    {
        "path": 7,
        "image": "Images\storyone_road.jpg",
        "text": "You keep waiting and all of a sudden your friend shows up",
        "question": "Should you tell them to go straight to work?",
        "choices": {"yes": 8, "no": 9}
    },
    {
        "path": 8,
        "text": "You tell them where you're going and that you need to get there immediately. They agree and takes you to work",
        "question": "Good job! You managed to get to work! You can quit the game or hit New Story to play again",
        "choices": {"Quit Game": None}
    },
    {
        "path": 9,
        "image": "Images\storyone_house.jpg",
        "text": "You tell your friend you need to go back home",
        "question": "Game Over - You couldn't get to work on time. You can quit the game or hit New Story to play again",
        "choices": {"Quit Game": None}
    }
  ],
  [
    {
        "path": 1,
        "image": "Images\storytwo_raining.jpg",
        "text": "It's late at night and you're on your way to get some food. You're walking alongside the curb when all of a sudden it starts raining and lightning heavily",
        "question": "What should you do?",
        "choices": {"Find cover": 2, "Keep walking": 3, "Go home": 2, "Call a friend": 3}
    },
    {
        "path": 2,
        "image": "Images\storytwo_building.jpg",
        "text": "You look ahead and see a building with an awning that you can use to wait out the rain. As you're waiting, you hear a noise from inside the building. ",
        "sound": "Sounds\random noise.wav",
        "question": "What should you do?",
        "choices": {"Investigate": 4, "Stay there": 5, "Follow someone in": 4, "Keep walking": 5}
    },
    {
        "path": 3,
        "text": "You decide to keep walking and all of a sudden a car stops next to you asking you some questions.",
        "sound": "Sounds\car skids.wav",
        "question": "Should you stop and see what they want?",
        "choices": {"Talk to them": 4, "Ignore them": 5, "Follow the car": 4, "Keep walking": 5}
    },
    {
        "path": 4,
        "image": "Images\storytwo_games.jpg",
        "text": "You go inside to investigate and see a bunch of people together, eating and playing games.",
        "question": "Should you go up to them and see what is happening?",
        "choices": {"yes": 6, "no": 7}
    },
    {
        "path": 5,
        "sound": "Sounds\sos-morse-code_daniel-simion.wav",
        "text": "You decide to ignore them and keep walking towards the restaurant you were headed to.",
        "question": "Game Over - You didn't have an adventure. You can quit the game or hit New Story to play again",
        "choices": {"Quit Game": None}
    },
    {
        "path": 6,
        "text": "You go up to everyone and they just stare at you wondering where you came from.",
        "question": "Do you want to start the conversation?",
        "choices": {"yes": 8, "no": 7} 
    },
    {
        "path": 7,
        "image": "Images\storytwo_raining.jpg",
        "text": "You leave the building and see that it is still raining and thundering out",
        "sound": "Sounds\rain.wav",
        "question": "Should you go back inside and meet some people?",
        "choices": {"yes": 8, "no": 9}
    },
    {
        "path": 8,
        "image": "Images\storytwo_games.jpg",
        "text": "You tell everyone you were on the way to get some food but it started raining outside and needed a place to wait it out. It turns out they are a club that meets weekly to hang out and play games. They invite you to stay",
        "question": "Good job! You went on an adventure and had a great night out! You can quit the game or hit New Story to play again",
        "choices": {"Quit Game": None}
    },
    {
        "path": 9,
        "text": "You decide to walk in the rain anyways and eventually you get to the restaurant you were headed to.",
        "question": "Game Over - You didn't have an adventure. You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    }
  ],
  [
    {
        "path": 1,
        "image": "Images\storythree_driving.jpg",
        "text": "You are looking for a new job and have a very important job interview at 9am that you have to get to. It's currently 7am and you get in the car to start driving there.",
        "question": "What should you do first?",
        "choices": {"Get food": 2, "Continue driving": 3, "Call sister": 2, "Go straight to job interview": 3}
    },
    {
        "path": 2,
        "image": "Images\storythree_drivethru.jpg",
        "text": "You stop to get food but as soon as you order you realize they are backed up. You have been waiting already for 20 minutes. ",
        "question": "Should you cancel your order and leave?",
        "choices": {"Cancel order": 4, "Wait in line": 5, "Get in the car": 4, "Stay there": 5}
    },
    {
        "path": 3,
        "image": "Images\storythree_driving.jpg",
        "text": "You decide to keep driving but then you remembered that you have a pick up order from your sister to get. ;",
        "sound": "Sounds\car starting.wav",
        "question": "Should you forget about the order and keep driving or pick it up? ",
        "choices": {"Keep driving": 4, "Pick up order": 5}
    },
    {
        "path": 4,
        "text": "You cancel the order and get back in your car. ",
        "sound": "Sounds\car starting.wav",
        "question": "Should you just drive straight to your interview or find a new restaurant? ",
        "choices": {"Drive to interview": 6, "Find new restaurant": 7}
    },
    {
        "path": 5,
        "image": "Images\storythree_traffic.jpg",
        "text": "You decide to pick up the order and when you get there, there are 15 cars ahead of you.",
        "question": "Game Over - You didn't make it to the interview. You can quit the game or hit New Story to play again",
        "choices": {"Quit Game": None}
    },
    {
        "path": 6,
        "image": "Images\storythree_traffic.jpg",
        "text": "As you're driving, you realize there is a big traffic jam on the highway.",
        "question": "Should you take the local roads?",
        "choices": {"yes": 8, "no": 7}
    },
    {
        "path": 7,
        "image": "Images\storythree_drivethru.jpg",
        "text": "You try to find a new place to get some food. You see another fast food restaurant across the street and go there.",
        "question": "Should you get the food and leave?",
        "choices": {"yes": 8, "no": 9}
    },
    {
        "path": 8,
        "image": "Images\storythree_driving.jpg",
        "text": "You take the local route and get to your location with 15 minutes to spare.",
        "question": "Good job! You made it to the interview! You can quit the game or hit New Story to play again",
        "choices": {"Quit Game": None}
    },
    {
        "path": 9,
        "text": "You decide to get the food and eat it there",
        "question": "Game Over - You didn't make it to the interview. You can quit the game or hit New Story to play again",
        "choices": {"Quit Game": None}
    }
  ],
  [
    {
        "path": 1,
        "image": "Images\storyfour_house.jpg",
        "text": "You got invited to go over to a friend's house to play games.",
        "question": "Should you go?",
        "choices": {"yes": 2, "no": 3}
    },
    {
        "path": 2,
        "image": "Images\storyfour_games.jpg",
        "text": "You get to your friends house and as soon as you get there you realize everyone is placing bets on who's going to win the most games by the end of the night",
        "sound": "random noise.wav",
        "question": "Should you participate in the bet?",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "path": 3,
        "image": "Images\storyfour_games.jpg",
        "text": "You tell your friends you're not going but they insist and you decide to go for a little bit. When you get there, you realize everyone is placing bets on who can win the most games.",
        "question": "Should you get involved?",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "path": 4,
        "text": "You get really confident and tell everyone you are going to have the most wins. One of your friends challenges you and says they bet $1000 you won't ",
        "question": "Do you want to challenge back?",
        "choices": {"yes": 6, "no": 7}
    },
    {
        "path": 5,
        "image": "Images\storythree_traffic.jpg",
        "text": "You decide not to place any bets and watch as your friends start placing bets and losing money",
        "question": "Game Over - You didn't get to participate in the game night. You can quit the game or hit New Story to play again",
        "choices": {"Quit Game": None}
    },
    {
        "path": 6,
        "image": "Images\storyfour_games.jpg",
        "text": "You bet $2,000 and you all begin with card games. You win the first game but start losing the rest. Your friends start laughing knowing they are about to make some money. You get to the last game and your friends offers a way to redeem yourself. If you bet $1,000, you can make this last game be the only that counts which means if you win, you win the whole bet but if you lose, you'll owe $3,000.",
        "question": "Should you play the game?",
        "choices": {"yes": 8, "no": 7}
    },
    {
        "path": 7,
        "image": "Images\storyfour_games.jpg",
        "text": "You counter back and say $500 you will. Your friend accepts and you all start playing card games. You get to the last game and your friend wants to bring up the bet to $1,000 ",
        "question": "Do you want to accept?",
        "choices": {"yes": 8, "no": 9}
    },
    {
        "path": 8,
        "image": "Images\storyfour_games2.jpg",
        "text": "Oof, you played that last game and unfortunately lost. You now owe money",
        "sound": "random noise.wav",
        "question": "Game Over - You can quit the game or hit New Story to play again",
        "choices": {"Quit Game": None}
    },
    {
        "path": 9,
        "image": "Images\storyfour_games2.jpg",
        "text": "You ignore your friend and begin playing the game. You win the last game and once everyone tallies the scores, you realize you won most of the games.",
        "question": "Congrats! You just won $500! You can quit the game or hit New Story to play again",
        "choices": {"Quit Game": None}
    }
  ],
  [
    {
        "path": 1,
        "image": "Images\storyfive_mall.jpg",
        "text": "You are at the mall when all of a sudden you see one of your old friends",
        "question": "Do you want to say hi or keep walking?",
        "choices": {"Say hi": 2, "Keep walking": 3}
    },
    {
        "path": 2,
        "text": "You guys used to be really close so you decide to go up to your friend and say hi. You start catching up and your friend invites you over for dinner.",
        "question": "Should you go?",
        "choices": {"Go to dinner": 4, "Decline": 5}
    },
    {
        "path": 3,
        "image": "Images\storyfive_mall.jpg",
        "text": "You decide to dodge your friend but as you're trying to hide, you run into one of her family members who is also there. She calls over Megan, your friend, and the two of you start chatting. She is so thrilled to see you and invites you to her house to have dinner.",
        "question": "Should you go have dinner with them?",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "path": 4,
        "image": "Images\storyfive_mansion.jpg",
        "text": "You decide to go and show up at your friends house. You pull up to a ginormous mansion and before you can even park, someone comes up and asks if you would like for your car to be parked. ",
        "sound": "Sounds\car skids.wav",
        "question": "You are confused and don't even know if you're at the right house. Should you stay?",
        "choices": {"yes": 6, "no": 7}
    },
    {
        "path": 5,
        "text": "You decided to not go to your friends house",
        "question": "Game Over - You didn't get to experience the fun night your friend had planned. You can quit the game or hit New Story to play again",
        "choices": {"Quit Game": None}
    },
    {
        "path": 6,
        "image": "Images\storyfive_mansion",
        "text": "You say yes and hand over the keys. Once you step out of the car, your friend comes out of the door and greets you. You let her know that you are impressed by where she lives. She explains she is in tech and also has a couple of side hustles that help bring a lot of income. She even says she has a couple of well known celebrities who are coming over for dinner that she would love for you to meet.",
        "sound": "Sounds\car skids.wav",
        "question": "You are shocked again and don't know what to say. Should you stay and see how the night goes?",
        "choices": {"yes": 8, "no": 7}
    },
    {
        "path": 7,
        "image": "Images\storythree_driving.jpg",
        "text": "You decide to leave and get in your car. As you're driving away, you get a call from your friend asking where are you. She asks for you to come back but you're not sure what to do.",
        "sound": "Sounds\phone ring.mp3",
        "question": "Should you go back and stay for dinner? (yes/no): ",
        "choices": {"yes": 8, "no": 9}
    },
    {
        "path": 8,
        "image": "Images\storyfive_dinner.jpg",
        "text": "You decide to stay and begin the night by having a 10-course meel. You get to meet well-known authors and actors that have met your friend through the years through her Instagram and YouTube channels. They seem impressed with your line of work and even offer to work with you in the future. ",
        "question": "Good job! You had a once in a lifetime experience. You can quit the game or hit New Story to play again",
        "choices": {"Quit Game": None}
    },
    {
        "path": 9,
        "text": "You tell your friend you are so sorry, explaining that you have an emergency to take care off. Your friend says she understands and then ends the call. ",
        "question": "Game Over - You didn't get to experience the wonderful night your friend had planned for all the guests she had invited. You can quit the game or hit New Story to play again",
        "choices": {"Quit Game": None}
    }
  ],
  [
    {
        "path": 1,
        "image": "Images\storysix_hiking.jpg",
        "text": "You decide to go on a hiking trip in a dense, unfamiliar forest. As you venture deeper into the woods, you realize you've lost your way.",
        "question": "Should you use a compass and map to navigate, try following the stars, follow the river, or climb a tree for a better view? (compass/stars/river/climb): ",
        "choices": {"compass": 2, "stars": 4, "river": 6, "climb": 8}
    },
    {
        "path": 2,
        "image": "Images\storysix_compass.jpg",
        "text": "You use your compass and map to find your way, but it's not helping much. You start to hear strange sounds in the forest.",
        "sound": "Sounds\forest.wav",
        "question": "Do you want to follow the sounds, continue using the compass, light a torch, or build a shelter for the night? (follow/compass/light/shelter): ",
        "choices": {"follow": 4, "compass": 5, "light": 7, "shelter": 8}
    },
    {
        "path": 4,
        "image": "Images\storysix_campfire.jpg",
        "text": "You follow the sounds and discover a hidden campfire with a group of mysterious people. They invite you to sit and share stories around the campfire.",
        "sound": "Sounds\fire.wav",
        "question": "Do you want to join them, continue using the compass, light a torch, or build a shelter for the night? (join/compass/light/shelter): ",
        "choices": {"join": 6, "compass": 5, "light": 7, "shelter": 8}
    },
    {
        "path": 5,
        "image": "Images\storysix_compass.jpg",
        "text": "You decide not to follow the sounds and continue to navigate using your compass and map. You eventually find your way out of the forest.",
        "sound": "Sounds\forest.wav",
        "question": "Congratulations, you made it out of the forest! You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    },
    {
        "path": 6,
        "text": "You join the group, and they share stories of the forest's secrets. It turns out they are friendly locals who know the area well. They guide you out of the forest the next morning.",
        "question": "Should you join them on another adventure?",
        "choices": {"Join": 11, "Go Home": 12}
    },
    {
        "path": 7,
        "image": "Images\storysix_compass.jpg",
        "text": "You decide not to join them and instead continue to follow the compass. It takes a while, but you eventually find your way out of the forest.",
        "question": "Congratulations, you made it out of the forest! You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    },
    {
        "path": 8,
        "image": "Images\storysix_tree.jpg",
        "text": "You decide to climb a tree to get a better view of your surroundings. From the top, you spot a distant clearing. Do you want to head towards the clearing, continue using the compass, light a torch, or build a shelter for the night? (clearing/compass/light/shelter): ",
        "sound": "Sounds\random noise.wav",
        "choices": {"clearing": 9, "compass": 5, "light": 7, "shelter": 10}
    },
    {
        "path": 9,
        "text": "You make your way to the clearing and find a trail that leads you out of the forest. You've successfully escaped the wilderness.",
        "question": "Congratulations, you made it out of the forest! You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    },
    {
        "path": 10,
        "image": "Images\storysix_shelter.jpg",
        "text": "You decide to build a shelter for the night, and it provides some protection. In the morning, you continue your journey and eventually find your way out of the forest.",
        "question": "Congratulations, you made it out of the forest! You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    },
    {
        "path": 11,
        "text": "You join them on another adventure!",
        "question": "Good job! You made new friends and found your way back home. You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    },
    {
        "path": 12,
        "text": "You join them on another adventure!",
        "question": "Oh no - seems like your adventure got cut short! You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    }
],
[
    {
        "path": 1,
        "image": "Images\storyseven_mailbox.jpg",
        "text": "You go to check your mailbox, and you find a mysterious package with no return address or name on it.",
        "question": "Should you open the package, leave it alone, contact the authorities, or take it to a friend's house? (open/leave/contact/friend): ",
        "choices": {"open": 2, "leave": 3, "contact": 4, "friend": 5}
    },
    {
        "path": 2,
        "image": "Images\storyseven_device.jpg",
        "text": "You decide to open the package, and inside, you find a peculiar device with a button. There's a note that says, 'Press the button.'",
        "sound": "Sounds\sos-morse-code_daniel-simion.wav",
        "question": "Do you want to press the button, take the device to an expert, ignore the button, or destroy the device? (press/expert/ignore/destroy): ",
        "choices": {"press": 6, "expert": 7, "ignore": 8, "destroy": 9}
    },
    {
        "path": 3,
        "image": "Images\storyseven_package.jpg",
        "text": "You choose not to open the package and put it aside. You're curious about it but decide to ignore it for now.",
        "question": "Game Over - You didn't explore the mysterious package. You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    },
    {
        "path": 4,
        "image": "Images\storyseven_light.jpg",
        "text": "You press the button, and the device starts beeping. Suddenly, there's a blinding flash of light and a loud explosion!",
        "sound": "Sounds\explosion.wav",
        "question": "Game Over - The mysterious package led to a dangerous outcome. You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    },
    {
        "path": 5,
        "text": "You decide not to press the button and instead read the note more carefully. It reveals a riddle that might lead to a hidden treasure.",
        "sound": "Sounds\sos-morse-code_daniel-simion.wav",
        "question": "Do you want to solve the riddle and embark on a treasure hunt, report the package to the authorities, leave it at a public place, or hand it to a scientist? (solve/report/leave/scientist): ",
        "choices": {"solve": 10, "report": 7, "leave": 8, "scientist": 11}
    },
    {
        "path": 6,
        "image": "Images\storyseven_treasurechest.jpg",
        "text": "You decide to solve the riddle, and it leads you on a thrilling adventure to find hidden treasure. You eventually uncover a chest full of valuable items.",
        "sound": "Sounds\sos-morse-code_daniel-simion.wav",
        "question": "Good job! You've successfully completed the treasure hunt. You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    },
    {
        "path": 7,
        "image": "Images\storyseven_package.jpg",
        "text": "You choose to report the package to the authorities, and they take it away for investigation. The package remains a mystery.",
        "question": "Game Over - You played it safe but missed an adventure. You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    },
    {
        "path": 8,
        "image": "Images\storyseven_package.jpg",
        "text": "You decide to leave the package at a public place, and it gets picked up by someone else. The contents of the package remain unknown to you.",
        "question": "Should you go back for the package or leave it there?",
        "choices": {"Go back": 12, "Leave it": 13}
    },
    {
        "path": 9,
        "image": "Images\storyseven_light.jpg",
        "text": "You decide to destroy the device, and it results in a loud explosion. The package was indeed dangerous.",
        "sound": "Sounds\explosion.wav",
        "question": "Game Over - You attempted to destroy the package, but it caused an explosion. You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    },
    {
        "path": 10,
        "image": "Images\storyseven_treasurechest.jpg",
        "text": "You successfully solve the riddle and embark on a thrilling adventure to find hidden treasure. You eventually uncover a chest full of valuable items.",
        "question": "Good job! You've successfully completed the treasure hunt. You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    },
    {
        "path": 11,
        "text": "You decide to hand the device to a scientist for examination. They thank you and promise to investigate the mysterious package further.",
        "question": "Good job! You contributed to solving the mystery. You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    },
        {
        "path": 12,
        "text": "You decide to go back to the package",
        "question": "Do you want to open it?",
        "choices": {"Yes": 2, "No": 13}
    },
    {
        "path": 13,
        "text": "You didn't open the package in time and someone else got it.",
        "question": "Game Over - You chose to let someone else deal with the package. You can quit the game or hit New Story to play again.",
        "choices": {"Quit Game": None}
    }
]


]
