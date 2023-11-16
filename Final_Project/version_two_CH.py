import random
import tkinter as tk
from PIL import Image, ImageTk
import os

print("CWD:", os.getcwd())
os.chdir("Final_Project")

from stories import stories

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

        self.buttons = []
        for i in range(4):  # Create buttons for choices
            button = tk.Button(self, text="", command=lambda i=i: self.select_choice(i), bg = "light blue", fg = "dark blue", font=("Arial", 12))
            self.buttons.append(button)
            button.grid(row=1, column=i, padx=10, pady=10, sticky="w")

        # get random story that hasn't been played yet
        num_stories = len(stories)
        while len(Story_app.past_stories) < num_stories:
            current_story_index = random.randint(0, num_stories-1)
            if current_story_index not in Story_app.past_stories:
                break
        else:
            print("All stories have been played!")
            self.after(2000, self.destroy)

        Story_app.past_stories.append(current_story_index) # remember this story has been played in the class list
        print("past_stories:", Story_app.past_stories)
        self.random_story = stories[current_story_index]
        self.current_location = 1
        self.img_list = []
        self.process_path()

    def process_path(self):
        self.segment = self.random_story[self.current_location - 1]

        self.text_widget.insert("end", self.segment["text"] + "\n")

        if "image" in self.segment:
            image_path = self.segment["image"]
            img = Image.open(image_path)
            img.thumbnail((150, 150))
            imgToInsert = ImageTk.PhotoImage(img)
            self.img_list.append(imgToInsert)
            self.text_widget.image_create("current", image=self.img_list[-1])

          # ask the question for current segment/path
        self.text_widget.insert("end", "\n" * 2 + self.segment['question'])
        
        # jump to the last line
        self.text_widget.see("end")

        choices = list(self.segment["choices"].keys())
        for i, choice in enumerate(choices):
            self.buttons[i].config(text=choice)
            self.buttons[i].config(state="normal")

        for i in range(len(choices), 4):
            self.buttons[i].config(text="")
            self.buttons[i].config(state="disabled")

    def select_choice(self, choice_idx):
        choices = list(self.segment["choices"].keys())
        selected_choice = choices[choice_idx]
        self.current_location = self.segment["choices"][selected_choice]

        if self.current_location is None:
            self.bye()
        else:
            self.process_path()

    def new_story(self):
        self.random_story = random.choice(stories)
        self.current_location = 1
        self.img_list = []
        self.text_widget.delete("1.0", "end")
        self.text_widget.insert("end", "Welcome to The Random Story of the Day!\n\n")
        self.process_path()

    def bye(self):
        self.text_widget.insert("end", "\nThanks for playing! Bye!")
        self.text_widget.update()  # force update to show last line
        self.after(2000, self.destroy)  # Destroy the window after 2 seconds

if __name__ == "__main__":
    app = Story_app()
    app.mainloop()

