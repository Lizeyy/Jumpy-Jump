import pickle
from sprites import *
from particles import *


class Background(pygame.sprite.Sprite):
    def __init__(self, engine):
        self.engine = engine
        pygame.sprite.Sprite.__init__(self)
        self.groups = engine.all_sprites
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.load()

    def load(self):
        file = open("Set.obj", 'rb')
        try:
            self.get = pickle.load(file)
        finally:
            file.close()

        self.image = back_list[self.get.theme].convert()


class Mouse(pygame.sprite.Sprite):
    def __init__(self, menu):
        self.menu = menu
        self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load(os.path.join(other_folder, 'mouse.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.groups = self.menu.engine.mouse
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.particles = []
        self.particles.append(Particles(600, 400, 2, 1, (204, 153, 255), self.menu.engine.screen, 0))
        self.particles.append(Particles(600, 400, 2, 1, (102, 0, 102), self.menu.engine.screen, 0))

    def update(self):
        self.rect.topleft = pygame.mouse.get_pos()
        x, y = pygame.mouse.get_pos()
        for par in self.particles:
            par.x = x
            par.y = y
            par.add_particles()
            par.emit()
