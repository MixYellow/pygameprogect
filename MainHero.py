import pygame
from random import choices, randint
from consts import *


class MainHero:
    def __init__(self, board_y, board_x, status_of_hero='allright'):
        self.inventory = []
        self.effects = []
        self.status_bar_health = []
        self.status_bar_speed = []
        self.volcanoses = {}
        self.board_y = board_y
        self.board_x = board_x
        self.status_of_hero = status_of_hero
        self.pribavka = 1

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

    def eruption(self, coords, board):
        coord_y, coord_x = coords
        lst_neighborsEVEN = [[-1, -1], [-2, 0], [-1, 0], [1, 0], [2, 0], [1, -1]]
        lst_neighborsODD = [[-1, 0], [-2, 0], [-1, 1], [1, 1], [2, 0], [1, 0]]

        board.get_board()[coord_y][coord_x].set_territory_status(['magma'])

        if coord_y % 2 == 0:
            for i in range(len(lst_neighborsEVEN)):
                try:
                    board.get_board()[coord_y + lst_neighborsEVEN[i][0]][
                        coord_x + lst_neighborsEVEN[i][1]].set_territory_status(['magma'])
                except Exception as error:
                    pass
        else:
            for i in range(len(lst_neighborsODD)):
                try:
                    board.get_board()[coord_y + lst_neighborsODD[i][0]][
                        coord_x + lst_neighborsODD[i][1]].set_territory_status(['magma'])
                except Exception as error:
                    pass

    def go_to(self, board_y, board_x, main_hero, board, score, last_coords_nat=[-1]):
        lst_neighborsEVEN = [(self.board_y - 1, self.board_x - 1), (self.board_y - 2, self.board_x),
                             (self.board_y - 1, self.board_x), (self.board_y + 1, self.board_x),
                             (self.board_y + 2, self.board_x), (self.board_y + 1, self.board_x - 1)]

        lst_neighborsODD = [(self.board_y - 1, self.board_x), (self.board_y - 2, self.board_x),
                            (self.board_y - 1, self.board_x + 1), (self.board_y + 1, self.board_x + 1),
                            (self.board_y + 2, self.board_x), (self.board_y + 1, self.board_x)]

        if self.board_y % 2 == 0:
            if (board_y, board_x) in lst_neighborsEVEN:
                hex_of_board = board.get_board()[board_y][board_x]
                if hex_of_board.get_status() != 'base':
                    hex_of_board.set_status('open')
                score += self.pribavka
                last_coords = [self.board_y, self.board_x]
                if last_coords_nat != [-1]:
                    last_coords = [last_coords_nat[0], last_coords_nat[1]]
                self.board_y = board_y
                self.board_x = board_x
                self.check_position_status(board_y, board_x, board, last_coords, main_hero, score)
                if str(score) in self.volcanoses:
                    self.eruption(self.volcanoses[str(score)], board)
                if self.status_bar_health == [] and self.status_bar_speed == []:
                    self.status_of_hero = 'allright'
                elif self.status_bar_health != []:
                    self.status_of_hero = self.status_bar_health[0]
                    del self.status_bar_health[0]
                elif self.status_bar_speed != []:
                    self.status_of_hero = self.status_bar_speed[0]
                    del self.status_bar_speed[0]
        else:
            if (board_y, board_x) in lst_neighborsODD:
                hex_of_board = board.get_board()[board_y][board_x]
                if hex_of_board.get_status() != 'base':
                    hex_of_board.set_status('open')
                score += self.pribavka
                last_coords = [self.board_y, self.board_x]
                if last_coords_nat != [-1]:
                    last_coords = [last_coords_nat[0], last_coords_nat[1]]
                self.board_y = board_y
                self.board_x = board_x
                self.check_position_status(board_y, board_x, board, last_coords, main_hero, score)
                if str(score) in self.volcanoses:
                    self.eruption(self.volcanoses[str(score)], board)
                if self.status_bar_health == [] and self.status_bar_speed == []:
                    self.status_of_hero = 'allright'
                elif self.status_bar_health != []:
                    self.status_of_hero = self.status_bar_health[0]
                    del self.status_bar_health[0]
                elif self.status_bar_speed != []:
                    self.status_of_hero = self.status_bar_speed[0]
                    del self.status_bar_speed[0]
        return score

    def draw_Hero(self, screen, pos, cell_size):
        statuses_of_heroes = {
            'allright': (42, 178, 98), 'injured': (155, 45, 48), 'sloweddown': (4, 103, 80),  # green, bordo, swamp
            'speedup': (153, 255, 153), 'neardeath': (47, 9, 9), 'death': (0, 0, 0)  # light-green, darked-bordo, black
        }

        pygame.draw.circle(screen, pygame.Color('Black'), pos, cell_size / 1.5, 3)
        pygame.draw.circle(screen, statuses_of_heroes[self.status_of_hero], pos, cell_size / 2)

    def check_position_status(self, board_y, board_x, board, last_coords, main_hero, score):
        status = board.get_board()[board_y][board_x].get_territory_status()[0]

        library_of_gives = {'lavender': 'lavender flowers', 'field': 'meat', 'desert': 'sand'}

        if status == 'lavender':
            if self.status_bar_health != []:
                self.status_bar_health = []
                self.status_of_hero = 'allright'

        if status == 'lavender' or status == 'field' or status == 'desert':
            drop = library_of_gives[status]
            count_in_inventory = self.inventory.count(drop)
            self.inventory += [drop, drop, drop][0:(3 - count_in_inventory)]
        elif status == 'trap':
            if 'lavender flowers' in self.inventory:
                self.inventory.remove('lavender flowers')
            else:
                if self.status_bar_health != []:
                    self.status_bar_health = ['death']
                    self.status_of_hero = 'death'
                else:
                    self.status_bar_health += DEATHLST
                    self.status_bar_speed = SPEEDDEATHLST
            #     animation??
            board.get_board()[board_y][board_x].set_territory_status(['emptiness'])
        elif status == 'natives':
            if 'lavender flowers' in self.inventory or 'meat' in self.inventory:
                board.get_board()[board_y][board_x].set_territory_status(['good_natives'])
                if 'meat' in self.inventory:
                    self.inventory.remove('meat')
                else:
                    self.inventory.remove('lavender flowers')
            else:
                if self.status_bar_health != []:
                    self.status_of_hero = 'death'
                    self.status_bar_health = ['death']
                else:
                    self.status_bar_health += DEATHLST
                    self.go_to(last_coords[0], last_coords[1], main_hero, board, score - 1,
                               [last_coords[0], last_coords[1]])
                    self.status_bar_speed = SPEEDDEATHLST
        elif status == 'swamp':
            if self.status_bar_speed == [] or 'death' not in self.status_bar_health:
                self.status_bar_speed = SPEEDDOWNLST
        elif status == 'animals':
            if 'meat' in self.inventory:
                self.status_bar_speed = LSTSPEEDUP
                self.inventory.remove('meat')
                board.get_board()[board_y][board_x].set_territory_status(['emptiness'])
            else:
                lucky = choices(['lucky', 'notlucky'], [0.9, 0.1])
                if lucky == 'notlucky':
                    if self.status_bar_health == []:
                        self.status_bar_health += DEATHLST
                        self.go_to(last_coords[0], last_coords[1], main_hero, board, score - 1,
                                   [last_coords[0], last_coords[1]])
                        self.status_bar_speed = SPEEDDEATHLST
                    else:
                        self.status_of_hero = 'death'
                        self.status_bar_health = ['death']
        elif status == 'volcano':
            chance = randint(0, 1000)
            self.volcanoses[str(chance)] = [board_y, board_x]
        
