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
        game_status = 'lose'
        while menu_open == 'on' and running is True:
            loadorno = None
            buttons = [] + menu.get_buttons()
            menu_open = menu.get_status()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        loadorno = button.triggered(event.pos, menu)
                        if loadorno is not None:
                            menu_open = 'off'
                            menu.set_status('off')
                            break
            screen.fill((0, 0, 0))
            menu.show_menu(screen, menu.get_buttons())
            all_sprites.update()
            pygame.display.flip()
            clock.tick(50)

        if loadorno is None:
            choice = menu.get_choice()
            if choice == 'Easy':
                cell_size = H // 20
                board = Board(5, 17, cell_size)
            elif choice == 'Medium':
                cell_size = H // 40
                board = Board(11, 36, cell_size)
            elif choice == 'Hard':
                cell_size = H // 50
                board = Board(14, 47, cell_size)

            dopcoords = board.prerender()
            score = 0
            main_hero = MainHero(dopcoords[0], dopcoords[1])

        else:
            cell_size = loadorno[1]
            board = loadorno[0]
            main_hero = loadorno[2]
            score = loadorno[3]
            menu.set_score(loadorno[4])
            menu.switch_choice(loadorno[5])

        while menu_open == 'off' and running is True:
            loadorno = None
            dop_menu = menu.get_dop_menu_status()
            menu_open = menu.get_status()
            if dop_menu == 'off':
                buttons = menu.ret_dop_buttons()
            else:
                buttons = menu.ret_game_over_buttons()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    what = board.on_click(event.pos, board)
                    if what is not False:
                        score = main_hero.go_to(what[0], what[1], main_hero, board, score, cell_size, menu)
                    for button in buttons:
                        loadorno = button.triggered(event.pos, menu, board, cell_size, main_hero, score)
                        if loadorno is not None:
                            cell_size = loadorno[1]
                            board = loadorno[0]
                            main_hero = loadorno[2]
                            score = loadorno[3]
                            menu.set_score(loadorno[4])
                            menu.switch_choice(loadorno[5])
                            break
            if main_hero.get_status_of_hero() == 'death':
                menu.set_dop_menu_buttons('on')
                game_status = 'lose'
                menu.set_score(0)
            if board.check_win() is True:
                menu.set_dop_menu_buttons('on')
                game_status = 'win'

            screen.fill((0, 0, 0))

            if dop_menu == 'off':
                board.render(screen, main_hero)
                all_sprites.draw(screen)
                all_sprites.update()
                menu.show_buttons_in_game(screen, menu.ret_dop_buttons())
            else:
                menu.show_buttons_in_game(screen, menu.ret_game_over_buttons(), menu, 'yes', 3, game_status)

            pygame.display.flip()
            clock.tick(50)


    pygame.quit()