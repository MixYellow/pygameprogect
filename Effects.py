import pygame
import os
import sys
from random import choice
from consts import GRAVITY

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

def create_particles(position, name):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, choice(numbers), choice(numbers), name)

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

    def __init__(self, pos, dx, dy, name):
        self.pictures = [load_image(name)]
        for scale in (10, 15, 25):
            self.pictures.append(pygame.transform.scale(self.pictures[0], (scale, scale)))
        super().__init__(all_sprites)
        self.image = choice(self.pictures)
        self.rect = self.image.get_rect()

        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos

        self.gravity = GRAVITY

    def update(self):
        self.velocity[1] += self.gravity

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # if not self.rect.colliderect(screen_rect):
        #     self.kill()
