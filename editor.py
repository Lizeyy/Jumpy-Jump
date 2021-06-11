import sys
import pickle

from sprites import *
from triumpf import TriumpfRect


class Editor:
    index = 0
    chose_skin = 0
    chose_theme = 0
    chose_mode = 0

    def __init__(self, menu):
        self.menu = menu
        file = open("Set.obj", 'rb')
        try:
            self.get = pickle.load(file)
        finally:
            file.close()

        self.chose_skin = self.get.skin
        self.chose_theme = self.get.theme
        self.chose_mode = self.get.mode

        self.mode = False
        self.skin = run_right[self.get.skin]
        self.theme = icons_list[self.get.theme]

        self.edit_buttons = pygame.sprite.Group()
        self.edit_sprites = pygame.sprite.Group()

        self.arrow1 = EditButton(self, 265, 340)
        self.edit_buttons.add(self.arrow1)
        self.arrow2 = EditButton(self, 865, 340)
        self.edit_buttons.add(self.arrow2)

        if self.get.mode == 0:
            self.arrow = EditButton(self, 480, 560)
        else:
            self.arrow = EditButton(self, 480, 665)
        self.edit_buttons.add(self.arrow)
        self.arrow.image = pygame.transform.scale(pygame.image.load(os.path.join(editor_folder, 'arrow.png'))
                                                  .convert_alpha(), (50, 50))

        self.edit_char = EditSprite(self, 190, 110, 250, 250)
        self.edit_sprites.add(self.edit_char)
        self.edit_back = EditSprite(self, 740, 110, 320, 200)
        self.edit_sprites.add(self.edit_back)

        self.edit_back.image = pygame.transform.scale(icons_list[self.get.theme], (320, 200))

        self.switch = TriumpfRect(1110, 10, 80, 40)
        self.edit_buttons.add(self.switch)
        self.click = pygame.mixer.Sound(os.path.join(sounds_folder, 'click_sound.mp3'))
        self.click.set_volume(0.5)

    def draw_editor(self):
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
                    pos = pygame.mouse.get_pos()

                    if 265 < pos[0] < 335 and 340 < pos[1] < 390:                   # arrow1
                        if self.chose_skin < len(run_right) - 1:
                            self.chose_skin += 1
                            self.check()
                        else:
                            self.chose_skin = 0
                        self.skin = run_right[self.chose_skin]
                        self.click.play()
                    elif 865 < pos[0] < 935 and 340 < pos[1] < 390:                 # arrow2
                        if self.chose_theme < len(icons_list) - 1:
                            self.chose_theme += 1
                            self.check2()
                        else:
                            self.chose_theme = 0
                        self.theme = icons_list[self.chose_theme]
                        self.theme = pygame.transform.scale(self.theme, (320, 200))
                        self.edit_back.image = self.theme
                        self.click.play()

                    elif self.mode and 435 < pos[0] < 755 and 540 < pos[1] < 650:   # classic
                        self.arrow.rect.x = 480
                        self.arrow.rect.y = 560
                        self.chose_mode = 0
                        self.click.play()
                    elif self.mode and 435 < pos[0] < 755 and 650 < pos[1] < 750:   # hard
                        self.arrow.rect.x = 480
                        self.arrow.rect.y = 665
                        self.chose_mode = 1
                        self.click.play()

                    elif 1110 < pos[0] < 1150 and 10 < pos[1] < 50:
                        if self.menu.engine.sound_play:
                            self.menu.engine.sound_play = False
                        else:
                            self.menu.engine.sound_play = True
                    elif 1150 < pos[0] < 1190 and 10 < pos[1] < 50:
                        if self.menu.engine.music_play:
                            self.menu.engine.music_play = False
                            pygame.mixer.music.pause()
                        else:
                            self.menu.engine.music_play = True
                            pygame.mixer.music.unpause()

                    elif 0 < pos[0] < 200 and 700 < pos[1] < 800:
                        waiting = False
                        self.click.play()
                        self.get.mode = self.chose_mode
                        self.get.skin = self.chose_skin
                        self.get.theme = self.chose_theme

                        file = open("Set.obj", "wb")
                        try:
                            pickle.dump(self.get, file)
                        finally:
                            file.close()

                        self.arrow1.kill()
                        self.arrow2.kill()
                        self.edit_char.kill()
                        self.edit_back.kill()

            self.character_animation()
            self.edit_buttons.draw(self.menu.engine.screen)
            self.edit_sprites.draw(self.menu.engine.screen)
            self.menu.mouse.update()
            self.menu.engine.mouse.draw(self.menu.engine.screen)
            pygame.display.flip()

    def character_animation(self):
        if self.index < len(self.skin) * 3 - 1:
            self.index += 1
        else:
            self.index = 0
        i = int(self.index / 3)
        self.skin[i] = pygame.transform.scale(self.skin[i], (200, 200))
        self.edit_char.image = self.skin[i]
        self.edit_sprites.draw(self.menu.engine.screen)

    def check(self):
        if not self.get.triumpfs[self.chose_skin]:
            if self.chose_skin < len(run_right) - 1:
                self.chose_skin += 1
            else:
                self.chose_skin = 0
            self.check()

    def check2(self):
        if not self.get.triumpfs_map[self.chose_theme]:
            if self.chose_theme < len(icons_list) - 1:
                self.chose_theme += 1
            else:
                self.chose_theme = 0
            self.check2()

    def animation(self, pos):
        if not 435 < pos[0] < 755 and not 380 < pos[1] < 540:
            self.mode = False

        if 435 < pos[0] < 755 and 380 < pos[1] < 540:
            background = pygame.image.load(os.path.join(editor_folder, "background_mode.png")).convert()
            self.load_image(background)
            self.mode = True
        elif self.mode and 435 < pos[0] < 755 and 540 < pos[1] < 650:
            background = pygame.image.load(os.path.join(editor_folder, "background_classic.png")).convert()
            self.load_image(background)
        elif self.mode and 435 < pos[0] < 755 and 650 < pos[1] < 750:
            background = pygame.image.load(os.path.join(editor_folder, "background_hard.png")).convert()
            self.load_image(background)
        elif 0 < pos[0] < 200 and 700 < pos[1] < 800:
            background = pygame.image.load(os.path.join(editor_folder, "background_quit.png")).convert()
            self.load_image(background)
        else:
            background = pygame.image.load(os.path.join(editor_folder, "background_clear.png")).convert()
            self.load_image(background)

        if 265 < pos[0] < 335 and 340 < pos[1] < 390:
            arrow = pygame.image.load(os.path.join(editor_folder, "arrow_2.png"))
            arrow = pygame.transform.scale(arrow, (70, 50))
            self.arrow1.image = arrow
        else:
            arrow = pygame.image.load(os.path.join(editor_folder, "arrow_1.png"))
            arrow = pygame.transform.scale(arrow, (70, 50))
            self.arrow1.image = arrow

        if 865 < pos[0] < 935 and 340 < pos[1] < 390:
            arrow = pygame.image.load(os.path.join(editor_folder, "arrow_2.png"))
            arrow = pygame.transform.scale(arrow, (70, 50))
            self.arrow2.image = arrow
        else:
            arrow = pygame.image.load(os.path.join(editor_folder, "arrow_1.png"))
            arrow = pygame.transform.scale(arrow, (70, 50))
            self.arrow2.image = arrow

        if self.mode:
            self.edit_buttons.add(self.arrow)
        else:
            self.edit_buttons.remove(self.arrow)

        if self.menu.engine.sound_play:
            if self.menu.engine.music_play:
                self.switch.image = pygame.image.load(os.path.join(other_folder, 'switch_clear.png'))
            else:
                self.switch.image = pygame.image.load(os.path.join(other_folder, 'switch_music.png'))
        else:
            if self.menu.engine.music_play:
                self.switch.image = pygame.image.load(os.path.join(other_folder, 'switch_sound.png'))
            else:
                self.switch.image = pygame.image.load(os.path.join(other_folder, 'switch_both.png'))
        self.switch.image = pygame.transform.scale(self.switch.image, (80, 40))

    def load_image(self, background):
        background_rect = background.get_rect()
        background_rect.center = WIDTH // 2, HEIGHT // 2
        self.menu.engine.screen.fill((0, 100, 0))
        self.menu.engine.screen.blit(background, background_rect)
        pygame.draw.rect(self.menu.engine.screen, (0, 0, 0), background_rect, 1)


class EditButton(pygame.sprite.Sprite):
    def __init__(self, edit, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.edit = edit
        self.groups = edit.edit_buttons
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class EditSprite(pygame.sprite.Sprite):
    def __init__(self, edit, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.edit = edit
        self.groups = edit.edit_sprites
        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
