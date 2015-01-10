import sys
import pygame
from pygame import * # I am using namespace so I don't need to be always calling pygame.something
sys.path.append("classes/cards/")

from Tkinter import*
from card import*
from magiccard import*
from trapcard import*
from creaturecard import*
from actioncard import*
from weapon import*
from armor import*

init()

### DIMENSIONS ###
width = 800
height = 600

##### COLORS #####
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

### CONFIGS, CLOCK SET and LOOP ###

gameDisplay = display.set_mode((width, height))
display.set_caption("LAND: Duels")
clock = time.Clock()
finished = False

### TEXT CONFIGS ###
font = font.Font("res/fonts/title.ttf", 200)
text = font.render("Land: Duels", True, (white))

### LOAD IMAGES ###
play_button = image.load("res/img/play.png")	


### MAIN LOOP ###
while not finished:
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True


        gameDisplay.fill(black)
        gameDisplay.blit(text, (400 - text.get_width() // 2, 100 - text.get_height() // 2))
        gameDisplay.blit(play_button, (400 - play_button.get_width() // 2, 350 - play_button.get_height() // 2))
	
	
    display.update()
    clock.tick(60)

pygame.quit()

