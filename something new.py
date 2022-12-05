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
        pygame.draw.line(screen, pygame.Color('white'), (18, 9), (18, 9 + self.cell_size), 2)

    def get_click(self, mouse_pos):
        cell_coords = self.get_cell(mouse_pos)
        if cell_coords is None:
            return
        self.on_click(cell_coords)

    def get_cell(self, mouse_pos):
        board_width = self.width * self.width_polygon
        board_height = self.height * self.height_polygon
        if self.left < mouse_pos[0] < self.left + board_width:
            if self.top < mouse_pos[1] < self.top + board_height:
                cell_coords = (mouse_pos[1] - self.left) // self.cell_size, (mouse_pos[0] - self.top) // self.cell_size
                return cell_coords
        return None

    def on_click(self, cell_coords):
        riad = cell_coords[0] // 50 - self.left // 50
        colonn = cell_coords[1] // 50 - self.top // 50
        if (riad >= 0 and colonn >= 0) and (riad < self.width and colonn < self.height):
            riad = cell_coords[0] // 50 - self.left // 50
            colonn = cell_coords[1] // 50 - self.top // 50
            print(riad, colonn)
        else:
            print(None)



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
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.on_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

    pygame.quit()
