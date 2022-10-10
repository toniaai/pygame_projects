import pygame

def render_ball_simple(radius, color):
    size = radius * 2
    surf = pygame.Surface((size, size))
    pygame.draw.circle(surf, color, (radius, radius), radius)

    return surf, surf.get_rect()

def max(x, y):
    if x > y:
        return y
    else:
        return x

def render_ball_funky(radius, color):
    size = radius * 2
    surf = pygame.Surface((size, size))

    increment = int(radius/4)

    for x in range(4):
        iradius = radius - (x * increment)
        print(iradius)

        isize = iradius * 2
        icolor = [0, 0, 0]

        icolor[0] = max(color[0] + (x * 2), 255)
        icolor[1] = max(color[1] + (x * 4), 255)
        icolor[2] = max(color[2] + (x * 3), 255)

        pygame.draw.circle(surf, icolor, (radius, radius), iradius)
    return surf, surf.get_rect()

def render_ball(radius, color):
    return render_ball_funky(radius, color)