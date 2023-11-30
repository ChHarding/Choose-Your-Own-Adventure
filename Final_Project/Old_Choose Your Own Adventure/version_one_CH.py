# add imports necessary for the app

import sys
import random
from PIL import Image,ImageTk
import os
import time 

print("CWD:", os.getcwd())
os.chdir("Final_Project")


#structure for game text and choices

from stories import stories


import tkinter as tk

class Story_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Random Story")

        # Create a Text widget that spans all three columns and is 15 lines tall
        self.text_widget = tk.Text(self, height=20,  wrap="word", bg = 'black', fg ="white", font=("Arial", 14))
        self.text_widget.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.text_widget.insert("end","Welcome to The Random Story of the Day!\n\n")

        self.scrollbar = tk.Scrollbar(self, command=self.text_widget.yview, bg = "light blue")
        self.scrollbar.grid(row=0, column=3, sticky="ns")
        self.text_widget.config(yscrollcommand=self.scrollbar.set)

        self.search_button = tk.Button(self, text="Yes", command=self.yes, bg = "light blue", fg = "dark blue", font=("Arial", 12))
        self.search_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.search_button = tk.Button(self, text="No", command=self.no, bg = "light blue", fg = "dark blue", font=("Arial", 12))
        self.search_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.search_button = tk.Button(self, text="New Story", command=self.new_story, bg = "light blue", fg = "dark blue", font=("Arial", 12))
        self.search_button.grid(row=1, column=2, padx=10, pady=10, sticky="w")
      
        self.random_story = random.choice(stories)
        self.current_location = 1
        self.img_list = []
        self.process_path()

    def process_path(self):

        # get current segment from random story, easy b/c it's a list!
        self.segment = self.random_story[self.current_location - 1]

        # show for current segment/path
        self.text_widget.insert("end", self.segment["text"]+"\n" * 2)

        #display the image if a current path in the story has one. 
        if "image" in self.segment:
            image_path = self.segment["image"]
            img = Image.open(image_path)
            
            # convert to 150 x 150 pixels thumbnail
            img.thumbnail((150, 150))

            # convert to tkinter PhotoImage
            imgToInsert = ImageTk.PhotoImage(img)
            self.img_list.append(imgToInsert)

            # insert into text widget
            self.text_widget.image_create("current",image=self.img_list[-1])

        # ask the question for current segment/path
        self.text_widget.insert("end", "\n" * 2 + self.segment['question'])
        
        # jump to the last line
        self.text_widget.see("end")

    # get new locations based on user button click
    def yes(self):
        self.current_location = self.segment["choices"]["yes"]
        if self.current_location is None:
             self.bye()
        else:
            self.process_path()  # next path

    def no(self):
        self.current_location = self.segment["choices"]["no"]
        if self.current_location is None:
             self.bye()
        else:
            self.process_path()

    def new_story(self):    
        self.random_story = random.choice(stories)
        self.current_location = 1
        self.img_list = []
        self.text_widget.delete("1.0", "end")
        self.text_widget.insert("end","Welcome to The Random Story of the Day!\n\n")
        self.process_path()

    def bye(self):
         self.text_widget.insert("end", "\nThanks for playing! Bye!")
         self.text_widget.update() # force update to show last line
         time.sleep(2)
         self.destroy()    


if __name__ == "__main__":
    app = Story_app()
    app.mainloop()

'''
#loop the user to another random story and go through all the different paths for each of the stories
while True:
    random_story = random.choice(stories)
    current_location = 1

    while current_location in range(1, len(random_story) + 1):
        self.segment = [s for s in random_story if s["path"] == current_location][0]

        print(self.segment["text"])

        #display the image if a certain path in the story has one. 
        if "image" in self.segment:
            image_path = self.segment["image"]
            img = Image.open(image_path)
            img.show()

        choice = input(f"{self.segment['question']} ").strip().lower()

        if choice == "yes" and "yes" in self.segment["choices"]:
            current_location = self.segment["choices"]["yes"]
        elif choice == "no" and "no" in self.segment["choices"]:
            current_location = self.segment["choices"]["no"]
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
'''