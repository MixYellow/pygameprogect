import pygame

lst_of_types_of_hex = [['lavender', 'field', 'desert'],  # good
                       ['trap', 'natives', 'swamp'],  # bad
                       ['emptiness', 'good_natives', 'magma', 'animals', 'volcano']]  # neutral

pygame.init()
infoObject = pygame.display.Info()
W, H = infoObject.current_w, infoObject.current_h

DEATHLST = ['injured', 'injured', 'injured', 'injured', 'injured', 'injured', 'injured', 'injured', 'injured',
            'injured',
            'injured', 'injured', 'neardeath', 'neardeath', 'neardeath', 'death']

LSTSPEEDUP = ['speedup', 'speedup', 'speedup', 'speedup', 'speedup']

SPEEDDEATHLST = ['sloweddown', 'sloweddown', 'sloweddown', 'sloweddown', 'sloweddown', 'sloweddown', 'sloweddown',
                 'sloweddown', 'sloweddown', 'sloweddown', 'sloweddown', 'sloweddown', 'sloweddown', 'sloweddown',
                 'sloweddown']

SPEEDDOWNLST = ['sloweddown', 'sloweddown', 'sloweddown', 'sloweddown', 'sloweddown', 'sloweddown', 'sloweddown',
                 'sloweddown', 'sloweddown', 'sloweddown']

EXPLORELST = ['boom.png', 'magma.png']

FLYLST = ['health.png', 'heart.png']

ONETIMELST = ['world.png', 'steam.png']

DROPLST = ['lavender.png', 'meat.png', 'sand.png']

FALLINGLST = ['speeddown.png']

JUMPINGLST = ['speedup.png']

ATTACKLST = ['beet.png', 'angry.png']

GRAVITY = 0.2

cell_size = H // 20