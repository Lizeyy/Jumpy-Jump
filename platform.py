from sprites import *
import random


class Platform(pygame.sprite.Sprite):
    def __init__(self, engine, x, y, w, h, theme):
        self.engine = engine
        self._layer = 4
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.theme = theme
        self.direct = 0
        self.width = w

        self.load_images(w)

    def load_images(self, w):
        if w < 225:
            self.image = platform1_list[self.theme]
            self.image = pygame.transform.scale(self.image, (w, 40))
        elif w < 300:
            self.image = platform2_list[self.theme]
            self.image = pygame.transform.scale(self.image, (w, 40))
        elif w < 500:
            self.image = platform3_list[self.theme]
            self.image = pygame.transform.scale(self.image, (w, 40))
        else:
            self.image = platform0_list[self.theme]
            self.image = pygame.transform.scale(self.image, (w, 80))

    def ornament(self):
        if self.width > 300:
            if self.theme == 0:
                path = default_folder
            elif self.theme == 1:
                path = desert_folder
            elif self.theme == 2:
                path = winter_folder
            else:
                path = spooky_folder
            rand = random.randrange(0, 15)

            if rand < 8:
                if 0 <= rand <= 1:
                    img = pygame.image.load(os.path.join(path, 'orn1.png')).convert_alpha()
                elif 2 <= rand <= 3:
                    img = pygame.image.load(os.path.join(path, 'orn2.png')).convert_alpha()
                elif 4 <= rand <= 5:
                    img = pygame.image.load(os.path.join(path, 'orn3.png')).convert_alpha()
                else:
                    img = pygame.image.load(os.path.join(path, 'orn4.png')).convert_alpha()
                size = int(img.get_width() / 2)
                try:
                    ornament = Ornament(self.engine, self.rect.x + random.randrange(size, self.width - size),
                                        self.rect.y + 1, img.get_width(), img.get_height(), 3, 0, 0)
                    ornament.image = img
                    self.engine.ornaments.add(ornament)
                    self.mask = pygame.mask.from_surface(self.image)
                except:
                    pass


class Ornament(pygame.sprite.Sprite):
    def __init__(self, engine, x, y, w, h, l, dire, sp):
        self.groups = engine.all_sprites
        self._layer = l
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.w = w
        self.direction = dire
        self.speed = sp
