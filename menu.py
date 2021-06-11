import random
from editor import *
from scoreboard import *
from triumpf import *
from background import Mouse
from credits import *


class Menu(object):
    def __init__(self, engine):
        self.engine = engine

        self.menu_sprites = pygame.sprite.Group()

        pygame.font.init()
        self.font = pygame.font.SysFont('inkfree', 30)

        self.event = True
        self.active = False

        self.nickbox = ''
        self.nicktext = ''
        self.click = pygame.mixer.Sound(os.path.join(sounds_folder, 'click_sound.mp3'))
        self.click.set_volume(0.5)
        self.mouse = Mouse(self)

    def new(self):
        file = open("Set.obj", 'rb')
        try:
            self.get = pickle.load(file)
        finally:
            file.close()

        score = []
        for i in range(0, len(self.get.score) - 1):
            score.append(self.get.score[i][1])
        if len(score) > 0:
            self.score_max = max(score)
        else:
            self.score_max = 0

        self.text_sc = self.font.render(str(self.score_max), True, (0, 90, 90))
        self.text_sc_rect = self.text_sc.get_rect()
        self.text_sc_rect.center = (90, 125)

        self.nick = self.font.render(self.get.nick, True, (0, 90, 90))
        self.nick_rect = self.nick.get_rect()
        self.nick_rect.bottomright = (1180, 170)

        self.nickdraw = self.font.render(self.nicktext, True, (0, 90, 90))
        self.nickdraw_rect = self.nickdraw.get_rect()
        self.nickdraw_rect.center = (340, 440)

        self.switch = TriumpfRect(1110, 10, 80, 40)
        self.menu_sprites.add(self.switch)

        pygame.mixer.music.load(os.path.join(music_folder, 'menu_bg.mp3'))

        pygame.mixer.music.play(-1)
        self.engine.music()

        self.spawn()
        self.draw_menu()

    def spawn(self):
        self.direction = random.choice([-1, 1])
        if self.direction == 1:
            self.choose = random.choice(run_right)
        else:
            self.choose = random.choice(run_left)
        self.menu_sprite = MenuSprite(self)
        self.menu_sprites.add(self.menu_sprite)

    def draw_menu(self):
        waiting = True
        while waiting:
            self.engine.clock.tick(FPS)
            self.menu_sprite.update_sprite()
            if self.menu_sprite.rect.x > WIDTH + 200 or self.menu_sprite.rect.x < -200:
                self.menu_sprite.kill()
                self.spawn()

            pos = pygame.mouse.get_pos()
            self.animation(pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    if self.event:
                        if 350 < pos[0] < 850 and 60 < pos[1] < 250:        # START
                            if self.engine.sound_play:
                                self.click.play()
                            self.menu_sprite.kill()
                            pygame.mixer.music.stop()
                            waiting = False

                        elif 200 < pos[0] < 600 and 290 < pos[1] < 480:     # editor
                            if self.engine.sound_play:
                                self.click.play()
                            self.editor = Editor(self)
                            self.editor.draw_editor()

                        elif 600 < pos[0] < 1000 and 290 < pos[1] < 480:     # triumpf
                            if self.engine.sound_play:
                                self.click.play()
                            self.triumpf = Triumpf(self)
                            self.triumpf.draw_triumpf()

                        elif 0 < pos[0] < 180 and 180 < pos[1] < 250:       # scoreboard
                            if self.engine.sound_play:
                                self.click.play()
                            self.scoreboard = Scoreboard(self)
                            self.scoreboard.draw()

                        elif 1020 < pos[0] < 1200 and 50 < pos[1] < 140:    # nick
                            if self.engine.sound_play:
                                self.click.play()
                            self.event = False
                            self.nicktext = ''
                            self.nickbox = MenuNick(self)
                            self.menu_sprites.add(self.nickbox)
                            self.active = True

                        elif 0 < pos[0] < 200 and 700 < pos[1] < 800:       # QUIT
                            if self.engine.sound_play:
                                self.click.play()
                            pygame.quit()
                            sys.exit()

                        elif 1000 < pos[0] < 1200 and 700 < pos[1] < 800:       # credits
                            if self.engine.sound_play:
                                self.click.play()
                            self.credit = Credits(self)
                            self.credit.draw()

                        elif 1110 < pos[0] < 1150 and 10 < pos[1] < 50:
                            if self.engine.sound_play:
                                self.engine.sound_play = False
                            else:
                                self.engine.sound_play = True
                        elif 1150 < pos[0] < 1190 and 10 < pos[1] < 50:
                            if self.engine.music_play:
                                self.engine.music_play = False
                                pygame.mixer.music.pause()
                            else:
                                self.engine.music_play = True
                                pygame.mixer.music.unpause()

                    else:
                        if 780 < pos[0] < 875 and 380 < pos[1] < 475:       # new nick
                            if self.engine.sound_play:
                                self.click.play()
                            self.nick = self.font.render(self.nicktext, True, (0, 90, 90))
                            self.nick_rect = self.nick.get_rect()
                            self.nick_rect.bottomright = (1180, 170)
                            self.event = True
                            self.nickbox.kill()

                            self.get.nick = self.nicktext

                            file = open("Set.obj", "wb")
                            try:
                                pickle.dump(self.get, file)
                            finally:
                                file.close()

                        if 820 < pos[0] < 890 and 212 < pos[1] < 280:       # exit nick
                            if self.engine.sound_play:
                                self.click.play()
                            self.event = True
                            self.nickbox.kill()

                if not self.event and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.engine.sound_play:
                            self.click.play()
                        self.nick = self.font.render(self.nicktext, True, (0, 90, 90))
                        self.nick_rect = self.nick.get_rect()
                        self.nick_rect.bottomright = (1180, 170)
                        self.event = True
                        self.nickbox.kill()

                        self.get.nick = self.nicktext
                        file = open("Set.obj", "wb")
                        try:
                            pickle.dump(self.get, file)
                        finally:
                            file.close()

                    elif event.key == pygame.K_BACKSPACE:
                        if len(self.nicktext) <= 15:
                            self.nicktext = self.nicktext[:-1]
                    else:
                        if len(self.nicktext) <= 15:
                            self.nicktext += event.unicode
                    self.nickdraw = self.font.render(self.nicktext, True, (0, 90, 90))

            self.menu_sprites.draw(self.engine.screen)
            self.engine.screen.blit(self.text_sc, self.text_sc_rect)
            self.engine.screen.blit(self.nick, self.nick_rect)
            if not self.event: self.engine.screen.blit(self.nickdraw, self.nickdraw_rect)
            self.engine.mouse.draw(self.engine.screen)
            self.mouse.update()
            pygame.display.flip()

    def animation(self, pos):
        if self.event:
            if 350 < pos[0] < 850 and 60 < pos[1] < 250:
                background = pygame.image.load(os.path.join(menu_folder, "background_start.png")).convert()
                self.load_image(background)
            elif 0 < pos[0] < 180 and 160 < pos[1] < 250:
                background = pygame.image.load(os.path.join(menu_folder, "background_score.png")).convert()
                self.load_image(background)
            elif 1020 < pos[0] < 1200 and 50 < pos[1] < 140:
                background = pygame.image.load(os.path.join(menu_folder, "background_nick.png")).convert()
                self.load_image(background)
            elif 200 < pos[0] < 600 and 290 < pos[1] < 480:
                background = pygame.image.load(os.path.join(menu_folder, "background_edit.png")).convert()
                self.load_image(background)
            elif 600 < pos[0] < 1000 and 290 < pos[1] < 480:
                background = pygame.image.load(os.path.join(menu_folder, "background_triumphs.png")).convert()
                self.load_image(background)
            elif 0 < pos[0] < 200 and 700 < pos[1] < 800:
                background = pygame.image.load(os.path.join(menu_folder, "background_quit.png")).convert()
                self.load_image(background)
            elif 1000 < pos[0] < 1200 and 700 < pos[1] < 800:
                background = pygame.image.load(os.path.join(menu_folder, "background_credits.png")).convert()
                self.load_image(background)
            else:
                background = pygame.image.load(os.path.join(menu_folder, "background_clear.png")).convert()
                self.load_image(background)

            if self.engine.sound_play:
                if self.engine.music_play:
                    self.switch.image = pygame.image.load(os.path.join(other_folder, 'switch_clear.png'))
                else:
                    self.switch.image = pygame.image.load(os.path.join(other_folder, 'switch_music.png'))
            else:
                if self.engine.music_play:
                    self.switch.image = pygame.image.load(os.path.join(other_folder, 'switch_sound.png'))
                else:
                    self.switch.image = pygame.image.load(os.path.join(other_folder, 'switch_both.png'))
            self.switch.image = pygame.transform.scale(self.switch.image, (80, 40))

        else:
            background = pygame.image.load(os.path.join(menu_folder, "background_clear.png")).convert()
            self.load_image(background)
            if 780 < pos[0] < 875 and 380 < pos[1] < 475:
                self.nickbox.image = pygame.image.load(os.path.join(menu_folder, 'nick_enter.png'))
                self.nickbox.image = pygame.transform.scale(self.nickbox.image, (625, 375))
            elif 820 < pos[0] < 890 and 212 < pos[1] < 280:
                self.nickbox.image = pygame.image.load(os.path.join(menu_folder, 'nick_exit.png'))
                self.nickbox.image = pygame.transform.scale(self.nickbox.image, (625, 375))
            else:
                self.nickbox.image = pygame.image.load(os.path.join(menu_folder, 'nick_clear.png'))
                self.nickbox.image = pygame.transform.scale(self.nickbox.image, (625, 375))

    def load_image(self, background):
        background_rect = background.get_rect()
        background_rect.center = WIDTH // 2, HEIGHT // 2
        self.engine.screen.fill((0, 100, 0))
        self.engine.screen.blit(background, background_rect)
        pygame.draw.rect(self.engine.screen, (0, 0, 0), background_rect, 1)


class MenuSprite(pygame.sprite.Sprite):
    index = 0

    def __init__(self, menu):
        self.menu = menu
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((200, 200))
        self.rect = self.image.get_rect()
        self.rect.y = 490
        if self.menu.direction == 1:
            self.rect.x = -200
        else:
            self.rect.x = WIDTH + 50
        self.img = self.menu.choose

    def update_sprite(self):
        if self.index < len(self.img) * 3 - 1:
            self.index += 1
        else:
            self.index = 0
        i = int(self.index / 3)
        self.img[i] = pygame.transform.scale(self.img[i], (200, 200))
        self.image = self.img[i]

        if self.menu.direction == 1:
            self.rect.x += 4
        else:
            self.rect.x -= 4


class MenuNick(pygame.sprite.Sprite):
    def __init__(self, menu):
        self.menu = menu
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((625, 375))
        self.rect = self.image.get_rect()
        self.rect.x = 287
        self.rect.y = 212
        self.image = pygame.image.load(os.path.join(menu_folder, 'nick_clear.png'))
        self.image = pygame.transform.scale(self.image, (625, 375))
