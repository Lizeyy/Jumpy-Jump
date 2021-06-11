from settings import *
import pygame
from PIL import Image, ImageFilter


class Pause:
    def __init__(self, engine):
        self.engine = engine

    def pause_screen(self):
        pygame.image.save(self.engine.screen, os.path.join(pause_folder, 'screen.png'))
        im = Image.open(os.path.join(pause_folder, 'screen.png'))
        im = im.filter(ImageFilter.BLUR)
        im = im.filter(ImageFilter.BLUR)
        im = im.filter(ImageFilter.BLUR)
        im = im.filter(ImageFilter.BLUR)
        im.save(os.path.join(pause_folder, 'screen.png'))

    def end_screen(self):
        pygame.image.save(self.engine.screen, os.path.join(end_folder, 'screen.png'))
        im = Image.open(os.path.join(end_folder, 'screen.png'))
        im = im.filter(ImageFilter.BLUR)
        im = im.filter(ImageFilter.BLUR)
        im = im.filter(ImageFilter.BLUR)
        im = im.filter(ImageFilter.BLUR)
        im.save(os.path.join(end_folder, 'screen.png'))


class PauseButton(pygame.sprite.Sprite):
    def __init__(self, engine, x, y, w, h, img):
        pygame.sprite.Sprite.__init__(self)
        self.engine = engine
        self.image = pygame.Surface((w, h))
        self.groups = self.engine.all_pause
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = img
