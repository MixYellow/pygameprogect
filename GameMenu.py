import pygame
from Button import *
from Effects import load_image
import os


class Menu:
    # класс игрового меню
    def __init__(self, weight, height, cell_size, sound, record, start_menu='on', play_menu='off', choice='on', dop_menu='off', score=10000):  # добавить draw позиции для отрисовки логотипа, кнопок
        self.cell_size = cell_size
        self.start_menu = start_menu
        self.play_menu = play_menu
        self.sound = sound
        self.record = record
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
        self.font2 = pygame.font.SysFont('Algerian', cell_size)
        self.buttons = []
        self.choice = choice
        self.score = score
        self.game_over = Button((weight // 15, height // 12 + self.cell_size * 5), self.cell_size * 2, 'Game_over', self.cell_size * 11)
        self.dopbuttons = [self.backMenu, self.save, self.miniload, self.end_game]
        self.gameoverbutton = [self.game_over]

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

    def get_music_status(self):
        return self.sound

    def ret_score(self):
        return self.score

    def change_score(self, pribavka):
        self.score += pribavka

    def set_score(self, new_input):
        self.score = new_input

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

    def ret_game_over_buttons(self):
        return self.gameoverbutton

    def set_dop_menu_buttons(self, new):
        self.dop_menu = new

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

    def show_buttons_in_game(self, screen, dopbuttons, ingamevol=None, game_over='no', k=1, status='lose', n=0):
        if game_over == 'no':
            score = str(self.ret_score())
            screen.blit(self.font.render('Score:', True, (255, 0, 0)), (self.weight // 1.38, 0))
            screen.blit(self.font.render('0' * (5 - len(score)) + score, True, (255, 0, 0)),
                        (self.weight // 1.38, self.height // 8))
            screen.blit(self.font2.render('Record: {}'.format(self.record), True, (255, 0, 0)),
                        (self.weight // 1.41, self.height // 3.75))
            pygame.draw.line(screen, (255, 255, 255), (self.weight // 1.5, 0), (self.weight // 1.5, self.height),
                             self.cell_size // 10)
        else:
            screen.blit(self.font.render('Score: {}'.format(self.ret_score()), True, (255, 0, 0)),
                        (self.weight // 3.5, self.height // 7))
            if status == 'lose':
                if os.path.isfile('sounds\lose.wav') and self.sound == 'on' and n < 1:
                    file = pygame.mixer.Sound('sounds\lose.wav')
                    file.set_volume(ingamevol)
                    file.play()
                screen.blit(self.font.render('You lose'.format(self.ret_score()), True, (255, 0, 0)),
                            (self.weight // 2.8, self.height // 2 + self.cell_size * 6))
            else:
                if os.path.isfile('sounds\Win.wav') and self.sound == 'on' and n < 1:
                    file = pygame.mixer.Sound('sounds\Win.wav')
                    file.set_volume(ingamevol)
                    file.play()
                screen.blit(self.font.render('You win!!'.format(self.ret_score()), True, (255, 0, 0)),
                            (self.weight // 2.8, self.height // 2 + self.cell_size * 6))
        for button in dopbuttons:
            button.draw(screen, self.cell_size * k)
