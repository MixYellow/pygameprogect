import pygame
from Board import *
from Effects import *
from consts import *
from GameMenu import *
from Button import *
import pickle

if __name__ == '__main__':
    pygame.display.set_mode((W, H))
    pygame.init()
    pygame.display.set_caption('SpaceColonizer')
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    try:
        with open('cfg.txt', 'rb') as f:
            data = pickle.load(f)
            musik_flag = data[2]
            vol = data[0]
            ingamevol = data[1]
            record = data[3]
    except Exception as error:
        with open('cfg.txt', 'wb') as f:
            pickle.dump([1.0, 1.0, 'on'], f)
            data = [1.0, 1.0, 'on', 0]
            musik_flag = data[2]
            vol = data[0]
            ingamevol = data[1]
            record = data[3]
    running = True
    menu_open = 'on'
    while running is True:
        menu = Menu(W, H, H // 20, musik_flag, record)
        game_status = 'lose'
        try:
            pygame.mixer.music.load('sounds/menu.ogg')
            pygame.mixer.music.play(-1)
        except Exception as err:
            pass
        while menu_open == 'on' and running is True:
            musik_flag = menu.get_musik_status()
            try:
                pygame.mixer.music.set_volume(vol)
                if musik_flag == 'on':
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
            except Exception as err:
                pass
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
                            if loadorno == 'endgame':
                                running = False
                                break
                            menu_open = 'off'
                            menu.set_status('off')
                            break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        vol -= 0.1
                    elif event.key == pygame.K_UP:
                        vol += 0.1
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

        try:
            pygame.mixer.music.load('sounds/background.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(ingamevol)
        except Exception as err:
            pass

        while menu_open == 'off' and running is True:
            loadorno = None
            dop_menu = menu.get_dop_menu_status()
            menu_open = menu.get_status()
            try:
                pygame.mixer.music.set_volume(ingamevol)
                if musik_flag == 'on':
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
            except Exception as err:
                pass
            if dop_menu == 'off':
                buttons = menu.ret_dop_buttons()
            else:
                buttons = menu.ret_game_over_buttons()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        ingamevol -= 0.1
                    elif event.key == pygame.K_UP:
                        ingamevol += 0.1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    what = board.on_click(event.pos, board)
                    if what is not False:
                        score = main_hero.go_to(what[0], what[1], main_hero, board, score, cell_size, menu)
                    for button in buttons:
                        loadorno = button.triggered(event.pos, menu, board, cell_size, main_hero, score)
                        if loadorno == 'gg':
                            break
                        if loadorno is not None:
                            cell_size = loadorno[1]
                            board = loadorno[0]
                            main_hero = loadorno[2]
                            score = loadorno[3]
                            menu.set_score(loadorno[4])
                            menu.switch_choice(loadorno[5])
                            break
            if loadorno == 'gg':
                n, r = board.check_win('gg')
                menu.set_dop_menu_buttons('on')
                game_status = 'lose'
                menu.change_score(n * -100 + r * -120)
                if menu.ret_score() > record:
                    record = menu.ret_score()
            if main_hero.get_status_of_hero() == 'death':
                menu.set_dop_menu_buttons('on')
                game_status = 'lose'
                menu.set_score(0)
            if board.check_win() is True:
                menu.set_dop_menu_buttons('on')
                game_status = 'win'
                if menu.ret_score() > record:
                    record = menu.ret_score()

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


    with open('cfg.txt', 'wb') as f:
        data = [vol, ingamevol, musik_flag, record]
        pickle.dump(data, f)
    pygame.quit()