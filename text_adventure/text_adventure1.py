import sys


stages = [
    {
        "stage": 1,
        "text": "You are Detective John Smith, a seasoned investigator in the city.",
        "question": "One rainy evening, you receive a mysterious phone call. A panicked voice on the other end says, 'Help me, detective! My life is in danger.' Do you want to investigate? (yes/no): ",
        "choices": {"yes": 2, "no": 3}
    },
    {
        "stage": 2,
        "text": "You decide to investigate. The address provided leads you to a dark, abandoned warehouse.",
        "question": "You cautiously enter the building and find a trail of blood leading deeper inside. Do you continue following the trail? (yes/no): ",
        "choices": {"yes": 4, "no": 5}
    },
    {
        "stage": 3,
        "text": "You decide not to investigate and ignore the call. You go about your routine, but you can't shake the feeling that something is amiss. Later that evening, you hear about a murder at the same address. You regret not taking action.",
        "question": "Game Over - You ignored the call, and the case remains unsolved. Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "stage": 4,
        "text": "You follow the trail of blood to a dimly lit room. In the room, you find a person tied to a chair, gagged and injured.",
        "question": "Do you untie the person? (yes/no): ",
        "choices": {"yes": 6, "no": 7}
    },
    {
        "stage": 5,
        "text": "You decide to call for backup and wait outside. While waiting, you hear sirens approaching.",
        "question": "Game Over - Backup arrives, and together you solve the case! Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "stage": 6,
        "text": "You untie the person, and they thank you profusely. They inform you that they witnessed a crime and were being silenced. You decide to take them to safety.",
        "question": "Game Over - You have rescued the witness and solved the case! Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "stage": 7,
        "text": "You leave the person tied up and continue investigating. As you explore further, you hear footsteps approaching.",
        "question": "Suddenly, a shadowy figure emerges from the darkness. They pull out a knife and approach you. Do you confront the figure? (yes/no): ",
        "choices": {"yes": 8, "no": 9}
    },
    {
        "stage": 8,
        "text": "You decide to retreat and find a place to hide. You hear the figure searching for you but manage to escape. You live to fight another day.",
        "question": "Game Over - You managed to escape the danger! Play again? (yes/no): ",
        "choices": {"yes": None, "no": None}
    },
    {
        "stage": 9,
        "text": "You confront the figure, but they overpower you. Your vision fades as you lose consciousness.",
        "question": "Game Over - You have been defeated. (yes/no): ",
        "choices": {"yes": None, "no": None}
    }
]

print("Welcome to Detective Adventure 1!")
current_stage = 1
stage = stages[current_stage - 1] # init with first stage

while True:
    
    # print the text for the current stage
    print(stage["text"])

    # pose the question for the current stage
    # choice will either be yes or no (anything else just repeats the question)
    choice = input(stage["question"]).lower()

    if choice == "yes":
        next_stage = stage["choices"]["yes"]
    elif choice == "no":
        next_stage = stage["choices"]["no"]
    else:
        print("Invalid choice. try again.")
        continue
    
    # None is used to indicate the end of the game
    if next_stage is None:
        print("Thanks for playing!")
        break

    # get next stage from list based on which number was stored for "yes" or "no" in the choices dict
    stage = stages[next_stage - 1]