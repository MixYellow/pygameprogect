import pygame
from Board import *
from Hex import *
from Effects import *
from consts import *
from GameMenu import *
from Button import *

if __name__ == '__main__':
    pygame.display.set_mode((W, H))
    pygame.init()
    pygame.display.set_caption('SpaceColonizer')
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()

    running = True
    menu_open = 'on'
    while running is True:
        menu = Menu(W, H, H // 20)
        while menu_open == 'on' and running is True:
            buttons = [] + menu.get_buttons()
            menu_open = menu.get_status()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        button.triggered(event.pos, menu)
            screen.fill((0, 0, 0))
            menu.show_menu(screen, menu.get_buttons())
            all_sprites.update()
            pygame.display.flip()
            clock.tick(50)

        board = Board(5, 17, cell_size)

        choice = menu.get_choice()
        if choice == 'Easy':
            cell_size = H // 20
            board = Board(5, 17, cell_size)
        if choice == 'Medium':
            cell_size = H // 40
            board = Board(10, 35, cell_size)
        dopcoords = board.prerender()
        score = 0
        main_hero = MainHero(dopcoords[0], dopcoords[1])

        while menu_open == 'off' and running is True:
            dop_menu = menu.get_dop_menu_status()
            menu_open = menu.get_status()
            if dop_menu == 'off':
                buttons = menu.ret_dop_buttons()
            else:
                buttons = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    what = board.on_click(event.pos, board)
                    if what is not False:
                        score = main_hero.go_to(what[0], what[1], main_hero, board, score)
                    for button in buttons:
                        button.triggered(event.pos, menu)

            screen.fill((0, 0, 0))
            board.render(screen, main_hero)
            all_sprites.draw(screen)
            all_sprites.update()
            menu.show_buttons_in_game(screen, menu.ret_dop_buttons())
            pygame.display.flip()
            clock.tick(50)

    pygame.quit()