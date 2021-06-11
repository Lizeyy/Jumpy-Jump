import pickle

from sprites import *

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    index = 0

    def __init__(self, engine):
        self.engine = engine
        self.groups = engine.all_sprites
        self._layer = 11
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.run_left = []
        self.run_right = []
        self.idle_left = []
        self.idle_right = []
        self.jump_left = []
        self.jump_right = []
        self.attack_left = []
        self.attack_right = []

        self.image = pygame.Surface((150, 150))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.image.get_rect()
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.left = False
        self.right = False
        self.jump = False
        self.last_left = False
        self.last_right = True
        self.can_attack = False
        self.attack = False

        self.get_images()

    def get_images(self):
        file = open("Set.obj", 'rb')
        try:
            get = pickle.load(file)
        finally:
            file.close()

        if get.skin == 6:
            self.can_attack = True
            self.attack_left = attack_left[1]
            self.attack_right = attack_right[1]
            self.a = 160
        elif get.skin == 7:
            self.can_attack = True
            self.attack_left = attack_left[0]
            self.attack_right = attack_right[0]
            self.a = 190
        elif get.skin == 8:
            self.can_attack = True
            self.attack_left = attack_left[2]
            self.attack_right = attack_right[2]
            self.a = 160

        self.run_left = run_left[get.skin]
        self.run_right = run_right[get.skin]
        self.idle_left = idle_left[get.skin]
        self.idle_right = idle_right[get.skin]
        self.jump_left = jump_left[get.skin]
        self.jump_right = jump_right[get.skin]

    def animation(self):
        if self.jump:
            if self.index < len(self.jump_left) * 5 - 1:
                self.index += 1
            i = int(self.index / 5)
        else:
            if self.index < len(self.run_right) * 5 - 1:
                self.index += 1
            else:
                self.index = 0
            i = int(self.index / 5)

        if not self.attack:
            if self.left and not self.jump:
                self.image = pygame.transform.scale(self.run_left[i], (150, 150))
            elif self.right and not self.jump:
                self.image = pygame.transform.scale(self.run_right[i], (150, 150))

            elif self.left and self.jump or self.last_left and self.jump:
                self.image = pygame.transform.scale(self.jump_left[i], (150, 150))
            elif self.right and self.jump or self.last_right and self.jump:
                self.image = pygame.transform.scale(self.jump_right[i], (150, 150))

            elif self.last_left and not self.jump and not self.right and not self.left:
                self.image = pygame.transform.scale(self.idle_left[i], (150, 150))
            elif self.last_right and not self.jump and not self.left and not self.right:
                self.image = pygame.transform.scale(self.idle_right[i], (150, 150))

        else:
            if self.last_right:
                self.image = pygame.transform.scale(self.attack_right[i], (self.a, self.a))
            elif self.last_left:
                self.image = pygame.transform.scale(self.attack_left[i], (self.a, self.a))
            if self.index == 0:
                self.attack = False

        self.mask = pygame.mask.from_surface(self.image)

    def jumpy(self, high):
        self.index = 0
        if self.engine.sound_play:
            pygame.mixer.Sound(os.path.join(sounds_folder, 'jump_sound.mp3')).play()
        hits = pygame.sprite.spritecollide(self, self.engine.platforms, False)
        if hits:
            self.vel.y = -high

    def update(self):
        self.animation()
        self.acc = vec(0, PLAYER_GRAVITY)

        if not self.attack and not self.engine.pause:
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                self.acc.x = -PLAYER_SPEED_X
                self.left = True
                self.last_left = True
                self.last_right = False
            else:
                self.left = False

            if key[pygame.K_RIGHT]:
                self.acc.x = PLAYER_SPEED_X
                self.right = True
                self.last_right = True
                self.last_left = False
            else:
                self.right = False

            if key[pygame.K_SPACE] and self.can_attack:
                if self.engine.sound_play:
                    pygame.mixer.Sound(os.path.join(sounds_folder, 'attack_sound.mp3')).play()
                self.attack = True
                self.index = 0

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 1 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        self.rect.midbottom = self.pos
