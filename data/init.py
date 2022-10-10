import pygame
from resources import *
import geometry

def game_loop():
    screen.blit(ball1, ball1_rect)

if __name__ == "__main__":
    pygame.init()

    if pygame.display.mode_ok((BASE_WIDTH, BASE_HEIGHT), DISPLAY_FLAGS):
        screen = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT), DISPLAY_FLAGS)

    run = 1
    pygame_time_clock = pygame.time.Clock()
    ball1, ball1_rect = geometry.render_ball(200, (60, 30, 50))

    while run:
        pygame_events = pygame.event.get()

        for pygame_event in pygame_events:

            if QUIT == pygame_event.type or (KEYDOWN == pygame_event.type and
             pygame_event.key in [K_ESCAPE, K_q]):
            
                run = 0

        game_loop()

        pygame.display.flip()
        pygame_time_clock.tick(40)

