import pygame
import os
import sys
from random import choice, randint
from math import sqrt
from consts import EXPLORELST, FLYLST, GRAVITY, DROPLST, ONETIMELST, FALLINGLST, JUMPINGLST, ATTACKLST, H, W

pygame.init()
all_sprites = pygame.sprite.Group()
# реализация эффектов внутри игры


def load_image(name, size=(10, 10), colorkey=None):
    fullname = os.path.join('img', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, size)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def create_particles(position, name, cell_size):
    types = ''
    if name in EXPLORELST:
        types = 'explore'
    elif name in FLYLST:
        types = 'fly'
    elif name in DROPLST:
        types = 'drop'
    elif name in ONETIMELST:
        types = 'big'
    elif name in FALLINGLST:
        types = 'fall'
    elif name in JUMPINGLST:
        types = 'up'
    elif name in ATTACKLST:
        types = 'attack'

    # количество создаваемых частиц
    if types == 'drop':
        particle_count = 3
    elif types == 'big':
        particle_count = 1
    elif types == 'fall' or types == 'up' or types == 'attack':
        particle_count = 5
    else:
        particle_count = 20

    # возможные скорости
    # numbers = range(-5, 6)
    numbers = range(-1, 2)
    for _ in range(particle_count):
        Particle(position, choice(numbers), choice(numbers), name, cell_size, types)


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

    def __init__(self, pos, dx, dy, name, radius, types):
        self.types = types
        if types == 'drop' or types == 'attack':
            self.pictures = [load_image(name, (radius // 1.5, radius // 1.5))]
            for scale in (radius // 1.5, radius // 1.5 + 5, radius // 1.5 + 10):
                self.pictures.append(pygame.transform.scale(self.pictures[0], (scale, scale)))
        elif types == 'big':
            self.pictures = [load_image(name, (radius, radius))]
            self.pictures.append(pygame.transform.scale(self.pictures[0], (radius, radius)))
        elif types == 'fall' or types == 'up':
            self.pictures = [load_image(name, (radius // 2, radius // 2))]
            for scale in (radius // 2, radius // 2 + 5, radius // 2 + 10):
                self.pictures.append(pygame.transform.scale(self.pictures[0], (scale, scale)))
        else:
            self.pictures = [load_image(name, (radius // 2, radius // 2))]
            for scale in (radius // 3, radius // 2 + 5, radius // 2 + 10):
                self.pictures.append(pygame.transform.scale(self.pictures[0], (scale, scale)))
        super().__init__(all_sprites)
        self.image = choice(self.pictures)
        self.rect = self.image.get_rect()
        self.radius = radius
        self.flagdrop = False

        self.velocity = [dx, dy]
        if types == 'fall':
            self.rect.x, self.rect.y = pos[0], pos[1] - radius // 2
            self.oldrectx, self.oldrecty = pos
        elif types == 'attack':
            self.rect.x, self.rect.y = pos[0] + randint(-radius, radius), pos[1] + randint(-radius, radius)
            self.oldrectx, self.oldrecty = pos
        else:
            self.oldrectx, self.oldrecty = pos
            self.rect.x, self.rect.y = pos

        self.gravity = GRAVITY
        self.gravity_x = 0
        self.gravity_y = 0

        if types == 'explore':
            self.gravity_x = randint(-5, 5) / 10
            self.gravity_y = randint(-5, 5) / 10
        elif types == 'fly':
            self.velocity[1] = randint(-2, 0)
            self.velocity[0] = randint(-1, 1)
            self.gravity_y = randint(-1, 0) / 200
            self.gravity = -0.02
        elif types == 'fall':
            self.rect.x = self.rect.x + randint(-radius // 2.5, radius // 2.5)
            self.gravity_y = randint(-1, 0) / 200
            self.gravity = 1
        elif types == 'up':
            self.rect.x = self.rect.x + randint(-radius // 3, radius // 3)
            self.gravity_y = randint(-1, 0) / 200
            self.gravity = -1
        elif types == 'big':
            self.gravity = -1

    def update(self):
        if self.rect.y >= H:
            self.kill()
        elif self.rect.y <= 0:
            self.kill()
        elif self.rect.x <= 0:
            self.kill()
        elif self.rect.x >= W:
            self.kill()
        if self.types == 'drop':
            if (sqrt((self.rect.x - self.oldrectx) ** 2 + (self.rect.y - self.oldrecty) ** 2) > self.radius * 1.25
            or self.velocity[0] == 0 and self.velocity[1] == 0) or self.flagdrop is True:
                if self.flagdrop is False:
                    self.flagdrop = True
                    self.gravity_x = abs(self.rect.x - self.oldrectx) / 8
                    self.gravity_y = abs(self.rect.y - self.oldrecty) / 8
                if self.rect.x > self.oldrectx:
                    self.rect.x -= self.gravity_x
                elif self.rect.x < self.oldrectx:
                    self.rect.x += self.gravity_x
                if self.rect.y > self.oldrecty:
                    self.rect.y -= self.gravity_y
                elif self.rect.y < self.oldrecty:
                    self.rect.y += self.gravity_y
                if (sqrt((self.rect.x - self.oldrectx) ** 2 + (self.rect.y - self.oldrecty) ** 2)) < self.radius / 5:
                    self.kill()
            else:
                self.rect.x += self.velocity[0]
                self.rect.y += self.velocity[1] + self.gravity
        elif self.types == 'attack':
            self.gravity_x = abs(self.rect.x - self.oldrectx) / 9
            self.gravity_y = abs(self.rect.y - self.oldrecty) / 9
            if self.rect.x > self.oldrectx:
                self.rect.x -= self.gravity_x
            elif self.rect.x < self.oldrectx:
                self.rect.x += self.gravity_x
            if self.rect.y > self.oldrecty:
                self.rect.y -= self.gravity_y
            elif self.rect.y < self.oldrecty:
                self.rect.y += self.gravity_y
            if (sqrt((self.rect.x - self.oldrectx) ** 2 + (self.rect.y - self.oldrecty) ** 2)) < self.radius / 3:
                self.kill()
        elif self.types == 'big':
            self.rect.y += self.gravity
            if sqrt((self.rect.x - self.oldrectx) ** 2 + (self.rect.y - self.oldrecty) ** 2) > self.radius * 2 or \
                    self.velocity[0] == 0 and self.velocity[1] == 0:
                self.kill()
        elif self.types == 'fall' or self.types == 'up':
            self.rect.y += self.gravity
            if sqrt((self.rect.x - self.oldrectx) ** 2 + (self.rect.y - self.oldrecty) ** 2) > self.radius // 1.75 or \
                    self.velocity[0] == 0 and self.velocity[1] == 0:
                self.kill()
        else:
            self.velocity[1] += self.gravity_y
            self.velocity[0] += self.gravity_x
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1] + self.gravity
            if sqrt((self.rect.x - self.oldrectx) ** 2 + (self.rect.y - self.oldrecty) ** 2) > self.radius * 2 or \
                    self.velocity[0] == 0 and self.velocity[1] == 0:
                self.kill()
