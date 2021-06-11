import pygame
import sys
from settings import *
from triumpf import TriumpfRect


class Credits:
    def __init__(self, menu):
        self.menu = menu
        self.credits = pygame.sprite.Group()
        self.click = pygame.mixer.Sound(os.path.join(sounds_folder, 'click_sound.mp3'))
        self.click.set_volume(0.5)
        self.text = TriumpfRect(0, HEIGHT, 1200, 1600)
        self.text.image = pygame.image.load(os.path.join(credits_folder, 'credits_text.png')).convert_alpha()
        self.credits.add(self.text)

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
                    if 0 < pos[0] < 200 and 700 < pos[1] < 800:  # EXIT
                        if self.menu.engine.sound_play:
                            self.click.play()
                        waiting = False

            self.text.rect.y -= 1

            if self.text.rect.midbottom[1] < -10:
                waiting = False

            self.credits.draw(self.menu.engine.screen)
            self.menu.mouse.update()
            self.menu.engine.mouse.draw(self.menu.engine.screen)
            pygame.display.flip()

    def animation(self, pos):
        if 0 < pos[0] < 200 and 700 < pos[1] < 800:
            background = pygame.image.load(os.path.join(credits_folder, "credits_quit.png")).convert()
            self.load_image(background)
        else:
            background = pygame.image.load(os.path.join(credits_folder, "credits_clear.png")).convert()
            self.load_image(background)

    def load_image(self, background):
        background_rect = background.get_rect()
        background_rect.center = WIDTH // 2, HEIGHT // 2
        self.menu.engine.screen.fill((0, 100, 0))
        self.menu.engine.screen.blit(background, background_rect)
        pygame.draw.rect(self.menu.engine.screen, (0, 0, 0), background_rect, 1)
