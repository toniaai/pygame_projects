import pygame
from data.resources import *

class Player():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = pygame.image.load(PLAYER_SPRITE)
        self.mask = pygame.mask.from_surface(self.image)