import pygame
from Button import *
from Effects import load_image


class Menu:
    def __init__(self, weight, height, cell_size, start_menu='on', sound='on', play_menu='off', choice='on', dop_menu='off', score=10000):  # добавить draw позиции для отрисовки логотипа, кнопок
        self.cell_size = cell_size
        self.start_menu = start_menu
        self.play_menu = play_menu
        self.sound = sound
        self.dop_menu = dop_menu
        self.quiter = Button((weight // 15, height // 9 + 10 * self.cell_size), self.cell_size, 'Quit')
        self.save = Button((weight // 15, height // 9 + 5 * self.cell_size), self.cell_size, 'Save')
        self.training = Button((weight // 2.5, height // 9), self.cell_size, 'Train')
        self.easymode = Button((weight // 1.5, height // 9), self.cell_size, 'Easy')
        self.mediummode = Button((weight // 2.5, height // 2), self.cell_size, 'Medium')
        self.hardmode = Button((weight // 1.5, height // 2), self.cell_size, 'Hard')
        self.backGeneral = Button((weight // 15, height // 9), self.cell_size, 'Back')
        self.play = Button((weight // 15, height // 9), self.cell_size, 'Play')
        self.load = Button((weight // 15, height // 9 + self.cell_size * 5), self.cell_size, 'Load')
        self.soundoff = Button((weight * (2 / 3) + self.cell_size * 3, height * (4 / 5)), self.cell_size // 2,
                          'sound-off', self.cell_size * 1.5)
        self.soundon = Button((weight * (2 / 3) + self.cell_size * 3, height * (4 / 5)), self.cell_size // 2, 'sound-on', self.cell_size * 1.5)
        self.backMenu = Button((weight // 1.425, height // 2), self.cell_size, 'Menu', self.cell_size // 1.7)
        self.save = Button((weight // 1.425, height // 2.6), self.cell_size // 2, 'Save')
        self.miniload = Button((weight // 1.425 + self.cell_size * 4.27, height // 2.6), self.cell_size // 2, 'Load')
        self.end_game = Button((weight // 1.425, height // 2 + self.cell_size * 4.3), self.cell_size, 'End', self.cell_size // 1.7)


        self.status = 'on'
        self.weight = weight
        self.height = height
        self.font = pygame.font.SysFont('Algerian', cell_size * 2)
        self.buttons = []
        self.choice = choice
        self.score = score
        self.dopbuttons = [self.backMenu, self.save, self.miniload, self.end_game]

    def get_buttons(self):
        self.buttons = []
        if self.start_menu == 'off':
            self.buttons = [self.save, self.quiter]
        else:
            if self.sound == 'on' and self.play_menu == 'on':
                self.buttons = [self.backGeneral, self.load, self.soundon, self.quiter,
                                self.training, self.easymode, self.mediummode, self.hardmode, self.backGeneral]
            elif self.sound == 'on' and self.play_menu == 'off':
                self.buttons = [self.play, self.load, self.soundon, self.quiter]
            elif self.sound == 'off' and self.play_menu == 'on':
                self.buttons = [self.backGeneral, self.load, self.soundoff, self.quiter,
                                self.training, self.easymode, self.mediummode, self.hardmode, self.backGeneral]
            elif self.sound == 'off' and self.play_menu == 'off':
                self.buttons = [self.play, self.load, self.soundoff, self.quiter]
        return self.buttons

    def play_menu_change_status(self, change):
        self.play_menu = change

    def ret_score(self):
        return self.score

    def change_score(self, pribavka):
        self.score += pribavka

    def set_sound_status(self, status):
        self.sound = status

    def get_status(self):
        return self.status

    def set_status(self, new):
        self.status = new

    def get_dop_menu_status(self):
        return self.dop_menu

    def ret_dop_buttons(self):
        return self.dopbuttons

    def switch_choice(self, mode):
        self.choice = mode

    def get_choice(self):
        return self.choice

    def show_menu(self, screen, buttons):
        planet = pygame.transform.scale(load_image('planet.png', (self.cell_size * 8, self.cell_size * 8)), (self.cell_size * 13, self.cell_size * 13))
        for button in buttons:
            button.draw(screen, self.cell_size)
            if self.play_menu == 'off':
                screen.blit(self.font.render('Spacecolonizer', True, (255, 0, 0)),
                            (self.weight // 2 - self.cell_size * 3, self.height // 2 + self.cell_size))
                planetrect = planet.get_rect(center=(self.weight // 1.5, self.height // 3.2))
                screen.blit(planet, planetrect)
            else:
                screen.blit(self.font.render('mode:', True, (255, 0, 0)),
                           (self.weight // 2 - self.cell_size * 2.75, self.height // 3))

    def show_buttons_in_game(self, screen, dopbuttons):
        score = str(self.ret_score())
        screen.blit(self.font.render('Score:', True, (255, 0, 0)), (self.weight // 1.38, 0))
        screen.blit(self.font.render('0' * (5 - len(score)) + score, True, (255, 0, 0)), (self.weight // 1.38, self.height // 8))
        pygame.draw.line(screen, (255, 255, 255), (self.weight // 1.5, 0), (self.weight // 1.5, self.height), self.cell_size // 10)
        for button in dopbuttons:
            button.draw(screen, self.cell_size)
