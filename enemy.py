from sprites import *


class Enemy(pygame.sprite.Sprite):
    index = 0

    def __init__(self, engine, x, y, theme, di):
        self.engine = engine
        self.groups = engine.enemies, engine.all_sprites
        self._layer = 9
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direct = di

        self.run_left = en_run_left[theme]
        self.run_right = en_run_right[theme]

    def update(self):
        if self.index < len(self.run_right) * 5 - 1:
            self.index += 1
        else:
            self.index = 0
        i = int(self.index / 5)

        if self.direct == -1:
            self.image = pygame.transform.scale(self.run_left[i], (100, 100))
            self.rect.x -= 1
        elif self.direct == 1:
            self.image = pygame.transform.scale(self.run_right[i], (100, 100))
            self.rect.x += 1
        else:
            x = self.engine.player.rect.x
            if x < self.rect.x:
                self.image = pygame.transform.scale(self.run_left[i], (80, 80))
            else:
                self.image = pygame.transform.scale(self.run_right[i], (80, 80))

        self.mask = pygame.mask.from_surface(self.image)
