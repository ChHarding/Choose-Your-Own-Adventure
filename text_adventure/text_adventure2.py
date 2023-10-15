import sys


stages = [
{
    "stage": 1,
    "text": "You are Detective Sarah Miller, known for your sharp instincts and keen intellect.",
    "question": "One sunny morning, you receive a call from a distressed client. They believe their spouse is cheating. Do you agree to take the case? (yes/no): ",
    "choices": {"yes": 2, "no": 3}
},
{
    "stage": 2,
    "text": "You decide to take the case and begin your investigation. You start by tailing the spouse.",
    "question": "While tailing them, you witness the spouse entering a mysterious building. Do you follow them inside? (yes/no): ",
    "choices": {"yes": 4, "no": 5}
},
{
    "stage": 3,
    "text": "You decline the case, not wanting to get involved in a potentially messy situation.",
    "question": "You spend the day in your office working on other cases when you receive another call. It's a mysterious caller asking for your help. Do you agree to meet them? (yes/no): ",
    "choices": {"yes": 6, "no": 7}
},
{
    "stage": 4,
    "text": "You follow the spouse inside the mysterious building. It turns out to be a secret nightclub.",
    "question": "You notice the spouse talking to a suspicious-looking stranger. Do you approach them? (yes/no): ",
    "choices": {"yes": 8, "no": 9}
},
{
    "stage": 5,
    "text": "You decide not to follow the spouse inside the building and return to your office.",
    "question": "Days pass without any significant findings. You receive another call from the distressed client, urging you to do more. Do you reconsider and resume the investigation? (yes/no): ",
    "choices": {"yes": 2, "no": 10}
},
{
    "stage": 6,
    "text": "You agree to meet the mysterious caller. They provide you with evidence of a citywide conspiracy involving powerful figures.",
    "question": "Do you decide to investigate the conspiracy further? (yes/no): ",
    "choices": {"yes": 11, "no": 12}
},
{
    "stage": 7,
    "text": "You decline to meet the mysterious caller, not wanting to get involved in unknown trouble.",
    "question": "Weeks pass, and you continue with your routine cases. You hear rumors of a high-profile case involving a dangerous conspiracy. Do you decide to investigate it? (yes/no): ",
    "choices": {"yes": 13, "no": 14}
},
{
    "stage": 8,
    "text": "You approach the spouse and the stranger, but they turn out to be undercover agents working on a secret case.",
    "question": "They request your assistance in their investigation. Do you agree to join forces? (yes/no): ",
    "choices": {"yes": 15, "no": 16}
},
{
    "stage": 9,
    "text": "You decide not to approach the spouse and maintain your distance.",
    "question": "While observing, you witness the spouse leaving the nightclub alone. Do you continue tailing them? (yes/no): ",
    "choices": {"yes": 17, "no": 18}
},
{
    "stage": 10,
    "text": "You decide not to resume the investigation, and the distressed client hires another detective to continue the case.",
    "question": "You continue with your routine cases but feel a sense of unfinished business. Do you regret your decision? (yes/no): ",
    "choices": {"yes": 19, "no": None}
},
{
    "stage": 11,
    "text": "You dive deeper into the conspiracy and uncover shocking secrets that could bring down powerful individuals.",
    "question": "You realize your life is in danger. Do you go into hiding to protect yourself? (yes/no): ",
    "choices": {"yes": 20, "no": 21}
},
{
    "stage": 12,
    "text": "You decide not to investigate the conspiracy further and continue with your regular cases.",
    "question": "Months later, you hear about a major scandal involving the conspiracy you ignored. Do you wish you had taken action? (yes/no): ",
    "choices": {"yes": 22, "no": None}
},
{
    "stage": 13,
    "text": "You decide to investigate the high-profile conspiracy case, which leads you into a dangerous web of corruption and deceit.",
    "question": "As you dig deeper, you uncover evidence that could expose the entire conspiracy. Do you choose to reveal it? (yes/no): ",
    "choices": {"yes": 23, "no": 24}
},
{
    "stage": 14,
    "text": "You decide not to investigate the conspiracy, wanting to avoid any unnecessary risks.",
    "question": "You continue with your routine cases, but the conspiracy case haunts your thoughts. Do you reconsider your decision? (yes/no): ",
    "choices": {"yes": 13, "no": None}
},
{
    "stage": 15,
    "text": "You join forces with the undercover agents and work together to solve their case, which leads to a major breakthrough in the investigation.",
    "question": "The case ends successfully, but you're left with unanswered questions. Do you seek answers on your own? (yes/no): ",
    "choices": {"yes": 25, "no": 26}
},
{
    "stage": 16,
    "text": "You decline to join forces with the undercover agents, deciding to continue working independently.",
    "question": "As time goes by, you hear about their successful operation, and you wonder if you made the right choice. Do you regret not joining them? (yes/no): ",
    "choices": {"yes": 15, "no": None}
},
{
    "stage": 17,
    "text": "You continue tailing the spouse and discover they are meeting with a divorce lawyer.",
    "question": "You realize your investigation was based on a misunderstanding. Do you inform the client of your findings? (yes/no): ",
    "choices": {"yes": 27, "no": 28}
},
{
    "stage": 18,
    "text": "You decide not to continue tailing the spouse and return to your office.",
    "question": "Days later, the client contacts you, expressing desperation and mistrust. Do you reconsider and resume the investigation? (yes/no): ",
    "choices": {"yes": 2, "no": 29}
},
{
    "stage": 19,
    "text": "You regret not resuming the investigation and feel a sense of missed opportunity.",
    "question": "You hear rumors that the case was eventually solved by another detective, leaving you with lingering doubts. Do you wish you had taken the case? (yes/no): ",
    "choices": {"yes": 2, "no": None}
},
{
    "stage": 20,
    "text": "You go into hiding, but the conspiracy's reach is far and wide. You must remain vigilant to protect your life.",
    "question": "While in hiding, you receive a coded message hinting at a breakthrough in the case. Do you return to investigate further? (yes/no): ",
    "choices": {"yes": 30, "no": 31}
},
{
    "stage": 21,
    "text": "You decide not to go into hiding and continue your regular life, hoping the conspiracy will eventually fade away.",
    "question": "You hear news of the conspiracy being exposed, and justice is served. Do you regret not taking action? (yes/no): ",
    "choices": {"yes": 22, "no": None}
},
{
    "stage": 22,
    "text": "You regret not taking action and wonder what could have been.",
    "question": "You continue with your routine cases, but the missed opportunity continues to weigh on your mind. Do you wish you had made a different choice? (yes/no): ",
    "choices": {"yes": 11, "no": None}
},
{
    "stage": 23,
    "text": "You choose to reveal the evidence, exposing the entire conspiracy and bringing the culprits to justice.",
    "question": "The case gains national attention, and you become a hero detective. Do you continue solving high-profile cases? (yes/no): ",
    "choices": {"yes": 32, "no": 33}
},
{
    "stage": 24,
    "text": "You decide not to reveal the evidence and keep it hidden, fearing the consequences.",
    "question": "The conspiracy continues to haunt you, and you receive threats warning you to stay silent. Do you seek protection from the authorities? (yes/no): ",
    "choices": {"yes": 34, "no": 35}
},
{
    "stage": 25,
    "text": "You seek answers on your own, uncovering a dark secret linked to the conspiracy.",
    "question": "Your investigation leads you to a hidden location. Do you go there to confront the truth? (yes/no): ",
    "choices": {"yes": 36, "no": 37}
},
{
    "stage": 26,
    "text": "You decide not to seek answers on your own and focus on your routine cases.",
    "question": "Years pass, and the mystery continues to intrigue you. Do you ever consider revisiting the case? (yes/no): ",
    "choices": {"yes": 25, "no": None}
},
{
    "stage": 27,
    "text": "You inform the client about the misunderstanding, and they thank you for your honesty.",
    "question": "The client hires you for another case, and you rebuild your professional reputation. Do you continue working as a detective? (yes/no): ",
    "choices": {"yes": 38, "no": 39}
},
{
    "stage": 28,
    "text": "You choose not to inform the client, keeping the misunderstanding hidden.",
    "question": "The client eventually discovers the truth and feels betrayed. Do you try to make amends? (yes/no): ",
    "choices": {"yes": 27, "no": None}
},
{
    "stage": 29,
    "text": "You reconsider and decide to resume the investigation. You discover new leads that take you deeper into the case.",
    "question": "The case becomes a major turning point in your career, and you gain recognition as a skilled detective. Do you embrace your new path? (yes/no): ",
    "choices": {"yes": 40, "no": None}
},
{
    "stage": 30,
    "text": "You return to investigate further, uncovering the final piece of the conspiracy puzzle.",
    "question": "You decide to reveal the evidence, ensuring that justice is served. Do you continue solving complex cases? (yes/no): ",
    "choices": {"yes": 32, "no": 33}
},
{
    "stage": 31,
    "text": "You choose not to return to investigate and live your life in hiding, always looking over your shoulder.",
    "question": "The case continues to haunt your thoughts. Do you ever decide to confront your fears and seek closure? (yes/no): ",
    "choices": {"yes": 25, "no": None}
},
{
    "stage": 32,
    "text": "You continue solving high-profile cases, becoming a legendary detective known for delivering justice.",
    "question": "Your career flourishes, but you wonder if there are more challenges out there. Do you take on a new, mysterious case? (yes/no): ",
    "choices": {"yes": 2, "no": None}
},
{
    "stage": 33,
    "text": "You decide not to continue solving high-profile cases, choosing a quieter life.",
    "question": "You find solace in your peaceful routine, free from the pressures of high-profile investigations. Do you ever look back with regret? (yes/no): ",
    "choices": {"yes": 34, "no": None}
},
{
    "stage": 34,
    "text": "You seek protection from the authorities, revealing the threats you've received.",
    "question": "With their assistance, you expose the culprits behind the threats and bring them to justice. Do you continue working as a detective? (yes/no): ",
    "choices": {"yes": 38, "no": 33}
},
{
    "stage": 35,
    "text": "You choose not to seek protection and face the threats on your own, determined to protect the evidence you hold.",
    "question": "Years pass, and you remain in hiding, guarding the secret. Do you ever decide to reveal it? (yes/no): ",
    "choices": {"yes": 36, "no": None}
},
{
    "stage": 36,
    "text": "You decide to confront the truth, leading to a climactic showdown with the conspirators.",
    "question": "With the evidence exposed, justice is served, but your life is forever changed. Do you continue your work as a detective? (yes/no): ",
    "choices": {"yes": 32, "no": None}
},
{
    "stage": 37,
    "text": "You choose not to confront the truth and continue living your life in uncertainty.",
    "question": "Years pass, and the unresolved mystery remains a shadow in your past. Do you ever decide to revisit the case? (yes/no): ",
    "choices": {"yes": 36, "no": None}
},
{
    "stage": 38,
    "text": "You continue working as a detective, using your experience to solve complex cases.",
    "question": "The end (yes/no)",
    "choices": {"yes": None, "no": None}
}
]

print("Welcome to Detective Adventure 2!")
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