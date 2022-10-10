import pygame
from resources import *


pygame.init()

if pygame.display.mode_ok((BASE_WIDTH, BASE_HEIGHT), DISPLAY_FLAGS):
    screen = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT), DISPLAY_FLAGS)

run = 1
pygame_time_clock = pygame.time.Clock()

while run:
    pygame_events = pygame.event.get()
    for pygame_event in pygame_events:

        if QUIT == pygame_event.type or (KEYDOWN == pygame_event.type and
                                         pygame_event.key in [K_ESCAPE, K_q]):
            run = 0

    pygame.display.flip()
    pygame_time_clock.tick(40)
