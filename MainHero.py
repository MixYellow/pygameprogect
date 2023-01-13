import pygame


class MainHero:
    def __init__(self, board_y, board_x, status_of_hero='allright'):
        self.inventory = []
        self.effects = []
        self.status_bar = []
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

    def go_to(self, board_y, board_x, main_hero, board, score):
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
                score += self.pribavka
                self.board_y = board_y
                self.board_x = board_x
                return score
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
                score += self.pribavka
                self.board_y = board_y
                self.board_x = board_x
                return score

    def draw_Hero(self, screen, pos, cell_size):
        statuses_of_heroes = {
            'allright': (42, 178, 98), 'injured': (155, 45, 48), 'sloweddown': (4, 103, 80),  # green, bordo, swamp
            'speedup': (153, 255, 153), 'neardeath': (47, 9, 9)  # light-green, darked-bordo
        }

        pygame.draw.circle(screen, pygame.Color('Black'), pos, cell_size / 1.5, 3)
        pygame.draw.circle(screen, statuses_of_heroes[self.status_of_hero], pos, cell_size / 2)

    def check_position_status(self, board_y, board_x, board):
        status = board.get_board()[board_y][board_x].get_territory_status()



