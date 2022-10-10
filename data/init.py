import pygame
from resources import *
import main


pygame.init()

if pygame.display.mode_ok((BASE_WIDTH, BASE_HEIGHT), DISPLAY_FLAGS):
    screen = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT), DISPLAY_FLAGS)

run = 1
pygame_time_clock = pygame.time.Clock()
ball1, ball1_rect = main.render_ball(200, (60, 30, 50))

while run:
    pygame_events = pygame.event.get()
    for pygame_event in pygame_events:

        if QUIT == pygame_event.type or (KEYDOWN == pygame_event.type and
                                         pygame_event.key in [K_ESCAPE, K_q]):
            run = 0

    screen.blit(ball1, ball1_rect)

    
    pygame.display.flip()
    
    # GAME FPS, ALWAYS LAST
    pygame_time_clock.tick(40)
