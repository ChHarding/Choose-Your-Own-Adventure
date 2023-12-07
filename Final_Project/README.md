**How To Get Started (User's Guide)**


**1. Set-Up to Run Code**
   
**VS Code**
- Download VS Code
- Commit the Code from Github to VS Code
  
**Installs in the Command Line** -- *This is what needs to be installed in the terminal first so the imports in the py file can run*
- "pip install pygame"
- "pip install Pillow"
- "pip install tk"

  **random, time and os is already included in python's standard library so pip isn't need to install them. They just need to be included at the top as imports
  for the code to run*

**Folder Set-Up**
- Images and Sounds folders need to be in the same root folder as the py file. If it's all in the same root folder, the sounds and images should run with the code correctly.
![project_folders](https://github.com/kiarachacon/Choose-Your-Own-Adventure/assets/143476708/1e09ec01-66c4-4869-b963-7cef80d041a0)


**2. Project User-Journey**
- Once you run the code, you'll start playing a random story. There will be images for each path of the story and you can click on an option to advance the game. 
![project_game](https://github.com/kiarachacon/Choose-Your-Own-Adventure/assets/143476708/3ff22223-3985-4444-b77c-cc5e219d8fdb)
- The options are to the right hand side of the screen
![project_options](https://github.com/kiarachacon/Choose-Your-Own-Adventure/assets/143476708/452392cc-4792-4a3a-9f3f-98f0fd298f7c)
- Once you reach the end of the game, you'll have the option of quitting the game or starting a new random story
![project_endgame](https://github.com/kiarachacon/Choose-Your-Own-Adventure/assets/143476708/112b91c4-977b-47e3-8435-ce3e0b54e866)
- New story will be at the bottom right of the screen. Quitting the game will take you back to the file.
![project_newstory](https://github.com/kiarachacon/Choose-Your-Own-Adventure/assets/143476708/0174e7d7-1595-4825-a78f-c5c6b34d37c5)


**3. Errors - If possible make a note on errors (i.e. messages that the user might get) and how to fix those.**
- File not found - just make sure you are in the right directory, which should be the root folder (Choose_Your_Own_Adventure). If you need to change directories,
  you can type "cd (path)" - make sure to include the full path (where the folder is saved locally)
- Image or sound file not found - make sure these folders are in the same root folder as py
![project_folders](https://github.com/kiarachacon/Choose-Your-Own-Adventure/assets/143476708/a3178111-b8ee-4b43-80c4-358ef5706ec6)
  
**4. Bugs & Limitations**
- Some of the images show up right next to each other when it should be images per path (set of options)
- The sounds should not play right before the game, they should play right after first option is chosen.
- All questions should be visible. There are a few paths that are not displaying the question, making it confusing to know option to choose.
