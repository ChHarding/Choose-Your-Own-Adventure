# Define the stages for the text adventure
stages = [
    {
        "stage": 1,
        "text": "You're a detective summoned to a sprawling mansion to investigate a series of mysterious disappearances.",
        "question": "Do you enter the mansion's grand foyer or decline the case? (Enter/Decline): ",
        "choices": {"Enter": 2, "Decline": 40}
    },
    {
        "stage": 2,
        "text": "The grand foyer is dimly lit, and two ornate doors beckon you, one to the left and one to the right.",
        "question": "Which door do you choose? (Left/Right): ",
        "choices": {"Left": 3, "Right": 4}
    },
    {
        "stage": 3,
        "text": "You enter the left door and find a dusty library filled with ancient books and scrolls.",
        "question": "Do you search for clues or leave the library? (Search/Leave): ",
        "choices": {"Search": 5, "Leave": 2}
    },
    {
        "stage": 4,
        "text": "You enter the right door and discover a luxurious dining room with a massive chandelier overhead.",
        "question": "Do you investigate the dining room or return to the foyer? (Investigate/Return): ",
        "choices": {"Investigate": 6, "Return": 2}
    },
    {
        "stage": 5,
        "text": "While searching the library, you uncover a hidden passage behind a bookshelf, leading deeper into the mansion.",
        "question": "Do you enter the hidden passage or go back to the foyer? (Enter/Return): ",
        "choices": {"Enter": 7, "Return": 3}
    },
    {
        "stage": 6,
        "text": "You explore the dining room and notice a door with an ornate keyhole. It piques your interest.",
        "question": "Do you find the key or return to the foyer? (Find key/Return): ",
        "choices": {"Find key": 8, "Return": 4}
    },
    {
        "stage": 7,
        "text": "You venture into the hidden passage and find yourself in an underground chamber filled with eerie artifacts.",
        "question": "Do you examine the artifacts or return to the library? (Examine/Return): ",
        "choices": {"Examine": 9, "Return": 5}
    },
    {
        "stage": 8,
        "text": "You search for the key and eventually find it hidden in an old cabinet.",
        "question": "Now that you have the key, what's your next move? (Enter passage/Return): ",
        "choices": {"Enter passage": 7, "Return": 6}
    },
    {
        "stage": 9,
        "text": "As you examine the artifacts, you uncover a cryptic message etched into one of them.",
        "question": "Do you decipher the message or return to the library? (Decipher/Return): ",
        "choices": {"Decipher": 10, "Return": 7}
    },
    {
        "stage": 10,
        "text": "You spend time deciphering the message, which reveals a hidden door leading further into the underground chambers.",
        "question": "Do you enter the hidden door or go back to the library? (Enter/Return): ",
        "choices": {"Enter": 11, "Return": 9}
    },
    {
        "stage": 11,
        "text": "You enter the hidden door and find a chamber filled with strange, glowing crystals.",
        "question": "Do you investigate the crystals or return to the previous chamber? (Investigate/Return): ",
        "choices": {"Investigate": 12, "Return": 10}
    },
    {
        "stage": 12,
        "text": "As you investigate the crystals, you begin to feel a strange energy emanating from them.",
        "question": "Do you touch the crystals or leave the chamber? (Touch/Leave): ",
        "choices": {"Touch": 13, "Leave": 11}
    },
    {
        "stage": 13,
        "text": "You cautiously touch one of the crystals, and suddenly, you are transported to a different part of the mansion.",
        "question": "You find yourself in a dark corridor. Do you continue exploring or try to return to where you were? (Explore/Return): ",
        "choices": {"Explore": 14, "Return": 10}
    },
    {
        "stage": 14,
        "text": "As you explore the dark corridor, you come across a locked door.",
        "question": "Do you attempt to pick the lock or return to where you were? (Pick lock/Return): ",
        "choices": {"Pick lock": 15, "Return": 13}
    },
    {
        "stage": 15,
        "text": "You successfully pick the lock, and the door creaks open to reveal a hidden room filled with mysterious artifacts.",
        "question": "Do you examine the artifacts or head back to the corridor? (Examine/Return): ",
        "choices": {"Examine": 16, "Return": 14}
    },
    {
        "stage": 16,
        "text": "As you examine the artifacts, you find a journal that mentions a secret passage in the basement.",
        "question": "Do you go to the basement or return to the corridor? (Basement/Return): ",
        "choices": {"Basement": 17, "Return": 15}
    },
    {
        "stage": 17,
        "text": "You head to the basement and discover a locked door with a keypad.",
        "question": "Do you attempt to crack the code or return to the corridor? (Crack code/Return): ",
        "choices": {"Crack code": 18, "Return": 16}
    },
    {
        "stage": 18,
        "text": "You successfully crack the code and enter the basement, revealing a hidden chamber.",
        "question": "Inside the chamber, you find ancient documents. Do you examine them or leave the basement? (Examine/Leave): ",
        "choices": {"Examine": 19, "Leave": 17}
    },
    {
        "stage": 19,
        "text": "As you examine the documents, you uncover a hidden passage leading deeper into the basement.",
        "question": "Do you enter the hidden passage or leave the basement? (Enter/Leave): ",
        "choices": {"Enter": 20, "Leave": 18}
    },
    {
        "stage": 20,
        "text": "You enter the hidden passage and find yourself in an underground chamber filled with ancient machinery.",
        "question": "Do you investigate the machinery or leave through the passage? (Investigate/Leave): ",
        "choices": {"Investigate": 21, "Leave": 19}
    },
    {
        "stage": 21,
        "text": "While investigating the machinery, you accidentally activate a hidden mechanism that starts the machinery.",
        "question": "Do you try to stop the machinery or run back to the chamber? (Stop machinery/Run back): ",
        "choices": {"Stop machinery": 22, "Run back": 20}
    },
    {
        "stage": 22,
        "text": "You manage to stop the machinery just in time. It appears that it was designed to create a portal to another dimension.",
        "question": "Do you enter the portal or stay in the chamber? (Enter portal/Stay): ",
        "choices": {"Enter portal": 23, "Stay": 21}
    },
    {
        "stage": 23,
        "text": "You step through the portal and find yourself in a strange and otherworldly realm.",
        "question": "Do you explore this realm or try to find a way back through the portal? (Explore/Find portal): ",
        "choices": {"Explore": 24, "Find portal": 21}
    },
    {
        "stage": 24,
        "text": "As you explore the otherworldly realm, you encounter bizarre creatures and unique landscapes.",
        "question": "Do you continue exploring or try to find a way back home? (Explore/Find way back): ",
        "choices": {"Explore": 25, "Find way back": 23}
    },
    {
        "stage": 25,
        "text": "Your exploration leads you to a mysterious temple. Its entrance is guarded by a mystical guardian.",
        "question": "Do you attempt to enter the temple or avoid the guardian? (Enter temple/Avoid guardian): ",
        "choices": {"Enter temple": 26, "Avoid guardian": 24}
    },
    {
        "stage": 26,
        "text": "You face the guardian and, through a series of challenges, gain access to the temple's inner sanctum.",
        "question": "Inside the sanctum, you find a powerful artifact. Do you take it or leave it? (Take/Leave): ",
        "choices": {"Take": 27, "Leave": 25}
    },
    {
        "stage": 27,
        "text": "You take the artifact, and suddenly, you're transported back to the mansion's basement.",
        "question": "You're back in the basement. What will you do now? (Explore/Leave basement): ",
        "choices": {"Explore": 28, "Leave basement": 26}
    },
    {
        "stage": 28,
        "text": "You decide to explore further, but the basement is now different, filled with strange and surreal rooms.",
        "question": "Do you continue exploring or try to find a way back to the mansion? (Explore/Find way back): ",
        "choices": {"Explore": 29, "Find way back": 27}
    },
    {
        "stage": 29,
        "text": "As you explore, you encounter bizarre and surreal challenges, testing your wit and courage.",
        "question": "Do you continue facing the challenges or look for an escape route? (Face challenges/Escape): ",
        "choices": {"Face challenges": 30, "Escape": 28}
    },
    {
        "stage": 30,
        "text": "You overcome the challenges and reach a room with a portal that seems to lead back to the mansion.",
        "question": "Do you enter the portal or hesitate? (Enter portal/Hesitate): ",
        "choices": {"Enter portal": 31, "Hesitate": 29}
    },
    {
        "stage": 31,
        "text": "You step through the portal and find yourself back in the mansion's basement.",
        "question": "Back in the basement, what's your next move? (Explore/Leave basement): ",
        "choices": {"Explore": 32, "Leave basement": 30}
    },
    {
        "stage": 32,
        "text": "You explore the basement once more and stumble upon a secret laboratory filled with strange experiments.",
        "question": "Do you investigate the experiments or leave the basement? (Investigate/Leave): ",
        "choices": {"Investigate": 33, "Leave": 31}
    },
    {
        "stage": 33,
        "text": "While investigating, you find a journal that hints at the mansion's dark secrets and a way to escape the basement.",
        "question": "Do you follow the journal's instructions or leave the basement? (Follow instructions/Leave): ",
        "choices": {"Follow instructions": 34, "Leave": 32}
    },
    {
        "stage": 34,
        "text": "You follow the journal's instructions and discover a hidden passage leading to a locked room.",
        "question": "Do you attempt to unlock the room or leave the basement? (Unlock room/Leave): ",
        "choices": {"Unlock room": 35, "Leave": 33}
    },
    {
        "stage": 35,
        "text": "You successfully unlock the room, revealing a chamber filled with ancient knowledge and a way to return home.",
        "question": "Do you study the ancient knowledge or return home? (Study knowledge/Return): ",
        "choices": {"Study knowledge": 36, "Return": 34}
    },
    {
        "stage": 36,
        "text": "You study the ancient knowledge and gain valuable insights, but now you must make a choice.",
        "question": "What is your ultimate decision? (Use knowledge/Return home): ",
        "choices": {"Use knowledge": 37, "Return home": 35}
    },
    {
        "stage": 37,
        "text": "Your choice to use the ancient knowledge sets in motion events that will reshape your world and the mansion.",
        "question": "(Continue): ",
        "choices": {"Continue": 40}
    },
    {
        "stage": 38,
        "text": "The mansion's mysteries unfold further as you delve deeper into its secrets, and your adventure continues.",
        "question": "(Continue): ",
        "choices": {"Continue": 40}
    },
    {
        "stage": 40,
        "text": "You decline the case and walk away from the mansion. The mystery remains unsolved. Game over.",
        "question": "",
        "choices": {}
    },
]



