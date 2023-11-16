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

        self.text_widget = tk.Text(self, height=20, wrap="word", bg='black', fg="white", font=("Arial", 14))
        self.text_widget.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.text_widget.insert("end", "Welcome to The Random Story of the Day!\n\n")

        self.scrollbar = tk.Scrollbar(self, command=self.text_widget.yview, bg="light blue")
        self.scrollbar.grid(row=0, column=4, sticky="ns")
        self.text_widget.config(yscrollcommand=self.scrollbar.set)

        self.buttons = []
        for i in range(4):  # Create buttons for choices
            button = tk.Button(self, text="", command=lambda i=i: self.select_choice(i), bg="light blue",
                               fg="dark blue", font=("Arial", 12))
            self.buttons.append(button)
            button.grid(row=1, column=i, padx=10, pady=10, sticky="w")

        self.new_story_button = tk.Button(self, text="Play New Story", command=self.new_story, bg="light green",
                                          fg="dark green", font=("Arial", 12))
        self.new_story_button.grid(row=1, column=4, padx=10, pady=10, sticky="e")

        self.current_story_questions = []  # To store the questions for the current story

        self.new_story()

    def process_path(self):
        self.segment = self.random_story[self.current_location - 1]

        self.text_widget.insert("end", self.segment["text"] + "\n")

        if "question" in self.segment:
            self.current_story_question = self.segment["question"]
            for question in self.current_story_question:
                self.text_widget.insert("end", f"{question}")

        if "image" in self.segment:
            image_path = self.segment["image"]
            img = Image.open(image_path)
            img.thumbnail((150, 150))
            imgToInsert = ImageTk.PhotoImage(img)
            self.img_list.append(imgToInsert)
            self.text_widget.image_create("current", image=self.img_list[-1])

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
        self.text_widget.insert("end", "\nThanks for playing! Do you want to play a new story or quit?")
        self.text_widget.update()  # force update to show last line
        self.new_story_button.config(state="normal")  # Enable the "Play New Story" button

if __name__ == "__main__":
    app = Story_app()
    app.mainloop()

