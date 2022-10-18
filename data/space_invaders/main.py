from asyncio import sleep
import pygame
from pygame.locals import *
import random
from math import ceil

DISPLAY_FLAGS = DOUBLEBUF
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 1000

ALIEN_LENGTH = 30
ALIEN_SPACE = 30
ALIEN_COLS = 7
ALIEN_ROWS = 5
ALIEN_MOVEMENT = 10

COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)


def return_leftmost_alien_indices(alien_list):
    max_i = len(alien_list) - 1 - ALIEN_ROWS
    max_x = alien_list[max_i][0]
    max_y = alien_list[max_i][1]

    for i in range(0, len(alien_list)):
        actual_x = int(alien_list[i][0])
        actual_y = int(alien_list[i][1])

        if actual_x > max_x:
            if actual_y < max_y:
                max_i = i
                max_x = actual_x
                max_y = actual_y
    return max_i

def return_rightmost_alien_indices(alien_list):
    max_i = len(alien_list) - 1
    max_x = alien_list[-1][0]
    max_y = alien_list[-1][1]

    for i in range(0, len(alien_list)):
        actual_x = int(alien_list[i][0])
        actual_y = int(alien_list[i][1])

        if actual_x > max_x:
            if actual_y > max_y:
                max_i = i
                max_x = actual_x
                max_y = actual_y
    return max_i
            
def move_aliens(screen, alien_list, direction):
    move_alien_list = []

    if direction == 1:
        # direction = 1 means we are moving to the right!
        ref_alien = alien_list[return_rightmost_alien_indices(alien_list)]

        if ref_alien[0] < SCREEN_WIDTH - (ALIEN_SPACE + ALIEN_LENGTH/2):
            for alien in alien_list:
                moved_alien = [alien[0] + ALIEN_MOVEMENT, alien[1], alien[2]]
                move_alien_list.append(moved_alien)
        else:
            direction = 0
            for alien in alien_list:
                moved_alien = [alien[0], + alien[1] + (ALIEN_SPACE + ALIEN_LENGTH), alien[2]]
                move_alien_list.append(moved_alien)

    else:
        ref_alien = alien_list[return_leftmost_alien_indices(alien_list)]

        if ref_alien[0] > (ALIEN_SPACE + ALIEN_LENGTH/2):

            for alien in alien_list:
                moved_alien = [alien[0] - ALIEN_MOVEMENT, alien[1], alien[2]]
                move_alien_list.append(moved_alien)
        else:
            direction = 1
            for alien in alien_list:
                moved_alien = [alien[0], + alien[1] + (ALIEN_SPACE + ALIEN_LENGTH), alien[2]]
                move_alien_list.append(moved_alien)

    return move_alien_list, direction

def random_updates(alien_list, direction):
    move_first_list = []
    for alien in alien_list:
        if random.random() > 0.5:
            if direction == 1:
                move_first_list.append([alien[0] + ALIEN_MOVEMENT/2, alien[1], alien[2]])
            else:
                move_first_list.append([alien[0] - ALIEN_MOVEMENT/2, alien[1], alien[2]])

    return move_first_list, alien_list

def draw_aliens(screen, alien_list):
    for alien in alien_list:
        if alien[2]:
            pygame.draw.rect(screen, COLOR_WHITE, (alien[0], alien[1], ALIEN_LENGTH, ALIEN_LENGTH))
    
    rightmost_alien = alien_list[return_rightmost_alien_indices(alien_list)]
    leftmost_alien = alien_list[return_leftmost_alien_indices(alien_list)]
    pygame.draw.rect(screen, COLOR_RED, (rightmost_alien[0], rightmost_alien[1], ALIEN_LENGTH, ALIEN_LENGTH))
    pygame.draw.rect(screen, COLOR_RED, (leftmost_alien[0], leftmost_alien[1], ALIEN_LENGTH, ALIEN_LENGTH))
    return alien_list

def generate_aliens():
    alien_list = []

    row_height = SCREEN_HEIGHT*0.1 + ALIEN_LENGTH/2
    col_width = SCREEN_WIDTH*0.1 + ALIEN_LENGTH/2

    for i in range(0, ALIEN_ROWS):
        col_width = SCREEN_WIDTH*0.1 + ALIEN_LENGTH/2
        
        for j in range(0, ALIEN_COLS):
            alien_list.append([col_width, row_height, True])
            col_width = col_width + ALIEN_LENGTH + ALIEN_SPACE
        row_height = row_height + ALIEN_LENGTH + ALIEN_SPACE

    return alien_list


def main():
    pygame.init()
    if pygame.display.mode_ok((SCREEN_WIDTH, SCREEN_HEIGHT), DISPLAY_FLAGS):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DISPLAY_FLAGS)
    
    aliens = generate_aliens()
    direction = 0
    frame = 0
    random.seed(1)
    run = 1
    clock = pygame.time.Clock()

    while run:
        events = pygame.event.get()

        for event in events:
            if event.type == QUIT or (event.type == KEYDOWN and event.key in [K_ESCAPE, K_q]):
                run = 0
            
            keys = pygame.key.get_pressed()

        screen.fill(0) 
        
        # Game action goes here
        aliens = draw_aliens(screen, aliens)
        if frame in [20, 40, 60]:

        
            aliens, direction = move_aliens(screen, aliens, direction)
            first_move, second_move = random_updates(aliens, direction)
            draw_aliens(screen, first_move)
            draw_aliens(screen, second_move)

        pygame.display.flip()
        clock.tick(60)
        frame = frame + 1 if frame < 60 else 0
        print(f'clock: {clock}')


main()
