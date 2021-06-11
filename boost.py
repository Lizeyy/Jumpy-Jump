from sprites import *


class Boost(pygame.sprite.Sprite):
    index = 0

    def __init__(self, engine, x, y, type):
        self.engine = engine
        self.groups = engine.others, engine.all_sprites
        self._layer = 4
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        self.types()

    def types(self):
        if self.type == 0:
            self.image = pygame.image.load(os.path.join(other_folder, 'boost.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 70))
            self.mask = pygame.mask.from_surface(self.image)

        elif self.type == 1:
            self.image = pygame.image.load(os.path.join(other_folder, 'star.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 70))
            self.rect.y -= 3
            self.mask = pygame.mask.from_surface(self.image)

        elif self.type == 2:
            self.image = pygame.image.load(os.path.join(other_folder, 'cactus.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 70))
            self.rect.y -= 10
            self.mask = pygame.mask.from_surface(self.image)

        elif self.type == 3:
            self.image = pygame.image.load(os.path.join(other_folder, 'snowflake.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 70))
            self.mask = pygame.mask.from_surface(self.image)

        elif self.type == 4:
            self.image = pygame.image.load(os.path.join(other_folder, 'pumpkin.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 70))
            self.rect.y -= 10
            self.mask = pygame.mask.from_surface(self.image)
