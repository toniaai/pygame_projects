import pygame
from pygame.locals import *
from math import sqrt, cos, sin



DISPLAY_FLAGS = DOUBLEBUF
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
THICKNESS_PUNTO = 3
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
MULT_GLOBAL = 0.01
BASE_W = 1
BASE_S = 1
BASE_A = 1
BASE_D = 1

WALLS = [((2, 0), (2, 1)), ((3, 0), (3, 1))]
POINTS = [(2, 0), (2, 1), (3, 0), (3, 1), (1, 1), (1, 2), (3, 2)]

HORIZON = 240
MAX_DISTANCE = 2
GRID_SIZE = 5

SCREEN_WIDHT_UNIT = SCREEN_WIDTH / GRID_SIZE
SCREEN_HEIGHT_UNIT = SCREEN_HEIGHT / GRID_SIZE

# FURTHERS VISION CONE
VISION_Y = 200
FORWARD_DISTANCE = 10
LEFT_EYE_ANGLE = 0.5
RIGHT_EYE_ANGLE = 0.5

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

def sign(point_1, point_2, point_3):
    return (point_1[0] - point_3[0]) * (point_2[1] - point_3[1]) - (point_2[0] - point_3[0]) * (point_1[1] - point_3[1])

def is_in_triangle(point, t_point_1, t_point_2, t_point_3):

    d_1 = sign(point, t_point_1, t_point_2)
    d_2 = sign(point, t_point_2, t_point_3)
    d_3 = sign(point, t_point_3, t_point_1)
    
    is_negative = (d_1 < 0) or (d_2 < 0) or (d_3 < 0)
    is_positive = (d_1 > 0) or (d_2 > 0) or (d_3 > 0)

    return not (is_negative and is_positive)

def draw_map_point(screen, point, player):
    point_l, point_r = draw_player_vision(screen, player)

    if is_in_triangle(convert_coordinate_to_pixel(point), (player[0], player[1]), point_l, point_r):
        pygame.draw.circle(screen, COLOR_RED, convert_coordinate_to_pixel(point), THICKNESS_PUNTO)
    else:
        pygame.draw.circle(screen, COLOR_WHITE, convert_coordinate_to_pixel(point), THICKNESS_PUNTO)

def draw_map_points(screen, points, player):
    for point in points:
        draw_map_point(screen, point, player)

def draw_player(screen, player):
    pygame.draw.circle(screen, COLOR_WHITE, (player[0], player[1]), THICKNESS_PUNTO)

def draw_player_vision(screen, player):
    new_point_f_x_l = cos(player[2] - LEFT_EYE_ANGLE) * (player[0] - player[0]) - sin(player[2] - LEFT_EYE_ANGLE) * ( player[1] + VISION_Y - player[1]) + player[0]
    new_point_f_y_l = sin(player[2] - LEFT_EYE_ANGLE) * (player[0] - player[0]) + cos(player[2] - LEFT_EYE_ANGLE) * ( player[1] + VISION_Y - player[1]) + player[1] 

    new_point_f_x_r = cos(player[2] + RIGHT_EYE_ANGLE) * (player[0] - player[0]) - sin(player[2] + RIGHT_EYE_ANGLE) * ( player[1] + VISION_Y - player[1]) + player[0]
    new_point_f_y_r = sin(player[2] + RIGHT_EYE_ANGLE) * (player[0] - player[0]) + cos(player[2] + RIGHT_EYE_ANGLE) * ( player[1] + VISION_Y - player[1]) + player[1] 

    pygame.draw.line(screen, COLOR_WHITE, (player[0], player[1]), (new_point_f_x_l, new_point_f_y_l), width= 1)
    pygame.draw.line(screen, COLOR_WHITE, (player[0], player[1]), (new_point_f_x_r, new_point_f_y_r), width= 1)
    return (new_point_f_x_l, new_point_f_y_l), (new_point_f_x_r, new_point_f_y_r)

def move_player(player, mode):
    new_point_f_x = cos(player[2]) * (player[0] - player[0]) - sin(player[2]) * ( player[1] + (FORWARD_DISTANCE * mode) - player[1]) + player[0]
    new_point_f_y = sin(player[2]) * (player[0] - player[0]) + cos(player[2]) * ( player[1] + (FORWARD_DISTANCE * mode) - player[1]) + player[1] 

    return [new_point_f_x, new_point_f_y, player[2]]

def main():
    pygame.init()
    if pygame.display.mode_ok((SCREEN_WIDTH, SCREEN_HEIGHT), DISPLAY_FLAGS):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DISPLAY_FLAGS)

    # player = [pos_x, pos_y, vision_angle]
    player = [320, 240, 0]

    run = 1
    clock = pygame.time.Clock()

    while run:
        
        events = pygame.event.get()

        for event in events:
            if event.type == QUIT or (event.type == KEYDOWN and
                                      event.key in [K_ESCAPE, K_q]):
                run = 0
            
            keys = pygame.key.get_pressed()

            if keys[K_a]:
                player = [player[0], player[1], player[2] - 0.1]
            
            if keys[K_d]:
                player = [player[0], player[1], player[2] + 0.1]
            
            if keys[K_w]:
                player = move_player(player, 1)
            
            if keys[K_s]:
                player = move_player(player, -1)

        screen.fill(0) 
        
        draw_player(screen, player)
        _, _ = draw_player_vision(screen, player)
        draw_map_points(screen, POINTS, player)

        
        pygame.display.flip()
        clock.tick(60)


main()
