import pickle
import pygame
import sys
from settings import *


class Triumpf:
    def __init__(self, menu):
        self.menu = menu
        self.triumpfs = pygame.sprite.Group()

        self.index = 0
        self.list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        file = open("Set.obj", 'rb')
        try:
            self.get = pickle.load(file)
        finally:
            file.close()

        icons = TriumpfRect(1150, 10, 33, 200)
        icons.image = pygame.transform.scale(pygame.image.load(os.path.join(triumpf_folder, 'icons.png')), (33, 200))
        self.triumpfs.add(icons)

        pygame.font.init()
        font = pygame.font.SysFont('inkfree', 30)
        self.death = font.render(str(self.get.death), True, (0, 90, 90))
        self.death_rect = self.death.get_rect(midright=(1140, 26))

        self.boost = font.render(str(self.get.boost), True, (0, 90, 90))
        self.boost_rect = self.boost.get_rect(midright=(1140, 59))

        self.star = font.render(str(self.get.star), True, (0, 90, 90))
        self.star_rect = self.star.get_rect(midright=(1140, 92))

        self.cactus = font.render(str(self.get.cactus), True, (0, 90, 90))
        self.cactus_rect = self.cactus.get_rect(midright=(1140, 125))

        self.snowflake = font.render(str(self.get.snowflake), True, (0, 90, 90))
        self.snowflake_rect = self.snowflake.get_rect(midright=(1140, 158))

        self.pumpkin = font.render(str(self.get.pumpkin), True, (0, 90, 90))
        self.pumpkin_rect = self.pumpkin.get_rect(midright=(1140, 191))

        self.tr1 = TriumpfRect(200, 305, 800, 150)
        self.tr2 = TriumpfRect(200, 470, 800, 150)

        self.click = pygame.mixer.Sound(os.path.join(sounds_folder, 'click_sound.mp3'))
        self.click.set_volume(0.5)
        self.image_init()
        self.triumpf_init()


    def draw_triumpf(self):
        waiting = True
        while waiting:
            pos = pygame.mouse.get_pos()
            self.animation(pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if 0 < pos[0] < 200 and 700 < pos[1] < 800:                                                   # EXIT
                        waiting = False
                        if self.menu.engine.sound_play:
                            self.click.play()
                        for obj in self.triumpfs:
                            obj.kill()

                    if 1060 < pos[0] < 1120 and 300 < pos[1] < 425:                                                 # UP
                        if self.index > 0:
                            self.index -= 1
                            self.triumpf_init()
                        if self.menu.engine.sound_play:
                            self.click.play()

                    if 1040 < pos[0] < 1100 and 550 < pos[1] < 670:                                               # DOWN
                        if self.index < len(self.list) - 2:
                            self.index += 1
                            self.triumpf_init()
                        if self.menu.engine.sound_play:
                            self.click.play()

            self.menu.engine.screen.blit(self.death, self.death_rect)
            self.menu.engine.screen.blit(self.boost, self.boost_rect)
            self.menu.engine.screen.blit(self.star, self.star_rect)
            self.menu.engine.screen.blit(self.cactus, self.cactus_rect)
            self.menu.engine.screen.blit(self.snowflake, self.snowflake_rect)
            self.menu.engine.screen.blit(self.pumpkin, self.pumpkin_rect)
            self.triumpfs.draw(self.menu.engine.screen)
            self.menu.engine.mouse.draw(self.menu.engine.screen)
            self.menu.mouse.update()
            pygame.display.flip()

    def triumpf_init(self):
        self.tr1.image = self.list[self.index]
        self.triumpfs.add(self.tr1)
        self.tr2.image = self.list[self.index + 1]
        self.triumpfs.add(self.tr2)

    def animation(self, pos):
        if 0 < pos[0] < 200 and 700 < pos[1] < 800:
            background = pygame.image.load(os.path.join(triumpf_folder, "triumpf_quit.png")).convert()
            self.load_image(background)
        else:
            background = pygame.image.load(os.path.join(triumpf_folder, "triumpf_clear.png")).convert()
            self.load_image(background)

    def load_image(self, background):
        background_rect = background.get_rect()
        background_rect.center = WIDTH // 2, HEIGHT // 2
        self.menu.engine.screen.fill((0, 100, 0))
        self.menu.engine.screen.blit(background, background_rect)
        pygame.draw.rect(self.menu.engine.screen, (0, 0, 0), background_rect, 1)

    def image_init(self):
        if self.get.triumpfs[4]:
            self.list[0] = pygame.image.load(os.path.join(triumpf_folder, 'adventure_boy_unlocked.png')).convert_alpha()
        else:
            self.list[0] = pygame.image.load(os.path.join(triumpf_folder, 'adventure_boy_locked.png')).convert_alpha()

        if self.get.triumpfs[5]:
            self.list[1] = pygame.image.load(os.path.join(triumpf_folder, 'adventure_girl_unlocked.png')).convert_alpha()
        else:
            self.list[1] = pygame.image.load(os.path.join(triumpf_folder, 'adventure_girl_locked.png')).convert_alpha()

        if self.get.triumpfs[6]:
            self.list[2] = pygame.image.load(os.path.join(triumpf_folder, 'ninja_girl_unlocked.png')).convert_alpha()
        else:
            self.list[2] = pygame.image.load(os.path.join(triumpf_folder, 'ninja_girl_locked.png')).convert_alpha()

        if self.get.triumpfs[7]:
            self.list[3] = pygame.image.load(os.path.join(triumpf_folder, 'ninja_boy_unlocked.png')).convert_alpha()
        else:
            self.list[3] = pygame.image.load(os.path.join(triumpf_folder, 'ninja_boy_locked.png')).convert_alpha()

        if self.get.triumpfs[8]:
            self.list[4] = pygame.image.load(os.path.join(triumpf_folder, 'knight_unlocked.png')).convert_alpha()
        else:
            self.list[4] = pygame.image.load(os.path.join(triumpf_folder, 'knight_locked.png')).convert_alpha()

        if self.get.triumpfs[9]:
            self.list[5] = pygame.image.load(os.path.join(triumpf_folder, 'zombie_boy_unlocked.png')).convert_alpha()
        else:
            self.list[5] = pygame.image.load(os.path.join(triumpf_folder, 'zombie_boy_locked.png')).convert_alpha()

        if self.get.triumpfs[10]:
            self.list[6] = pygame.image.load(os.path.join(triumpf_folder, 'zombie_girl_unlocked.png')).convert_alpha()
        else:
            self.list[6] = pygame.image.load(os.path.join(triumpf_folder, 'zombie_girl_locked.png')).convert_alpha()

        if self.get.triumpfs[11]:
            self.list[7] = pygame.image.load(os.path.join(triumpf_folder, 'robot_unlocked.png')).convert_alpha()
        else:
            self.list[7] = pygame.image.load(os.path.join(triumpf_folder, 'robot_locked.png')).convert_alpha()

        if self.get.triumpfs[12]:
            self.list[8] = pygame.image.load(os.path.join(triumpf_folder, 'santa_unlocked.png')).convert_alpha()
        else:
            self.list[8] = pygame.image.load(os.path.join(triumpf_folder, 'santa_locked.png')).convert_alpha()

        if self.get.triumpfs[13]:
            self.list[9] = pygame.image.load(os.path.join(triumpf_folder, 'jack_unlocked.png')).convert_alpha()
        else:
            self.list[9] = pygame.image.load(os.path.join(triumpf_folder, 'jack_locked.png')).convert_alpha()

        if self.get.triumpfs_map[1]:
            self.list[10] = pygame.image.load(os.path.join(triumpf_folder, 'desert_unlocked.png')).convert_alpha()
        else:
            self.list[10] = pygame.image.load(os.path.join(triumpf_folder, 'desert_locked.png')).convert_alpha()

        if self.get.triumpfs_map[2]:
            self.list[11] = pygame.image.load(os.path.join(triumpf_folder, 'winter_unlocked.png')).convert_alpha()
        else:
            self.list[11] = pygame.image.load(os.path.join(triumpf_folder, 'winter_locked.png')).convert_alpha()

        if self.get.triumpfs_map[3]:
            self.list[12] = pygame.image.load(os.path.join(triumpf_folder, 'spooky_unlocked.png')).convert_alpha()
        else:
            self.list[12] = pygame.image.load(os.path.join(triumpf_folder, 'spooky_locked.png')).convert_alpha()


class TriumpfRect(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        self._layer = 10
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

