import random
import tkinter as tk
from PIL import Image, ImageTk
import pygame
import time
import os

from stories import stories

pygame.mixer.init()


class Story_app(tk.Tk):
    past_stories = []  # must be accessed by class name: Story_app.past_stories not self.past_stories!
    def __init__(self):
        super().__init__()
        self.title("Random Story")

        self.text_widget = tk.Text(self, height=20,  wrap="word", bg = 'black', fg ="white", font=("Arial", 14))
        self.text_widget.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.text_widget.insert("end", "Welcome to The Random Story of the Day!\n\n")

        self.scrollbar = tk.Scrollbar(self, command=self.text_widget.yview, bg = "light blue")
        self.scrollbar.grid(row=0, column=3, sticky="ns")
        self.text_widget.config(yscrollcommand=self.scrollbar.set)

        button_frame = tk.Frame(self, bg='black')
        button_frame.grid(row=0, column=4, rowspan=2, padx=10, pady=10, sticky="nsew")


        # Create buttons for choices inside the button frame with rounded corners and centered
        button_width = 20  # Set the desired width
        corner_radius = 10  # Set the desired corner radius

        self.buttons = []
        for i in range(4):
            button = tk.Button(
                button_frame,
                text="",
                command=lambda i=i: self.select_choice(i),
                bg="light blue",
                fg="black",
                font=("Arial", 12),
                width=button_width,
                relief="flat",  # Set the relief to 'flat' for rounded corners
                borderwidth=corner_radius,  # Adjust the corner radius
            )
            self.buttons.append(button)
            button.grid(row=i, column=0, pady=10, sticky="ew")  # Use "ew" to center horizontally

        # Configure weights for grid to allow resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(4, weight=1)

        self.new_story_button = tk.Button(self, text="Play New Story", command=self.new_story, bg="black",
                                          fg="yellow", font=("Arial", 12))
        self.new_story_button.grid(row=1, column=4, padx=10, pady=10, sticky="e")

        self.new_story()

    def new_story(self):
        print("past_stories:", Story_app.past_stories) # show indices of old stories

        # clear the text widget
        self.text_widget.delete("1.0", "end")
        self.text_widget.insert("end", "Welcome to The Random Story of the Day!\n\n")

        # get random story that hasn't been played yet
        num_stories = len(stories)
        while len(Story_app.past_stories) < num_stories:
            current_story_index = random.randint(0, num_stories-1)
            if current_story_index not in Story_app.past_stories:
                 break
        else:
            # Didn't find and return a new story, all stories are done
            # This needs to by a UI message or a dialog box ...
            print("All stories have been played!")
            self.after(2000, self.destroy)

        # remember this story has been played in the class list
        Story_app.past_stories.append(current_story_index) 
        self.random_story = stories[current_story_index]
        
        self.current_location = 1
        self.img_list = []
        self.process_path()  # start new story at the beginning

    def process_path(self):
        self.segment = self.random_story[self.current_location - 1]

        self.text_widget.tag_configure("story", foreground="white")
        self.text_widget.insert("end", self.segment["text"] + "\n", "story")

        if "image" in self.segment:
            image_path = self.segment["image"]
            img = Image.open(image_path)
            img.thumbnail((150, 150))
            imgToInsert = ImageTk.PhotoImage(img)
            self.img_list.append(imgToInsert)
            self.text_widget.image_create("current", image=self.img_list[-1])

        if "sound" in self.segment:
            sound_path = self.segment["sound"]
            self.play_sound(sound_path)

        # ask the question for current segment/path        
        self.text_widget.tag_configure("question", foreground="yellow")
        self.text_widget.insert("end", "\n" * 2 + self.segment['question'] + "\n" * 2, "question")

        # jump to the last line
        self.text_widget.see("end")

        choices = list(self.segment["choices"].keys())
        for i in range(4):
            if i < len(choices):
                self.buttons[i].config(text=choices[i])
                self.buttons[i].config(state="normal")
                self.buttons[i].grid()  # make the button visible
            else:
                self.buttons[i].config(text="")
                self.buttons[i].config(state="disabled")
                self.buttons[i].grid_remove()  # hide the button


    def play_sound(self, file_path):
        try:
            pygame.mixer.music.load(file_path)

            # Play the loaded music file
            pygame.mixer.music.play()

            # while sound is playing, just stay in a sleep state
            while pygame.mixer.music.get_busy():
                time.sleep(0.5)

        except Exception as e:
            print("Error: ", e)



    def select_choice(self, choice_idx):
        choices = list(self.segment["choices"].keys())
        selected_choice = choices[choice_idx]
        self.current_location = self.segment["choices"][selected_choice]

        if self.current_location is None:
            self.bye()
        else:
            self.process_path()

    def bye(self):
        self.text_widget.insert("end", "\nThanks for playing! Bye!")
        self.text_widget.update()  # force update to show last line
        self.after(2000, self.destroy)  # Destroy the window after 2 seconds

if __name__ == "__main__":
    app = Story_app()
    app.mainloop()

