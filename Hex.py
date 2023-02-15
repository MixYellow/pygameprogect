import pygame
from math import sqrt


class Hex:
    # реализация класса игровой клетки
    def __init__(self, position_x, position_y, territory_status, status='close'):
        self.territory_status = territory_status
        self.status = status
        self.position_x = position_x
        self.position_y = position_y

    def __int__(self):
        return self.position_x, self.position_y

    def get_territory_status(self):
        return self.territory_status

    def set_territory_status(self, status):
        self.territory_status = status

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def drawHex(self, screen, pos, cell_size):
        colors_of_types = {
            'lavender': tuple((166, 166, 237)), 'field': tuple((245, 222, 179)), 'desert': tuple((233, 152, 93)),  # lavender, bezevii, pesok
            'trap': tuple((255, 102, 0)), 'natives': tuple((128, 64, 48)), 'swamp': tuple((172, 183, 142)),  # orange, braun, swamp
            'volcano': tuple((46, 48, 54)), 'emptiness': tuple((190, 190, 190)), 'good_natives': tuple((205, 133, 63)),
            # vulcansii, grey, light_braun
            'magma': tuple((200, 116, 84)), 'animals': tuple((178, 34, 34))  # rizii, red
        }

        x, y = pos
        points = [(x + cell_size, y), (x + cell_size / 2, y + cell_size * sqrt(3) / 2),
                  (x - cell_size / 2, y + cell_size * sqrt(3) / 2), (x - cell_size, y),
                  (x - cell_size / 2, y - cell_size * sqrt(3) / 2), (x + cell_size / 2, y - cell_size * sqrt(3) / 2)]
        if self.status == 'close':
            pygame.draw.polygon(screen, pygame.Color('white'), points, 1)
        elif self.status == 'open':
            pygame.draw.polygon(screen, colors_of_types[self.territory_status[0]], points)
        elif self.status == 'base':
            pygame.draw.polygon(screen, pygame.Color('Yellow'), points)

    def isBelongingPointToHexagon(self, x1, y1, x2, y2, board):
        z = board.__int__()
        x, y = abs(x1 - x2), abs(y1 - y2)

        py1 = z * 0.86602540378
        px2 = z * 0.2588190451
        py2 = z * 0.96592582628

        p_angle_01 = -x * (py1 - y) - x * y
        p_angle_20 = -y * (px2 - x) + x * (py2 - y)
        p_angle_03 = y * z
        p_angle_12 = -x * (py2 - y) - (px2 - x) * (py1 - y)
        p_angle_32 = (z - x) * (py2 - y) + y * (px2 - x)

        is_inside_1 = (p_angle_01 * p_angle_12 >= 0) and (p_angle_12 * p_angle_20 >= 0)
        is_inside_2 = (p_angle_03 * p_angle_32 >= 0) and (p_angle_32 * p_angle_20 >= 0)

        return is_inside_1 or is_inside_2

    def inHex(self, pos, board):
        x2, y2 = self.__int__()
        if Hex.isBelongingPointToHexagon(self, pos[0], pos[1], x2, y2, board) is True:
            return True
        else:
            return False
