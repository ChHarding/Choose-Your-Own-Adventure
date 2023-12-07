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


**2. Project User-Journey**
- 

**3. Errors - If possible make a note on errors (i.e. messages that the user might get) and how to fix those.**
- File not found - just make sure you are in the right directory, which should be the root folder (Choose_Your_Own_Adventure). If you need to change directories,
  you can type "cd (path)" - make sure to include the full path (where the folder is saved locally)
- Image or sound file not found - make sure these folders are in the same root folder as py
  
**4. Bugs & Limitations**
- Some of the images show up right next to each other when it should be images per path (set of options)
- The sounds should not play right before the game, they should play right after first option is chosen.
- All questions should should be visible. There are a few paths that are not displaying the question, making it confusing to know option to choose.
