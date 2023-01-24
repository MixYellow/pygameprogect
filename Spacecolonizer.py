import pygame
from Board import *
from Hex import *
from Effects import *
from consts import *

if __name__ == '__main__':
    # pygame.init()
    # infoObject = pygame.display.Info()
    # W, H = infoObject.current_w, infoObject.current_h
    # pygame.display.set_mode((W, H))
    pygame.init()
    pygame.display.set_caption('SpaceColonizer')
    screen = pygame.display.set_mode((400, 400))
    board = Board(5, 17)
    dopcoords = board.prerender()
    score = 0
    main_hero = MainHero(dopcoords[0], dopcoords[1])
    addtoall_sprites('boom.png')
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                what = board.on_click(event.pos, board)
                if what is not False:
                    score = main_hero.go_to(what[0], what[1], main_hero, board, score)
                print(score)
                print(main_hero.get_status_of_hero())
        all_sprites.update()
        screen.fill((0, 0, 0))
        board.render(screen, main_hero)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(50)

    pygame.quit()
