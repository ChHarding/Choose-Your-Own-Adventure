import random
import tkinter as tk
from PIL import Image, ImageTk
import os

print("CWD:", os.getcwd())
os.chdir("Final_Project")

from stories import stories

class Story_app(tk.Tk):
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

        self.random_story = random.choice(stories)
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