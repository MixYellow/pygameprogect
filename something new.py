import math

import pygame
from math import sin, cos, pi, sqrt
from random import randint, choices


# class Tile(pygame.sprite.Sprite):

class MainHero:
    def __init__(self, board_y, board_x, status_of_hero='allright'):
        self.inventory = []
        self.effects = []
        self.status_bar = []
        self.board_y = board_y
        self.board_x = board_x
        self.status_of_hero = status_of_hero

    def get_status_of_hero(self):
        return self.status_of_hero

    def set_status_of_hero(self, what_happend):
        self.status_of_hero = what_happend

    def where_am_i(self):
        self.coords = (self.board_y, self.board_x)
        return self.coords

    def show_inventory(self):
        return self.inventory

    def this_in_inventory(self, item):
        if item in self.inventory:
            return True
        else:
            return False

    def go_to(self, board_y, board_x):
        lst_neighborsEVEN = [(self.board_y - 1, self.board_x - 1), (self.board_y - 2, self.board_x),
                             (self.board_y - 1, self.board_x), (self.board_y + 1, self.board_x),
                             (self.board_y + 2, self.board_x), (self.board_y + 1, self.board_x - 1)]
        lst_neighborsODD = [(self.board_y - 1, self.board_x), (self.board_y - 2, self.board_x),
                            (self.board_y - 1, self.board_x + 1), (self.board_y + 1, self.board_x + 1),
                            (self.board_y + 2, self.board_x), (self.board_y + 1, self.board_x)]

        if self.board_y % 2 == 0:
            if (board_y, board_x) in lst_neighborsEVEN:
                if self.status_bar != []:
                    main_hero.set_status_of_hero(self.status_bar[0])
                    del self.status_bar[0]
                else:
                    main_hero.set_status_of_hero('allright')
                hex_of_board = board.get_board()[board_y][board_x]
                if hex_of_board.get_status() != 'base':
                    hex_of_board.set_status('open')
                self.board_y = board_y
                self.board_x = board_x
        else:
            if (board_y, board_x) in lst_neighborsODD:
                if self.status_bar != []:
                    main_hero.set_status_of_hero(self.status_bar[0])
                    del self.status_bar[0]
                else:
                    main_hero.set_status_of_hero('allright')
                hex_of_board = board.get_board()[board_y][board_x]
                if hex_of_board.get_status() != 'base':
                    hex_of_board.set_status('open')
                self.board_y = board_y
                self.board_x = board_x

    def draw_Hero(self, screen, pos, cell_size):
        statuses_of_heroes = {
            'allright': (42, 178, 98), 'injured': (155, 45, 48), 'sloweddown': (4, 103, 80),  # green, bordo, swamp
            'speedup': (153, 255, 153), 'neardeath': (47, 9, 9)  # light-green, darked-bordo
        }

        pygame.draw.circle(screen, pygame.Color('Black'), pos, cell_size / 1.5, 3)

        # pygame.draw.circle(screen, pygame.Color('black'), pos, cell_size / 1.5)
        pygame.draw.circle(screen, statuses_of_heroes[self.status_of_hero], pos, cell_size / 2)


