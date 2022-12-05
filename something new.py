import pygame
from math import sin, cos, pi, sqrt

# class Tile(pygame.sprite.Sprite):

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 30
        self.top = 30
        self.cell_size = 50
        self.height_polygon = self.cell_size * 2
        self.vert = self.cell_size * (1 / 2)
        self.width_polygon = 2 * self.height_polygon
        self.horiz = self.width_polygon * (3 / 7)


    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.polygon(screen, pygame.Color(255, 255, 255),
                                    ([((y % 2) * self.width_polygon * (3 / 14) + x
                                       * self.horiz + self.left + self.cell_size // 2
                                       * cos(2 * pi * i / 6), y * self.vert + self.top
                                       + self.cell_size // 2 * sin(2 * pi * i / 6)) for i in range(6)]), 1)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('SpaceColonizer')
    screen = pygame.display.set_mode((400, 400))

    board = Board(4, 12)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

    pygame.quit()
