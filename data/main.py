from asyncio import base_subprocess
import pygame
from pygame.locals import *
from math import sqrt

DISPLAY_FLAGS = DOUBLEBUF
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
THICKNESS_PUNTO = 5
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
MULT_GLOBAL = 0.01
BASE_W = 1
BASE_S = 1
BASE_A = 1
BASE_D = 1

WALLS = [((2, 0), (2, 1)), ((3, 0), (3, 1))]
POINTS = [(2,0), (2,1), (3,0), (3,1)]

HORIZON = 240
MAX_DISTANCE = 2
GRID_SIZE = 5
SCREEN_WIDHT_UNIT = SCREEN_WIDTH / GRID_SIZE
SCREEN_HEIGHT_UNIT = SCREEN_HEIGHT / GRID_SIZE

def convert_coordinate_to_pixel(point):
    point_x = point[0]
    point_y = point[1]

    #   
    #               
    #  (0, 0)____________ x 640
    #       |           .
    #       |           .
    #       |   .   .   .
    #        y           (639, 479)
    #       480
    # 

    return (SCREEN_WIDTH/GRID_SIZE * point_x, SCREEN_HEIGHT/GRID_SIZE * point_y)

def euclidean_distance(q, p):
    return sqrt((q[0] - p[0])**2 + (q[1] - p[1])**2)

def is_point_in_distance(q, p, distance):
    return (euclidean_distance(q , p) <= distance)

def is_top_horizon(q):
    return q[1] > HORIZON

def return_points_in_distance(player, distance, points):
    points_in_distance = []
    for point in points:
        if is_point_in_distance(player, point, distance):
            return_points_in_distance.append(point)

def draw_walls(player, walls):

    # check which points are in distance

def main():
    pygame.init()
    if pygame.display.mode_ok((SCREEN_WIDTH, SCREEN_HEIGHT), DISPLAY_FLAGS):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DISPLAY_FLAGS)

    player = [320, 20]

    run = 1
    clock = pygame.time.Clock()

    while run:
        events = pygame.event.get()

        for event in events:
            if event.type == QUIT or (event.type == KEYDOWN and

                                      event.key in [K_ESCAPE, K_q]):
                run = 0



        pygame.display.flip()
        clock.tick(60)



