from start import *

def add(name):
    f = open(name, "r")
    exec(f.read())
    f.close()
    globals().update(locals())

print("Starting imports")
#       IMPORTS
import pygame
import time
import random
import ast
import sys
import webbrowser
#   CUSTOM IMPORTS
from configs import *
from colors import *
add("menu.py")
add("screen.py")
print("Imports Finished")

def exit():
    sys.exit()

x = config.display["x"]
y = config.display["y"]
mainScreen = pygame.display.set_mode((x, y))
pygame.display.set_caption(config.display["windowName"])
mainScreen.fill(color.skyBlue)
pygame.display.update()

menu.init()
while True:
    screen.menu.showButtons()
    events = pygame.event.get()
    screen.menu.buttonClick(events, playButton, mpButton, settingButton, exitButton, discordButton, redditButton)
    if discordButton.pressed:
        discordButton.pressed = False
        webbrowser.open('https://discord.gg/2KNxTVEfTY')
    if redditButton.pressed:
        redditButton.pressed = False
        webbrowser.open('https://reddit.com/r/laurabrehd')

exit()
