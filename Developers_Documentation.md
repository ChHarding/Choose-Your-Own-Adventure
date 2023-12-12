**Developer’s Guide**
-


**Overview**
Target Audience

Users would be gamers that are looking for entertainment in a unique style game. (Ages 12-40 depending on complexity and plot of the story)
Secondary stakeholders could be game companies that would like to use some aspect of the game on their own.

**Why Is This Important?**
Since choose your own adventure games are becoming more popular, I thought having an image and text based game that would randomize each time would be appealing to users who are looking for these types of games but in a new way.

**What is the primary interaction?**
The primary interaction is the set of options presented at the right side of the game screen. Users choose how they would like the story to go. 
The other main interaction is the “Play New Story” button that runs a randomized story.

**How is data being used?**
All the stories are being stored in a list in a file called stories.py. This file is pulling all the images and sounds being used for each path of the game
Each story has a path, image, text, sound, question, and set of questions
All the images and sounds are stored in their own folders under the root folder of the project
The gam_run py file is the main file that pulls all the data (stories) from the stories file.

**How are the results presented?**
The code is running on tkinter and is using pygame. The code runs and opens the random story screen where a user goes through gameplay. 

**Condensed version of the Final Planning Specs**
- Task Vignettes (User Activity “Flow”)
- Opening the app
- Vignette: 
- The story starts off right away as the user opens up the app. The user will see several UI elements 
- Options - users begin playing through the story
- Play New Story - If user doesn’t like the current game or is done, they can choose a new story to play
- Technical Details:
- Story will randomize each time the user opens up the app and each time they choose a new story to play
- Game Play
- Vignette: 
- User sees an image, text opening up the story and several UI elements (buttons) that are the set of options they need to choose from. 
- Once an option is chosen, they are taken over to the next screen, where there’s an image, text and a set of options. This repeats until the user finishes the story
- There are sounds that play in between scenes to help with the transition and help move the story forward. 
- Technical Details:
- Images needs to match the set of text and options
- Sounds need to match the set of text and options
- Colors and design will match the tone of the story
- Technical “Flow”
- Install pygame
- Import Random to randomize stories. 
- Dictionary for different stories
- Path
- Image
- Text
- Question
- Choices
- List to store all stories
- story_one -> story_ten
- While loop to go through storyline and take player back to another story
- If else statement in while loop that goes back to the beginning and chooses a new story

**Install/deployment/admin issues:**
- Everything that needs to be set up for this program is mentioned in the user’s guide (README.md) file on github. This program isn’t too complex and doesn’t require additional installations.

**(End) User interaction and flow through your code ("walkthrough")**
- The storyflow is mentioned in the user’s guide (README.md) file on github. Images are included of what the step by step process is.
- Images and sounds (stored in separate folders that are pulled into the story.py file
- Stories.py (stores all the stories in a dictionary by different aspects of the game mentioned above)
- Path -> Helps direct where in the story to go to next
- Sound -> complete file name
- Text -> complete file name
- Question -> Question displayed before choices
- Choices -> Choices connect to the different paths (helps with storyflow)
- The main py file runs tkinter
- Everything is stored in (Story.app) to run tkinter
- Def __init__(self) 
- setting up the widgets
- UI elements
- For loop to make sure number of buttons displayed match the number of choices
- Buttons for options and new story
- Def new_story
- While loop to play new story
- If user has played all stories, it should quit the game
- Def process_path
- Defines story flow
- Plays sounds and images if available
- Questions are displayed
- Def play_sound
- Using the pygame mixer
- Def select_choice
- List of choices -> User can choose where to go
- Each path connects to another
- If a path goes to None, user can quit the game
- Def bye
- Shows user the last line of the game


**All issues are mentioned in the user’s guide (all are minor)**

**Future work:**
- Expanding on stories (more complex and intricate) 
- Including more sounds and images
- Fixing the UI more (making the options and text stand out more)
- Having more features available to the user


