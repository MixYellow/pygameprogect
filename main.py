import pygame

# origins = ['https://www.redblobgames.com/grids/hexagons/implementation.html',
#  'https://habr.com/ru/post/319644/?_ga=2.213659475.636956551.1670160105-1118741671.1649861395']

# from __future__ import division
# from __future__ import print_function


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('SpaceColonizer')
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
