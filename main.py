import pygame
import os

pygame.init()

#global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("assets/monkey","" )),
           pygame.image.load(os.path.join("assets/monkey","" ))]