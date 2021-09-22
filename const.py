import pygame
pygame.init()
import os

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


#Systems
FPS = 5
WIN_WIDTH = 600
WIN_HEIGHT = 600
FONT = pygame.font.Font(None,50)


#Images
ARCADE_MACHINE_IMAGE = pygame.image.load(os.path.join('Assets','arcadeMachine.png'))
ARCADE_MACHINE = pygame.transform.scale(ARCADE_MACHINE_IMAGE,(55,55))
