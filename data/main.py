from asyncio import base_subprocess
import pygame
from pygame.locals import *

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

MULT_w_W = MULT_GLOBAL * BASE_W
MULT_w_H = MULT_GLOBAL * BASE_W
def go_forward(point_u_xy, point_u_yx, point_d_xy, point_d_yx):
    point_u_xy = [point_u_xy[0] + (-SCREEN_HEIGHT * MULT_w_H), point_u_xy[1] + (-SCREEN_WIDTH * MULT_w_W)]
    point_u_yx = [point_u_yx[0] + (SCREEN_HEIGHT * MULT_w_H), point_u_yx[1] + (-SCREEN_WIDTH * MULT_w_W)]
    point_d_xy = [point_d_xy[0] + (-SCREEN_HEIGHT * MULT_w_H), point_d_xy[1] + (SCREEN_WIDTH * MULT_w_W)]
    point_d_yx = [point_d_yx[0] + (SCREEN_HEIGHT * MULT_w_H), point_d_yx[1] + (SCREEN_WIDTH * MULT_w_W)]
    return point_u_xy, point_u_yx, point_d_xy, point_d_yx

MULT_s_W = MULT_GLOBAL * BASE_S
MULT_s_H = MULT_GLOBAL * BASE_S
def go_backward(point_u_xy, point_u_yx, point_d_xy, point_d_yx):
    point_u_xy = [point_u_xy[0] + (SCREEN_HEIGHT * MULT_s_H), point_u_xy[1] + (SCREEN_WIDTH * MULT_s_W)]
    point_u_yx = [point_u_yx[0] + (-SCREEN_HEIGHT * MULT_s_H), point_u_yx[1] + (SCREEN_WIDTH * MULT_s_W)]
    point_d_xy = [point_d_xy[0] + (SCREEN_HEIGHT * MULT_s_H), point_d_xy[1] + (-SCREEN_WIDTH * MULT_s_W)]
    point_d_yx = [point_d_yx[0] + (-SCREEN_HEIGHT * MULT_s_H), point_d_yx[1] + (-SCREEN_WIDTH * MULT_s_W)]
    return point_u_xy, point_u_yx, point_d_xy, point_d_yx

MULT_a_W = MULT_GLOBAL * BASE_A
MULT_a_H = MULT_GLOBAL * BASE_A
def go_left(point_u_xy, point_u_yx, point_d_xy, point_d_yx):
    point_u_xy = [point_u_xy[0] + (SCREEN_HEIGHT * MULT_d_H), point_u_xy[1] + (-SCREEN_WIDTH * MULT_d_W)]
    point_u_yx = [point_u_yx[0] + (SCREEN_HEIGHT * MULT_d_H), point_u_yx[1] + (SCREEN_WIDTH * MULT_d_W)]
    point_d_xy = [point_d_xy[0] + (SCREEN_HEIGHT * MULT_d_H), point_d_xy[1] + (SCREEN_WIDTH * MULT_d_W)]
    point_d_yx = [point_d_yx[0] + (SCREEN_HEIGHT * MULT_d_H), point_d_yx[1] + (-SCREEN_WIDTH * MULT_d_W)]
    return point_u_xy, point_u_yx, point_d_xy, point_d_yx

MULT_d_W = MULT_GLOBAL * BASE_D
MULT_d_H = MULT_GLOBAL * BASE_D
def go_right(point_u_xy, point_u_yx, point_d_xy, point_d_yx):
    point_u_xy = [point_u_xy[0] + (-SCREEN_HEIGHT * MULT_d_H), point_u_xy[1] + (SCREEN_WIDTH * MULT_d_W)]
    point_u_yx = [point_u_yx[0] + (-SCREEN_HEIGHT * MULT_d_H), point_u_yx[1] + (-SCREEN_WIDTH * MULT_d_W)]
    point_d_xy = [point_d_xy[0] + (-SCREEN_HEIGHT * MULT_d_H), point_d_xy[1] + (-SCREEN_WIDTH * MULT_d_W)]
    point_d_yx = [point_d_yx[0] + (-SCREEN_HEIGHT * MULT_d_H), point_d_yx[1] + (SCREEN_WIDTH * MULT_d_W)]
    return point_u_xy, point_u_yx, point_d_xy, point_d_yx

def draw_rectangle(screen, point_u_xy, point_u_yx, point_d_xy, point_d_yx):
    pygame.draw.line(screen, COLOR_WHITE, False, ((point_u_xy[0], point_u_xy[1]), (point_u_yx[0], point_u_yx[1])))

def draw_points(screen, point_u_xy, point_u_yx, point_d_xy, point_d_yx):
    screen.fill((COLOR_BLACK))
    pygame.draw.circle(screen, COLOR_WHITE, (point_u_xy[0], point_u_xy[1]), THICKNESS_PUNTO)
    pygame.draw.circle(screen, COLOR_WHITE, (point_u_yx[0], point_u_yx[1]), THICKNESS_PUNTO)
    pygame.draw.circle(screen, COLOR_WHITE, (point_d_xy[0], point_d_xy[1]), THICKNESS_PUNTO)
    pygame.draw.circle(screen, COLOR_WHITE, (point_d_yx[0], point_d_yx[1]), THICKNESS_PUNTO)
    pygame.display.update()

    return screen, point_u_xy, point_u_yx, point_d_xy, point_d_yx

def main():
    pygame.init()
    if pygame.display.mode_ok((SCREEN_WIDTH, SCREEN_HEIGHT), DISPLAY_FLAGS):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DISPLAY_FLAGS)

    point_u_xy = [160, 120]
    point_u_yx = [480, 120]
    point_d_xy = [160, 360]
    point_d_yx = [480, 360]

    run = 1
    clock = pygame.time.Clock()

    while run:
        events = pygame.event.get()

        for event in events:
            if event.type == QUIT or (event.type == KEYDOWN and
                                      event.key in [K_ESCAPE, K_q]):
                run = 0

            if event.type == KEYDOWN and event.key in [K_w]:
                point_u_xy, point_u_yx, point_d_xy, point_d_yx = go_forward(point_u_xy, point_u_yx, point_d_xy, point_d_yx)
            
            if event.type == KEYDOWN and event.key in [K_s]:
                point_u_xy, point_u_yx, point_d_xy, point_d_yx = go_backward(point_u_xy, point_u_yx, point_d_xy, point_d_yx)

            if event.type == KEYDOWN and event.key in [K_a]:
                point_u_xy, point_u_yx, point_d_xy, point_d_yx = go_left(point_u_xy, point_u_yx, point_d_xy, point_d_yx)
            
            if event.type == KEYDOWN and event.key in [K_d]:
                point_u_xy, point_u_yx, point_d_xy, point_d_yx = go_right(point_u_xy, point_u_yx, point_d_xy, point_d_yx)

            screen, point_u_xy, point_u_yx, point_d_xy, point_d_yx = draw_points(screen, point_u_xy, point_u_yx, point_d_xy, point_d_yx)

            screen, point_u_xy, point_u_yx, point_d_xy, point_d_yx = draw_rectangle(screen, point_u_xy, point_u_yx, point_d_xy, point_d_yx)

        pygame.display.flip()
        clock.tick(60)
main()