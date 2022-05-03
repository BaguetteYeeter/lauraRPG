from start import *

def add(name):
    exec(open(name, "r").read())
    globals().update(locals())

print("Starting imports")
#       IMPORTS
import pygame
import time
import random
import ast
import sys
#   CUSTOM IMPORTS
from configs import *
from colors import *
add("menu.py")
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
    menu.showButtons()

exit()