print("Welcome to Detective Adventure!")
current_stage = 1
stage = stages[current_stage - 1] # init with first stage

while True:
    
    if stage["stage"] == 40:
        print("Thanks for playing!")
        break

    # print the text for the current stage
    print(stage["text"])

    # pose the question for the current stage
    # choice will either be y or n (anything else just repeats the question)
    choice = input(stage["question"])

    valid_choices = stage["choices"].keys()
    if choice not in valid_choices:
        print("Invalid choice. try again.")
        continue

    next_stage = stage["choices"][choice]
    
    # None is used to indicate the end of the game
    if next_stage is None:
        print("Game over! Thanks for playing!")
        break

    # get next stage from list based on which number was stored for "y" or "n" in the choices dict
    stage = stages[next_stage - 1]












# Create a dictionary to map stage numbers to their respective text and questions for easy access.
story_dict = {stage["stage"]: {"text": stage["text"], "question": stage["question"], "choices": stage["choices"]} for stage in story}

# Initialize the story by setting the current stage to the beginning.
current_stage = 1

# Start the story loop.
while True:
    # Check if the current stage is the end of the story.
    if current_stage == 40:
        print("The story has come to an end. Thank you for playing!")
        break

    # Get the current stage's text and question.
    current_stage_info = story_dict[current_stage]
    text = current_stage_info["text"]
    question = current_stage_info["question"]

    # Display the current stage's text and question.
    print(text)
    user_choice = input(question).capitalize()

    # Check if the user's choice is valid and corresponds to a stage.
    if user_choice in current_stage_info["choices"]:
        current_stage = current_stage_info["choices"][user_choice]
    else:
        print("Invalid choice. Please enter a valid option.")
