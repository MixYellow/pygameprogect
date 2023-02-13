import pickle

import pygame


class Button:
    def __init__(self, coord, cell_size, status=None, dobavka=0, col=(0, 0, 0)):
        self.coords = coord
        self.cell_size = cell_size
        self.color = col
        self.status = status
        self.font = pygame.font.SysFont('Algerian', cell_size * 2)
        self.dobavka = dobavka

    def params(self):
        return (self.coords[0], self.coords[1], self.cell_size * 7 + self.dobavka,
                self.cell_size * 4)

    def inButton(self, pos):
        params = self.params()
        if pos[0] > params[0] and pos[1] > params[1] and pos[0] < params[0] + params[2] \
                and pos[1] < params[1] + params[3]:
            return True
        else:
            return False

    def highlighted(self, button):
        self.color = (255, 255, 255)

    def triggered(self, pos, menu, board=None, cell_size=None, main_hero=None, score=None):
        if self.inButton(pos) is True:
            if self.status == 'Play':
                menu.play_menu_change_status('on')
            elif self.status == 'sound-off':
                menu.set_sound_status('on')
            elif self.status == 'sound-on':
                menu.set_sound_status('off')
            elif self.status == 'Quit':
                return 'endgame'
            elif self.status == 'Back':
                menu.play_menu_change_status('off')
            elif self.status == 'Easy':
                menu.switch_choice('Easy')
                menu.set_status('off')
            elif self.status == 'Medium':
                menu.switch_choice('Medium')
                menu.set_status('off')
            elif self.status == 'Hard':
                menu.switch_choice('Hard')
                menu.set_status('off')
            elif self.status == 'Menu':
                menu.switch_choice('on')
                menu.set_status('on')
            elif self.status == 'Save':
                try:
                    data = [board, cell_size, main_hero, score, menu.ret_score(), menu.get_choice()]
                    with open('save.txt', 'wb') as f:
                        pickle.dump(data, f)
                except Exception as error:
                    pass
            elif self.status == 'Load':
                try:
                    with open('save.txt', 'rb') as f:
                        data = pickle.load(f)
                    return data
                except Exception as error:
                    pass
            elif self.status == 'Game_over':
                menu.switch_choice('on')
                menu.set_status('on')
            elif self.status == 'End':
                return 'gg'
            else:
                print(self.status)



    def __int__(self):
        return self.coords

    def draw(self, screen, cell_size):
        pygame.draw.rect(screen, pygame.Color('White'), (self.params()[0], self.params()[1],
                                                         self.params()[2] + self.cell_size // 2,
                                                         self.params()[3]), 0, self.cell_size // 2)
        screen.blit(self.font.render(self.status, True, (255, 0, 0)),
                    (self.coords[0] + self.cell_size // 6, self.coords[1] + cell_size // 1.25))
