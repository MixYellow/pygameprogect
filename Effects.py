import pygame
import os
import sys
from random import choice, randint
from math import sqrt
from consts import EXPLORELST, FLYLST, GRAVITY

pygame.init()
all_sprites = pygame.sprite.Group()



def load_image(name, colorkey=None):
    fullname = os.path.join('img', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, (10, 10))
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def create_particles(position, name, cell_size):
    type = ''
    if name in EXPLORELST:
        type = 'explore'
    elif name in FLYLST:
        type = 'fly'

    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, choice(numbers), choice(numbers), name, cell_size, type)

def addtoall_sprites(name):
    all_sprites = pygame.sprite.Group()
    # создадим спрайт
    sprite = pygame.sprite.Sprite()
    # определим его вид
    sprite.image = load_image(name)
    # и размеры
    sprite.rect = sprite.image.get_rect()
    # добавим спрайт в группу
    all_sprites.add(sprite)


class Particle(pygame.sprite.Sprite):

    def __init__(self, pos, dx, dy, name, radius, type):
        self.pictures = [load_image(name)]
        for scale in (10, 15, 25):
            self.pictures.append(pygame.transform.scale(self.pictures[0], (scale, scale)))
        super().__init__(all_sprites)
        self.image = choice(self.pictures)
        self.rect = self.image.get_rect()
        self.radius = radius

        self.velocity = [dx, dy]
        self.oldrectx, self.oldrecty = pos
        self.rect.x, self.rect.y = pos

        self.gravity = GRAVITY
        self.gravity_x = 0
        self.gravity_y = 0


        if type == 'explore':
            self.gravity_x = randint(-5, 5) / 10
            self.gravity_y = randint(-5, 5) / 10
        elif type == 'fly':
            self.velocity[1] = randint(-2, 0)
            self.velocity[0] = randint(-1, 1)
            self.gravity_y = randint(-1, 0) / 200
            self.gravity = -0.02

    def update(self):
        self.velocity[1] += self.gravity_y
        self.velocity[0] += self.gravity_x

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1] + self.gravity

        if sqrt((self.rect.x - self.oldrectx) ** 2 + (self.rect.y - self.oldrecty) ** 2) > self.radius * 2 or \
                self.velocity[0] == 0 and self.velocity[1] == 0:
            self.kill()


