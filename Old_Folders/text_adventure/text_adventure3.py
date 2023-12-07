import sys


 
stages = [
{
    "stage": 1,
    "text": "You are Detective Alex Turner, a renwned investigator with a reputation for solving the toughest cases.",
    "question": "One evening, you receive a cryptic letter with n return address. It contains a riddle and a mysterious key. Do you decipher the riddle and investigate? (y/n): ",
    "choices": {"y": 2, "n": 3}
},
{
    "stage": 2,
    "text": "You decipher the riddle and follow the clues to a hidden underground chamber beneath an old library.",
    "question": "In the chamber, you find a locked chest. You have a key but hesitate to open it. What do you do? (open/leave): ",
    "choices": {"open": 4, "leave": 5}
},
{
    "stage": 3,
    "text": "You disregard the mysterious letter, thinking it's a hoax. Days later, you see a news report about a heist at the same library.",
    "question": "Do you decide to investigate the heist? (y/n): ",
    "choices": {"y": 6, "n": 7}
},
{
    "stage": 4,
    "text": "You open the chest and discover a map leading to an ancient artifact called the 'Eye of Horus.'",
    "question": "The map indicates a perilous journey. Do you embark on the quest to find the artifact? (y/n): ",
    "choices": {"y": 8, "n": 9}
},
{
    "stage": 5,
    "text": "You leave the chest behind and return to the surface. As you exit the library, you ntice a shadowy figure watching you.",
    "question": "Do you confront the figure? (y/n): ",
    "choices": {"y": 10, "n": 11}
},
{
    "stage": 6,
    "text": "You investigate the library heist, discovering a complex web of clues that lead to a ntorious art thief.",
    "question": "Do you decide to track down the thief and recover the stolen artwork? (y/n): ",
    "choices": {"y": 12, "n": 13}
},
{
    "stage": 7,
    "text": "You choose nt to investigate the heist, focusing on other cases. The library heist remains a mystery.",
    "question": "Months later, you receive an annymous tip about the heist. Do you reconsider your decision? (y/n): ",
    "choices": {"y": 6, "n": 14}
},
{
    "stage": 8,
    "text": "You embark on a perilous journey to find the 'Eye of Horus.' Along the way, you encounter challenges and adversaries.",
    "question": "At a crossroads, you find three items: a stone, an apple, and a hammer. Which item do you take with you? (stone/apple/hammer): ",
    "choices": {"stone": 15, "apple": 16, "hammer": 17}
    # Example of how to use multiple choices beyond y or n
},
{
    "stage": 9,
    "text": "You decide nt to pursue the artifact quest and return to your regular cases, leaving the mystery behind.",
    "question": "Years pass, and you wonder about the 'Eye of Horus.' Do you ever revisit the quest? (y/n): ",
    "choices": {"y": 8, "n": None}
},
{
    "stage": 10,
    "text": "You confront the shadowy figure, revealing them as an informant who has valuable information about the library heist.",
    "question": "They offer to help you solve the case. Do you trust them and accept their assistance? (y/n): ",
    "choices": {"y": 18, "n": 19}
},
{
    "stage": 11,
    "text": "You choose nt to confront the figure and instead leave the scene discreetly.",
    "question": "You continue to receive annymous messages from the figure. Do you eventually respond? (y/n): ",
    "choices": {"y": 20, "n": 21}
},
{
    "stage": 12,
    "text": "You track down the art thief and engage in a thrilling chase. You recover the stolen artwork and apprehend the thief.",
    "question": "The case is solved, but you're left with a new mystery regarding the thief's motives. Do you pursue answers? (y/n): ",
    "choices": {"y": 22, "n": 23}
},
{
    "stage": 13,
    "text": "You decide nt to pursue the art thief further, considering the case closed with the recovery of the stolen artwork.",
    "question": "You return to your routine cases but wonder about the thief's hidden agenda. Do you ever reopen the case? (y/n): ",
    "choices": {"y": 12, "n": None}
},
{
    "stage": 14,
    "text": "You reconsider your decision and decide to investigate the heist based on the annymous tip.",
    "question": "The tip leads you to a surprising twist in the case. Do you continue to unravel the mystery? (y/n): ",
    "choices": {"y": 6, "n": None}
},
{
    "stage": 15,
    "text": "You take the stone with you on your quest. It proves to be useful in solving a puzzle along the way.",
    "question": "You make progress toward finding the 'Eye of Horus.' Do you press on? (y/n): ",
    "choices": {"y": 24, "n": 9}
},
{
    "stage": 16,
    "text": "You choose the apple as your companion on the quest. It provides sustenance during challenging moments.",
    "question": "Your journey continues, and you encounter a mysterious orchard. Do you explore it for clues? (y/n): ",
    "choices": {"y": 25, "n": 9}
},
{
    "stage": 17,
    "text": "You opt for the hammer as your tool. It helps you overcome obstacles and clear a blocked path.",
    "question": "As you move forward, you face a massive stone door. Do you attempt to open it with the hammer? (y/n): ",
    "choices": {"y": 26, "n": 9}
},
{
    "stage": 18,
    "text": "You trust the informant and accept their help. Together, you uncover a conspiracy behind the library heist.",
    "question": "The conspiracy leads to powerful figures. Do you confront them to expose the truth? (y/n): ",
    "choices": {"y": 27, "n": 28}
},
{
    "stage": 19,
    "text": "You distrust the informant and reject their assistance, deciding to solve the case independently.",
    "question": "You uncover leads that reveal the informant's hidden agenda. Do you reconsider your decision? (y/n): ",
    "choices": {"y": 18, "n": None}
},
{
    "stage": 20,
    "text": "You eventually respond to the annymous messages, leading to a tense meeting with the shadowy figure.",
    "question": "The figure offers crucial information but demands a favor in return. Do you agree to their terms? (y/n): ",
    "choices": {"y": 29, "n": 30}
},
{
    "stage": 21,
    "text": "You never respond to the annymous messages, and the figure remains a mysterious enigma.",
    "question": "Years pass, and you wonder about the messages' purpose. Do you ever seek answers? (y/n): ",
    "choices": {"y": 20, "n": None}
},
{
    "stage": 22,
    "text": "You pursue answers about the art thief's motives, unveiling a complex scheme involving stolen identities and a secret society.",
    "question": "You expose the secret society's activities. Do you continue investigating their operations? (y/n): ",
    "choices": {"y": 31, "n": 32}
},
{
    "stage": 23,
    "text": "You decide nt to pursue answers about the art thief's motives and focus on more straightforward cases.",
    "question": "The art thief case remains a puzzle in your career. Do you ever revisit it? (y/n): ",
    "choices": {"y": 22, "n": None}
},
{
    "stage": 24,
    "text": "You make progress with the stone, reaching a chamber containing the 'Eye of Horus.'",
    "question": "You've found the artifact, but it's guarded by traps. Do you proceed with caution? (y/n): ",
    "choices": {"y": 33, "n": 34}
},
{
    "stage": 25,
    "text": "You explore the orchard and find a clue that leads you to a hidden passage in your quest.",
    "question": "The passage takes you to a mysterious underground maze. Do you enter it? (y/n): ",
    "choices": {"y": 35, "n": 36}
},
{
    "stage": 26,
    "text": "You use the hammer to open the massive stone door. Inside, you uncover a secret chamber with ancient inscriptions.",
    "question": "The inscriptions offer cryptic guidance. Do you decipher them to proceed? (y/n): ",
    "choices": {"y": 37, "n": 38}
},
{
    "stage": 27,
    "text": "You confront the powerful figures behind the conspiracy, risking your safety to expose the truth.",
    "question": "Your actions lead to a major scandal. Do you embrace your role as a whistleblower? (y/n): ",
    "choices": {"y": 39, "n": 40}
},
{
    "stage": 28,
    "text": "You choose nt to confront the powerful figures, fearing the consequences of exposing the truth.",
    "question": "The conspiracy continues, and you live with the knwledge of their actions. Do you ever reconsider your decision? (y/n): ",
    "choices": {"y": 27, "n": None}
},
{
    "stage": 29,
    "text": "You agree to the figure's terms and perform the favor, which ultimately helps you solve the library heist case.",
    "question": "The figure disappears, leaving you with unanswered questions. Do you search for their whereabouts? (y/n): ",
    "choices": {"y": 41, "n": 42}
},
{
    "stage": 30,
    "text": "You refuse to agree to the figure's terms, opting to solve the case without their help.",
    "question": "You uncover their identity but never establish contact. Do you ever reach out to them? (y/n): ",
    "choices": {"y": 29, "n": None}
},
{
    "stage": 31,
    "text": "You continue investigating the secret society, leading to a final confrontation that exposes their activities.",
    "question": "The society's members are arrested, and justice is served. Do you continue your career as a detective? (y/n): ",
    "choices": {"y": 43, "n": 44}
},
{
    "stage": 32,
    "text": "You become a legendary detective knwn for your role in exposing the secret society.",
    "question": "Your career reaches new heights, but you receive an annymous message hinting at a new mystery. Do you accept the challenge? (y/n): ",
    "choices": {"y": 2, "n": None}
},
{
    "stage": 33,
    "text": "You proceed with caution and successfully retrieve the 'Eye of Horus.' It's a valuable artifact with mystical powers.",
    "question": "The artifact opens new possibilities. Do you use its powers to aid in your future investigations? (y/n): ",
    "choices": {"y": 45, "n": 32}
},
{
    "stage": 34,
    "text": "You choose nt to proceed with caution, triggering a trap that seals the chamber forever.",
    "question": "You return to your regular cases, pondering the lost artifact. Do you ever attempt to recover it? (y/n): ",
    "choices": {"y": 8, "n": None}
},
{
    "stage": 35,
    "text": "You enter the underground maze, facing challenging puzzles and trials.",
    "question": "The maze leads you to a hidden chamber with a valuable clue. Do you continue to explore the maze? (y/n): ",
    "choices": {"y": 46, "n": 9}
},
{
    "stage": 36,
    "text": "You choose nt to enter the underground maze and leave it behind, unresolved.",
    "question": "Years later, you hear rumors of a legendary treasure hidden in the maze. Do you revisit it? (y/n): ",
    "choices": {"y": 35, "n": None}
},
{
    "stage": 37,
    "text": "You decipher the inscriptions, gaining insight into the chamber's secrets and successfully advancing in your quest.",
    "question": "The chamber reveals a passage to the 'Eye of Horus.' Do you proceed through it? (y/n): ",
    "choices": {"y": 33, "n": 34}
},
{
    "stage": 38,
    "text": "You choose nt to decipher the inscriptions, uncertain about their meaning.",
    "question": "You return to the stone door, wondering if there's anther way to proceed. Do you investigate further? (y/n): ",
    "choices": {"y": 47, "n": 34}
},
{
    "stage": 39,
    "text": "You embrace your role as a whistleblower, and the scandal rocks the city's elite.",
    "question": "Your reputation soars, but you receive threats from powerful figures. Do you seek protection? (y/n): ",
    "choices": {"y": 48, "n": 40}
},
{
    "stage": 40,
    "text": "You choose nt to seek protection and face the threats alone, standing your ground.",
    "question": "Years pass, and the conspiracy case remains a defining moment in your career. Do you ever reveal more about it? (y/n): ",
    "choices": {"y": 31, "n": None}
},
{
    "stage": 41,
    "text": "You search for the figure's whereabouts and uncover their true identity, which ties them to the library heist.",
    "question": "You confront the figure, seeking answers about their involvement. Do they reveal their motives? (y/n): ",
    "choices": {"y": 49, "n": 50}
},
{
    "stage": 42,
    "text": "You never search for the figure's whereabouts, leaving their motives a lingering mystery.",
    "question": "The figure's messages continue to haunt you. Do you ever respond to them? (y/n): ",
    "choices": {"y": 41, "n": None}
},
{
    "stage": 43,
    "text": "You continue your career as a detective, taking on challenging cases that come your way.",
    "question": "Your reputation as a legendary detective grows, attracting even more high-profile cases. Do you accept them? (y/n): ",
    "choices": {"y": 2, "n": None}
},
{
    "stage": 44,
    "text": "You choose to step away from the detective life, seeking a quieter and more peaceful existence.",
    "question": "You find solace in your newfound life but wonder if you made the right choice. Do you ever return to your detective career? (y/n): ",
    "choices": {"y": 43, "n": None}
},
{
    "stage": 45,
    "text": "You use the artifact's powers to aid in your investigations, gaining an edge in solving complex cases.",
    "question": "Your success rate soars, but you attract the attention of organizations seeking the artifact's power. Do you protect it at all costs? (y/n): ",
    "choices": {"y": 51, "n": 32}
},
{
    "stage": 46,
    "text": "You explore the maze further and uncover a hidden chamber with ancient relics that could aid in your investigations.",
    "question": "The relics have mysterious properties. Do you take them with you? (y/n): ",
    "choices": {"y": 52, "n": 9}
},
{
    "stage": 47,
    "text": "You investigate further, discovering a hidden mechanism that allows you to bypass the stone door.",
    "question": "Beyond the door, you find a passage leading to the 'Eye of Horus.' Do you continue to the artifact? (y/n): ",
    "choices": {"y": 33, "n": 34}
},
{
    "stage": 48,
    "text": "You seek protection and expose the threats you've received, leading to the arrest of those behind them.",
    "question": "With your safety assured, you continue to take on high-profile cases. Do you maintain your status as a whistleblower? (y/n): ",
    "choices": {"y": 39, "n": 40}
},
{
    "stage": 49,
    "text": "The figure reveals their motives, explaining their coNonection to the library heist and the hidden treasure within the library.",
    "question": "They offer to share the treasure with you. Do you accept their offer? (y/n): ",
    "choices": {"y": 53, "n": 54}
},
{
    "stage": 50,
    "text": "The figure remains silent about their motives, leaving you with unanswered questions.",
    "question": "You continue to receive cryptic messages from them. Do you ever attempt to decipher their meaning? (y/n): ",
    "choices": {"y": 49, "n": None}
},
{
    "stage": 51,
    "text": "You protect the artifact at all costs, even against powerful organizations seeking its power.",
    "question": "Your actions lead to a dangerous pursuit by these organizations. Do you go underground to safeguard the artifact? (y/n): ",
    "choices": {"y": 55, "n": 32}
},
{
    "stage": 52,
    "text": "You take the ancient relics with you, using their mysterious properties to aid in your investigations.",
    "question": "The relics enhance your detective skills, but they draw the attention of a secret society. Do you confront the society? (y/n): ",
    "choices": {"y": 56, "n": 32}
},
{
    "stage": 53,
    "text": "You accept the figure's offer and share the hidden treasure, gaining a valuable ally in future cases.",
    "question": "Your alliance with the figure leads to more mysteries and adventures. Do you continue working together? (y/n): ",
    "choices": {"y": 57, "n": 32}
},
{
    "stage": 54,
    "text": "You decline the figure's offer, preferring to work independently.",
    "question": "The figure disappears, and you continue your detective career alone. Do you ever regret your decision? (y/n): ",
    "choices": {"y": 53, "n": None}
},
{
    "stage": 55,
    "text": "You go underground to safeguard the artifact, becoming a guardian of its power.",
    "question": "Your life takes on a secretive and perilous path. Do you ever reveal the artifact's existence to the world? (y/n): ",
    "choices": {"y": 58, "n": 32}
},
{
    "stage": 56,
    "text": "You confront the secret society, uncovering their sinister plans and putting an end to their activities.",
    "question": "Your actions bring down the society, but they leave behind a legacy of challenges. Do you face those challenges head-on? (y/n): ",
    "choices": {"y": 32, "n": 32}
},
{
    "stage": 57,
    "text": "You continue working together with the figure, solving intricate cases and uncovering hidden secrets.",
    "question": "Your partnership becomes legendary in the world of detectives. Do you ever part ways with the figure? (y/n): ",
    "choices": {"y": 32, "n": None}
},
{
    "stage": 58,
    "text": "You reveal the artifact's existence to the world, leading to a new era of discovery and wonder.",
    "question": "Your actions change the course of history. Do you continue your work as a detective in this new world? (y/n): ",
    "choices": {"y": 32, "n": None}
}
]

print("Welcome to Detective Adventure 3!")
current_stage = 1
stage = stages[current_stage - 1] # init with first stage

while True:
    
    # print the text for the current stage
    print(stage["text"])

    # pose the question for the current stage
    # choice will either be y or n (anything else just repeats the question)
    choice = input(stage["question"]).lower()

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