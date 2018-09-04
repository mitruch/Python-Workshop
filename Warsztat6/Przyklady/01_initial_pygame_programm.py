# zgapione z książki: http://inventwithpython.com/pygame
import pygame, sys
from pygame.locals import * #trzeba uwazac zeby nie nadpisac sobie zmiennych 

pygame.init() #inicjalizacja pygame
DISPLAYSURF = pygame.display.set_mode((400, 300)) #inicjalizacja powierzchni której bedziemy uzywac #okienko 
pygame.display.set_caption('Hello World!') #ustawiamy tytul okienka
while True: # main game loop
    for event in pygame.event.get(): #pygejmowe eventy
        if event.type == QUIT:
            pygame.quit() #sprzatamy po sobie
            sys.exit() #zamykamy okienko
    pygame.display.update() #jezeli nie quit to update