from Hex import *
from MainHero import MainHero
from consts import lst_of_types_of_hex
from random import randint, choices


class Board:
    # создание поля
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.board = []
        # значения по умолчанию
        self.left = cell_size * 3
        self.top = cell_size * 2
        self.cell_size = cell_size

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
                who_it_is = [0, 1, 2]
                who_it_is = choices(who_it_is, weights=[0.3, 0.2, 0.5])[0]
                if who_it_is == 0:
                    who_it_is = choices(lst_of_types_of_hex[0], weights=[0.3, 0.3, 0.4])
                elif who_it_is == 1:
                    who_it_is = choices(lst_of_types_of_hex[1], weights=[0.2, 0.4, 0.4])
                else:
                    who_it_is = choices(lst_of_types_of_hex[2], weights=[0.68, 0.0, 0.2, 0.1, 0.02])

                self.help1.append(Hex((_ % 2) * self.width_polygon * (3 / 18) + __ * self.horiz + self.left,
                                      _ * self.vert + self.top, who_it_is))

            self.board.append(self.help1)
            self.help1 = []
        y, x = randint(0, self.height - 1), randint(0, self.width - 1)
        self.board[y][x].set_status('base')
        self.board[y][x].set_territory_status('emptiness')
        self.coords_in_lst2 = [y, x]
        return self.coords_in_lst2

    def get_board(self):
        return self.board

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen, main_hero):
        for y in range(self.height):
            for x in range(self.width):
                Hex.drawHex(self.board[y][x], screen,
                            (self.board[y][x].__int__()), self.cell_size)

        hero_y, hero_x = main_hero.where_am_i()
        MainHero.draw_Hero(main_hero, screen, self.board[hero_y][hero_x].__int__(), self.cell_size)

    def on_click(self, pos, board):
        for yy in range(len(self.board)):
            for xx in range(len(self.board[yy])):
                if self.board[yy][xx].inHex(pos, board) is True:
                    self.coords_in_lst = [yy, xx]
                    return self.coords_in_lst
        return False

    def check_win(self):
        flagopen = True
        flagbed = True
        for yy in range(len(self.board)):
            for xx in range(len(self.board[yy])):
                if self.board[yy][xx].get_status() == 'close':
                    flagopen = False
                if self.board[yy][xx].get_territory_status()[0] in lst_of_types_of_hex[1]:
                    flagbed = False
        if flagbed is True and flagopen is True:
            return True
        return False

