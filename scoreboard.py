import pygame
import sys
import pickle
from settings import *


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, menu):
        pygame.sprite.Sprite.__init__(self)
        self.menu = menu

        file = open("Set.obj", 'rb')
        try:
            self.get = pickle.load(file)
        finally:
            file.close()

        self.score = self.get.score
        pygame.font.init()
        self.font = pygame.font.SysFont('inkfree', 40)

        self.index = 0

        self.text1 = self.font.render("", False, (0, 0, 0))
        self.text1_rect = self.text1.get_rect(center=(600, 350))

        self.text2 = self.font.render("", False, (0, 0, 0))
        self.text2_rect = self.text2.get_rect(center=(600, 430))

        self.text3 = self.font.render("", False, (0, 0, 0))
        self.text3_rect = self.text3.get_rect(center=(600, 510))

        self.text4 = self.font.render("", False, (0, 0, 0))
        self.text4_rect = self.text4.get_rect(center=(600, 590))

        self.click = pygame.mixer.Sound(os.path.join(sounds_folder, 'click_sound.mp3'))
        self.click.set_volume(0.5)
        self.sort()
        self.text_init()

    def sort(self):
        n = len(self.score)
        while n > 1:
            swap = False
            for i in range(0, n - 1):
                if self.score[i][1] < self.score[i + 1][1]:
                    self.score[i], self.score[i + 1] = self.score[i + 1], self.score[i]
                    swap = True
            n -= 1
            if not swap: break

    def draw(self):
        waiting = True
        while waiting:
            self.menu.engine.clock.tick(FPS)
            pos = pygame.mouse.get_pos()
            self.animation(pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if 0 < pos[0] < 200 and 700 < pos[1] < 800:                                                   # EXIT
                        if self.menu.engine.sound_play:
                            self.click.play()
                        waiting = False

                    if 1060 < pos[0] < 1120 and 300 < pos[1] < 425:                                                 # UP
                        if self.index > 0:
                            self.index -= 1
                        if self.menu.engine.sound_play:
                            self.click.play()

                    if 1040 < pos[0] < 1100 and 550 < pos[1] < 670:                                               # DOWN
                        if self.index < len(self.score) - 4:
                            self.index += 1
                        if self.menu.engine.sound_play:
                            self.click.play()

            self.text_init()
            self.menu.engine.screen.blit(self.text1, self.text1_rect)
            self.menu.engine.screen.blit(self.text2, self.text2_rect)
            self.menu.engine.screen.blit(self.text3, self.text3_rect)
            self.menu.engine.screen.blit(self.text4, self.text4_rect)
            self.menu.mouse.update()
            self.menu.engine.mouse.draw(self.menu.engine.screen)
            pygame.display.flip()

    def text_init(self):
        try:
            self.text1 = self.font.render(str(self.score[self.index][0]) + "        "
                                          + str(self.score[self.index][1]), True, (255, 255, 255))
            self.text1_rect = self.text1.get_rect(center=(600, 350))

            self.text2 = self.font.render(str(self.score[self.index + 1][0]) + "        "
                                          + str(self.score[self.index + 1][1]), True, (255, 255, 255))
            self.text2_rect = self.text2.get_rect(center=(600, 430))

            self.text3 = self.font.render(str(self.score[self.index + 2][0]) + "        "
                                          + str(self.score[self.index + 2][1]), True, (255, 255, 255))
            self.text3_rect = self.text3.get_rect(center=(600, 510))

            self.text4 = self.font.render(str(self.score[self.index + 3][0]) + "        "
                                          + str(self.score[self.index + 3][1]), True, (255, 255, 255))
            self.text4_rect = self.text4.get_rect(center=(600, 590))
        except:
            pass

    def animation(self, pos):
        if 0 < pos[0] < 200 and 700 < pos[1] < 800:
            background = pygame.image.load(os.path.join(menu_folder, "scoreboard_quit.png")).convert()
            self.load_image(background)
        else:
            background = pygame.image.load(os.path.join(menu_folder, "scoreboard_clear.png")).convert()
            self.load_image(background)

    def load_image(self, background):
        background_rect = background.get_rect()
        background_rect.center = WIDTH // 2, HEIGHT // 2
        self.menu.engine.screen.fill((0, 100, 0))
        self.menu.engine.screen.blit(background, background_rect)
        pygame.draw.rect(self.menu.engine.screen, (0, 0, 0), background_rect, 1)
