import pygame

start = input().split()
try:
    width = float(start[0])
    height = float(start[1])
    if width % 1 != 0 or height % 1 != 0:
        b = 1 / 0
except Exception as error:
    print('Неправильный формат ввода')
    exit()

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('')
    size = width, height
    screen = pygame.display.set_mode(size)

    pygame.draw.rect(screen, pygame.Color('red'), (1, 1, width - 2, height - 2))

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
