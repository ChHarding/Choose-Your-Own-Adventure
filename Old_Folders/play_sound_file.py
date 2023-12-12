import pygame # pip install pygame
import time
import os

# Initialize sound mixer. Do this only once, at the beginning of your program!
pygame.mixer.init()

def play_sound(file_path):
    try:
        pygame.mixer.music.load(file_path)

        # Play the loaded music file
        pygame.mixer.music.play()

        # while sound is playing, just stay in a sleep state
        while pygame.mixer.music.get_busy():
            time.sleep(0.5)

    except Exception as e:
        print("Error: ", e)

# Example usage
os.chdir("Final_Project")

print("wav")
play_sound("Sounds/sos-morse-code_daniel-simion.wav")

print("mp3")
play_sound("Sounds/sos-morse-code_daniel-simion.mp3")