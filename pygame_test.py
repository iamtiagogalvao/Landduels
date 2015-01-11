import sys
import pygame
from pygame import * # I am using namespace so I don't need to be always calling pygame.something
sys.path.append("classes/cards/")
sys.path.append("classes/")

from starterdeck import*
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
deck = StarterDeck()

### TEXT CONFIGS ###
font_choice={"title" : "res/fonts/title.ttf", "basic" : "res/fonts/basic.ttf",}

font1 = pygame.font.Font(font_choice["title"], 200)
title = font1.render("Land: Duels", True, (white))

font2 = pygame.font.Font(font_choice["basic"], 50)
names = font2.render(deck.magic_cards["name"], True, (white))

### LOAD IMAGES ###
play_button = image.load("res/img/play.png")

card_image = image.load(deck.magic_cards["image"])




### MAIN LOOP ###
while not finished:
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True


        gameDisplay.fill(black)
        gameDisplay.blit(title, (400 - title.get_width() // 2, 100 - title.get_height() // 2))
        gameDisplay.blit(play_button, (400 - play_button.get_width() // 2, 350 - play_button.get_height() // 2))
        gameDisplay.blit(names, (400 - names.get_width() // 2, 400 - names.get_height() // 2))
        gameDisplay.blit(card_image, (400 - card_image.get_width() // 2, 400 - card_image.get_height() // 2))
	
	
    display.update()
    clock.tick(60)

pygame.quit()