class Hex:
    def __init__(self, position_x, position_y, territory_status='none', status='close'):
        self.territory_status = territory_status
        self.status = status
        self.position_x = position_x
        self.position_y = position_y

    def __int__(self):
        return self.position_x, self.position_y

    def get_territory_status(self):
        return self.territory_status

    def set_territory_status(self, status):
        self.territory_status = status

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def drawHex(self, screen, pos, cell_size):
        colors_of_types = {
            'lavender': (166, 166, 237), 'field': (245, 222, 179), 'desert': (233, 152, 93),  # lavender, bezevii, pesok
            'trap': (255, 102, 0), 'natives': (128, 64, 48), 'swamp': (172, 183, 142),  # orange, braun, swamp
            'volcano': (46, 48, 54), 'emptiness': (190, 190, 190), 'good_natives': (205, 133, 63),
            # vulcansii, grey, light_braun
            'magma': (200, 116, 84), 'animals': (178, 34, 34)  # rizii, red
        }

        x, y = pos
        points = [(x + cell_size, y), (x + cell_size / 2, y + cell_size * sqrt(3) / 2),
                  (x - cell_size / 2, y + cell_size * sqrt(3) / 2), (x - cell_size, y),
                  (x - cell_size / 2, y - cell_size * sqrt(3) / 2), (x + cell_size / 2, y - cell_size * sqrt(3) / 2)]
        if self.status == 'close':
            pygame.draw.polygon(screen, pygame.Color('white'), points, 1)
        elif self.status == 'open':
            pygame.draw.polygon(screen, colors_of_types[self.territory_status[0]], points)
        elif self.status == 'base':
            pygame.draw.polygon(screen, pygame.Color('Yellow'), points)

    def isBelongingPointToHexagon(self, x1, y1, x2, y2):
        z = Board.__int__(board)
        x, y = abs(x1 - x2), abs(y1 - y2)

        py1 = z * 0.86602540378
        px2 = z * 0.2588190451
        py2 = z * 0.96592582628

        p_angle_01 = -x * (py1 - y) - x * y
        p_angle_20 = -y * (px2 - x) + x * (py2 - y)
        p_angle_03 = y * z
        p_angle_12 = -x * (py2 - y) - (px2 - x) * (py1 - y)
        p_angle_32 = (z - x) * (py2 - y) + y * (px2 - x)

        is_inside_1 = (p_angle_01 * p_angle_12 >= 0) and (p_angle_12 * p_angle_20 >= 0)
        is_inside_2 = (p_angle_03 * p_angle_32 >= 0) and (p_angle_32 * p_angle_20 >= 0)

        return is_inside_1 or is_inside_2

    def inHex(self, pos):
        x2, y2 = self.__int__()
        if Hex.isBelongingPointToHexagon(self, pos[0], pos[1], x2, y2) is True:
            return True
        else:
            return False


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        # значения по умолчанию
        self.left = 30
        self.top = 30
        self.cell_size = 20

        self.height_polygon = self.cell_size * 5
        self.vert = self.cell_size * 1
        self.width_polygon = 2 * self.height_polygon
        self.horiz = self.width_polygon * (1 / 3)

    def __int__(self):
        return self.cell_size

    def prerender(self):
        self.help1 = []
        for _ in range(self.height):
            for __ in range(self.width):
                self.help1.append(Hex((_ % 2) * self.width_polygon * (3 / 18) + __ * self.horiz + self.left,
                                      _ * self.vert + self.top))
            self.board.append(self.help1)
            self.help1 = []
        for ___ in range(self.height):
            for ____ in range(self.width):
                who_it_is = [0, 1, 2]
                who_it_is = choices(who_it_is, weights=[0.3, 0.2, 0.5])[0]
                if who_it_is == 0:
                    who_it_is = choices(lst_of_types_of_hex[0], weights=[0.3, 0.3, 0.4])
                elif who_it_is == 1:
                    who_it_is = choices(lst_of_types_of_hex[1], weights=[0.2, 0.4, 0.3, 0.1])
                else:
                    who_it_is = choices(lst_of_types_of_hex[2], weights=[0.7, 0.0, 0.2, 0.1])
                self.board[___][____].set_territory_status(who_it_is)
        y, x = randint(0, self.height - 1), randint(0, self.width - 1)
        self.board[y][x].set_status('base')
        self.coords_in_lst2 = [y, x]
        return self.coords_in_lst2

    def get_board(self):
        return self.board

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                Hex.drawHex(self.board[y][x], screen,
                            (self.board[y][x].__int__()), self.cell_size)

        hero_y, hero_x = main_hero.where_am_i()
        MainHero.draw_Hero(main_hero, screen, self.board[hero_y][hero_x].__int__(), self.cell_size)

    def on_click(self, pos):
        for yy in range(len(self.board)):
            for xx in range(len(self.board[yy])):
                if self.board[yy][xx].inHex(pos) is True:
                    self.coords_in_lst = [yy, xx]
                    return self.coords_in_lst
        return False


if __name__ == '__main__':
    # pygame.init()
    # infoObject = pygame.display.Info()
    # W, H = infoObject.current_w, infoObject.current_h
    # pygame.display.set_mode((W, H))
    lst_of_types_of_hex = [['lavender', 'field', 'desert'],  # good
                           ['trap', 'natives', 'swamp', 'volcano'],  # bad
                           ['emptiness', 'good_natives', 'magma', 'animals']]  # neutral
    pygame.init()
    pygame.display.set_caption('SpaceColonizer')
    screen = pygame.display.set_mode((400, 400))
    board = Board(5, 17)
    dopcoords = board.prerender()
    score = 0
    main_hero = MainHero(dopcoords[0], dopcoords[1])
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                what = board.on_click(event.pos)
                if what is not False:
                    # board.get_board()[what[0]][what[1]].set_status('open')
                    main_hero.go_to(what[0], what[1])
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

    pygame.quit()
