import time

from menu import *
from player import *
from platform import *
from background import *
from pause import *
from enemy import *
from boost import *
from triumpf import TriumpfRect
from particles import *


class Engine:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.platforms = pygame.sprite.Group()
        self.backs = pygame.sprite.Group()
        self.all_pause = pygame.sprite.Group()
        self.all_end = pygame.sprite.Group()
        self.move_platform = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.others = pygame.sprite.Group()
        self.ornaments = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.back = pygame.sprite.Group()
        self.mouse = pygame.sprite.Group()

        self.running = True
        self.playing = False
        self.pause = False
        self.end = False
        self.msg = False
        self.music_play = True
        self.sound_play = True
        self.booster = False
        self.kill_particle = [False, 0]

        self.score = 0
        self.time = 0
        self.kill = 0

        self.menu = Menu(self)

        pygame.font.init()
        self.font = pygame.font.SysFont('inkfree', 30)

        self.text = self.font.render("Punkty: " + str(self.score), True, (0, 90, 90))
        self.text_rect = self.text.get_rect()
        self.text_rect.topleft = (10, 10)
        self.click = pygame.mixer.Sound(os.path.join(sounds_folder, 'click_sound.mp3'))
        self.click.set_volume(0.5)

        self.particles = []

    def new(self):
        file = open("Set.obj", 'rb')
        try:
            self.get = pickle.load(file)
        finally:
            file.close()

        self.all_sprites.add(Background(self))
        for plat in PLATFORM_LIST:
            p = Platform(self, *plat, self.get.theme)
            self.all_sprites.add(p)
            self.platforms.add(p)
            p.ornament()

        self.player = Player(self)
        self.score = 0
        self.kill = 0

        self.running = True
        self.playing = False
        self.pause = False
        self.end = False

        if self.get.skin == 11 and self.get.theme == 1:
            self.bonus = True
        elif self.get.skin == 12 and self.get.theme == 2:
            self.bonus = True
        elif self.get.skin == 13 and self.get.theme == 3:
            self.bonus = True
        else:
            self.bonus = False

        self.start = False
        if self.get.mode == 1:
            self.draw()
            self.time_start = time.time()
            self.start = True

        if self.get.theme == 1:
            pygame.mixer.music.load(os.path.join(music_folder, 'desert_bg.mp3'))
        elif self.get.theme == 2:
            pygame.mixer.music.load(os.path.join(music_folder, 'winter_bg.mp3'))
        elif self.get.theme == 3:
            pygame.mixer.music.load(os.path.join(music_folder, 'spooky_bg.mp3'))
        else:
            pygame.mixer.music.load(os.path.join(music_folder, 'default_bg.mp3'))

        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        self.music()

        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.draw()
            self.events()
            self.update()
            self.check()

    def update(self):
        if self.pause:
            pos = pygame.mouse.get_pos()
            self.menu.mouse.update()
            if 230 < pos[0] < 550 and 400 < pos[1] < 600:
                img = pygame.image.load(os.path.join(pause_folder, 'return_game2.png')).convert_alpha()
                img = pygame.transform.scale(img, (320, 200))
                self.pause_game.image = img
            else:
                img = pygame.image.load(os.path.join(pause_folder, 'return_game1.png')).convert_alpha()
                img = pygame.transform.scale(img, (320, 200))
                self.pause_game.image = img
            if 650 < pos[0] < 970 and 400 < pos[1] < 600:
                img = pygame.image.load(os.path.join(pause_folder, 'return_menu2.png')).convert_alpha()
                img = pygame.transform.scale(img, (320, 200))
                self.pause_menu.image = img
            else:
                img = pygame.image.load(os.path.join(pause_folder, 'return_menu1.png')).convert_alpha()
                img = pygame.transform.scale(img, (320, 200))
                self.pause_menu.image = img
            if self.sound_play:
                if self.music_play:
                    self.switch.image = pygame.image.load(os.path.join(other_folder, 'switch_clear.png'))
                else:
                    self.switch.image = pygame.image.load(os.path.join(other_folder, 'switch_music.png'))
            else:
                if self.music_play:
                    self.switch.image = pygame.image.load(os.path.join(other_folder, 'switch_sound.png'))
                else:
                    self.switch.image = pygame.image.load(os.path.join(other_folder, 'switch_both.png'))
            self.switch.image = pygame.transform.scale(self.switch.image, (80, 40))

        elif self.end:
            self.menu.mouse.update()
            pos = pygame.mouse.get_pos()
            if 230 < pos[0] < 550 and 500 < pos[1] < 700:
                img = pygame.image.load(os.path.join(end_folder, 'again2.png')).convert_alpha()
                img = pygame.transform.scale(img, (320, 200))
                self.end_game.image = img
            else:
                img = pygame.image.load(os.path.join(end_folder, 'again1.png')).convert_alpha()
                img = pygame.transform.scale(img, (320, 200))
                self.end_game.image = img
            if 650 < pos[0] < 970 and 500 < pos[1] < 700:
                img = pygame.image.load(os.path.join(end_folder, 'return_menu2.png')).convert_alpha()
                img = pygame.transform.scale(img, (320, 200))
                self.end_menu.image = img
            else:
                img = pygame.image.load(os.path.join(end_folder, 'return_menu1.png')).convert_alpha()
                img = pygame.transform.scale(img, (320, 200))
                self.end_menu.image = img

        elif self.start:
            if time.time() - self.time_start < 1:
                img_st = pygame.image.load(os.path.join(other_folder, 'three.png')).convert_alpha()
                rect_st = img_st.get_rect(center=(600, 400))
                self.screen.blit(img_st, rect_st)
            elif time.time() - self.time_start < 2:
                img_st = pygame.image.load(os.path.join(other_folder, 'two.png')).convert_alpha()
                rect_st = img_st.get_rect(center=(600, 400))
                self.screen.blit(img_st, rect_st)
            elif time.time() - self.time_start < 3:
                img_st = pygame.image.load(os.path.join(other_folder, 'one.png')).convert_alpha()
                rect_st = img_st.get_rect(center=(600, 400))
                self.screen.blit(img_st, rect_st)
            else:
                self.start = False

        else:
            self.all_sprites.update()
            if self.player.vel.y > 0:
                hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
                if hits:
                    lowest = hits[0]
                    for hit in hits:
                        if hit.rect.bottom > lowest.rect.bottom:
                            lowest = hit

                    if lowest.direct == 1:
                        self.player.pos.x += 2
                    elif lowest.direct == -1:
                        self.player.pos.x += -2

                    if lowest.rect.right + 20 > self.player.pos.x > lowest.rect.left - 20:
                        if self.player.pos.y < lowest.rect.centery + 20:
                            self.player.pos.y = lowest.rect.top + 5
                            self.player.vel.y = 0
                            self.player.jump = False
                            self.booster = False

            if self.get.mode == 0:
                if self.player.rect.top <= HEIGHT / 4:
                    self.player.pos.y += max(abs(self.player.vel.y), 2)
                    if self.get.skin == 4 or self.get.skin == 5 or self.get.skin == 8:
                        self.score += 0.11
                    elif self.bonus:
                        self.score += 0.12
                    elif self.get.skin == 9 or self.get.skin == 10:
                        self.score += 0.05
                    else:
                        self.score += 0.1

                    for plat in self.platforms:
                        plat.rect.y += max(abs(self.player.vel.y), 2)
                        if plat.rect.top >= HEIGHT:
                            plat.kill()
                    for mob in self.enemies:
                        mob.rect.y += max(abs(self.player.vel.y), 2)
                        if mob.rect.top >= HEIGHT:
                            mob.kill()
                    for oth in self.others:
                        oth.rect.y += max(abs(self.player.vel.y), 2)
                        if oth.rect.top >= HEIGHT:
                            oth.kill()
                    for orn in self.ornaments:
                        orn.rect.y += max(abs(self.player.vel.y), 2)
                        if orn.rect.top >= HEIGHT:
                            orn.kill()
                    for cl in self.clouds:
                        cl.rect.y += max(abs(self.player.vel.y), 2)
                        if cl.rect.top >= HEIGHT:
                            cl.kill()
                    for par in self.particles:
                        par.y += max(abs(self.player.vel.y), 2)

            elif self.get.mode == 1:
                self.player.rect.y += 1
                for plat in self.platforms:
                    plat.rect.y += 1
                    if plat.rect.top >= HEIGHT:
                        plat.kill()
                for mob in self.enemies:
                    mob.rect.y += 1
                    if mob.rect.top >= HEIGHT:
                        mob.kill()
                for oth in self.others:
                    oth.rect.y += 1
                    if oth.rect.top >= HEIGHT:
                        oth.kill()
                for orn in self.ornaments:
                    orn.rect.y += 1
                    if orn.rect.top >= HEIGHT:
                        orn.kill()
                for cl in self.clouds:
                    cl.rect.y += 1
                    if cl.rect.top >= HEIGHT:
                        cl.kill()
                for par in self.particles:
                    par.y += 1

                if self.player.rect.top <= HEIGHT / 4:
                    self.player.pos.y += max(abs(self.player.vel.y), 2)
                    if self.get.skin == 4 or self.get.skin == 5 or self.get.skin == 8:
                        self.score += 0.16
                    elif self.bonus:
                        self.score += 0.17
                    elif self.get.skin == 9 or self.get.skin == 10:
                        self.score += 0.1
                    else:
                        self.score += 0.15
                    for plat in self.platforms:
                        plat.rect.y += max(abs(self.player.vel.y), 2)
                    for mob in self.enemies:
                        mob.rect.y += max(abs(self.player.vel.y), 2)
                    for oth in self.others:
                        oth.rect.y += max(abs(self.player.vel.y), 2)
                    for orn in self.ornaments:
                        orn.rect.y += max(abs(self.player.vel.y), 2)
                    for cl in self.clouds:
                        cl.rect.y += max(abs(self.player.vel.y), 2)
                    for par in self.particles:
                        par.y += max(abs(self.player.vel.y), 2)

            while len(self.platforms) < 5:
                rand = random.randrange(150, 400)
                rand_x = random.randrange(0, WIDTH - rand)
                rand_y = random.randrange(-65, -20)
                p = Platform(self, rand_x, rand_y, rand, 40, self.get.theme)

                for entity in self.platforms:
                    if entity == p:
                        continue
                    if abs(p.rect.y - entity.rect.y) < 90:
                        rand_y = rand_y - random.randrange(100, 200)
                        rand = rand - 50
                        p = Platform(self, rand_x, rand_y, rand, 40, self.get.theme)

                self.all_sprites.add(p)
                self.platforms.add(p)
                p.ornament()

                if rand < 100:                                                                          # move platforms
                    p.direct = 1
                    self.move_platform.add(p)
                elif rand < 200:
                    p.direct = -1
                    self.move_platform.add(p)

                elif 300 < rand < 350 and len(self.enemies) < 2:                                               # enemies
                    if rand < 250:
                        Enemy(self, rand_x + rand - 150, rand_y - 100, self.get.theme, 1)
                    else:
                        Enemy(self, rand_x + rand - 150, rand_y - 100, self.get.theme, -1)

                elif rand < 370 and len(self.enemies) < 2:
                    Enemy(self, rand_x + rand - 150, rand_y - 80, 4, 0)

                elif -65 < rand_y < -55 and len(self.others) < 1:                                                # boost
                    Boost(self, rand_x + rand - 150, rand_y - 60, 0)
                elif -55 < rand_y < -45 and len(self.others) < 1:                                                # start
                    Boost(self, rand_x + rand - 150, rand_y - 60, self.get.theme + 1)

                elif 200 < rand < 400 and len(self.clouds) < 4:                                                 # clouds
                    width = random.randrange(50, 100)
                    speed = random.randrange(1, 10) * 0.1
                    if rand < 300:
                        cl = Ornament(self, -150, random.randrange(10, 300), width * 2, width, 1, 1, speed)
                    else:
                        cl = Ornament(self, 1250, random.randrange(10, 300), width * 2, width, 1, -1, speed)

                    if self.get.theme == 3:
                        cl.image = pygame.image.load(os.path.join(other_folder, 'cloud1.png')).convert_alpha()
                    else:
                        cl.image = pygame.image.load(os.path.join(other_folder, 'cloud.png')).convert_alpha()
                    cl.image = pygame.transform.scale(cl.image, (width * 2, width))
                    self.clouds.add(cl)

            for monster in self.enemies:
                if not monster.direct == 0:
                    rand_mo = random.randrange(0, 200)
                    if rand_mo == 1 and self.sound_play:
                        if self.get.theme == 3:
                            pygame.mixer.Sound(os.path.join(sounds_folder, 'ghost.mp3')).play().set_volume(0.5)
                        else:
                            pygame.mixer.Sound(os.path.join(sounds_folder, 'monster_sound.mp3')).play().set_volume(0.5)

            for plat in self.move_platform:                                                             # move platforms
                if plat.rect.x < 5:
                    plat.direct = 1
                elif plat.rect.x > WIDTH - 5 - plat.width:
                    plat.direct = -1

                if plat.direct == 1:
                    plat.rect.x += 2
                else:
                    plat.rect.x -= 2

            for mob in self.enemies:                                                                         # move mobs
                hits = pygame.sprite.spritecollide(mob, self.platforms, False)
                if hits:
                    lowest = hits[0]
                    for hit in hits:
                        if hit.rect.bottom > lowest.rect.bottom:
                            lowest = hit
                    if lowest.rect.right < mob.rect.right:
                        mob.direct = -1
                    elif lowest.rect.left > mob.rect.left:
                        mob.direct = 1

            for cl in self.clouds:
                if cl.direction == -1:
                    cl.rect.x -= cl.speed
                else:
                    cl.rect.x += 1

            en_hit = False
            if not self.get.skin == 10:
                if self.get.skin == 9 and self.get.theme == 3:
                    pass
                else:
                    en_hit = pygame.sprite.spritecollide(self.player, self.enemies, False, pygame.sprite.collide_mask)
                    if self.player.attack:
                        for att in en_hit:
                            self.kill_particle = [True, time.time()]
                            x, y = att.rect.center
                            if self.player.last_left and att.rect.x < self.player.rect.x:
                                self.particles.append(Particles(x + 5, y - 5, 6, -1, (230, 230, 230), self.screen, time.time()))
                                self.particles.append(Particles(x - 5, y + 5, 6, -1, (130, 130, 130), self.screen, time.time()))
                                att.kill()
                                self.kill += 1
                                if self.get.skin == 7 or self.get.skin == 8:
                                    self.score += 10
                                if self.sound_play:
                                    pygame.mixer.Sound(os.path.join(sounds_folder, 'kill_sound.mp3')).play()
                            if self.player.last_right and att.rect.x > self.player.rect.x:
                                self.particles.append(Particles(x + 5, y - 5, 6, -1, (230, 230, 230), self.screen, time.time()))
                                self.particles.append(Particles(x - 5, y + 5, 6, -1, (130, 130, 130), self.screen, time.time()))
                                att.kill()
                                self.kill += 1
                                if self.get.skin == 7 or self.get.skin == 8:
                                    self.score += 10
                                if self.sound_play:
                                    pygame.mixer.Sound(os.path.join(sounds_folder, 'kill_sound.mp3')).play()

            other_hit = pygame.sprite.spritecollide(self.player, self.others, False, pygame.sprite.collide_mask)
            if other_hit:
                for oth in other_hit:
                    x, y = oth.rect.center
                    if oth.type == 0:
                        self.player.vel.y = -50
                        self.player.jump = True
                        self.booster = True
                        self.get.boost += 1
                        if self.sound_play:
                            pygame.mixer.Sound(os.path.join(sounds_folder, 'boost_sound.mp3')).play()
                        x, y = self.player.rect.midbottom
                        self.particles.append(Particles(x + 5, y - 5, 6, -1, (153, 221, 255), self.screen, time.time() + 2))
                        self.particles.append(Particles(x - 5, y - 10, 6, -1, (0, 17, 26), self.screen, time.time() + 2))
                    elif oth.type == 1:
                        self.get.star += 1
                        if self.get.skin == 5:
                            self.score += 5
                        if self.sound_play:
                            pygame.mixer.Sound(os.path.join(sounds_folder, 'collect_sound.mp3')).play().set_volume(0.5)
                        self.particles.append(Particles(x + 5, y - 5, 6, 0, (255, 204, 0), self.screen, time.time()))
                        self.particles.append(Particles(x - 5, y + 5, 6, 0, (255, 153, 0), self.screen, time.time()))
                    elif oth.type == 2:
                        self.get.cactus += 1
                        if self.get.skin == 11:
                            self.score += 10
                        if self.sound_play:
                            pygame.mixer.Sound(os.path.join(sounds_folder, 'collect_sound.mp3')).play().set_volume(0.5)
                        self.particles.append(Particles(x + 5, y - 5, 6, 0, (0, 204, 0), self.screen, time.time()))
                        self.particles.append(Particles(x - 5, y + 5, 6, 0, (0, 102, 0), self.screen, time.time()))
                    elif oth.type == 3:
                        self.get.snowflake += 1
                        if self.get.skin == 12:
                            self.score += 10
                        if self.sound_play:
                            pygame.mixer.Sound(os.path.join(sounds_folder, 'collect_sound.mp3')).play().set_volume(0.5)
                        self.particles.append(Particles(x + 5, y - 5, 6, 0, (0, 153, 255), self.screen, time.time()))
                        self.particles.append(Particles(x - 5, y + 5, 6, 0, (0, 51, 204), self.screen, time.time()))
                    elif oth.type == 4:
                        self.get.pumpkin += 1
                        if self.get.skin == 13:
                            self.score += 10
                        if self.sound_play:
                            pygame.mixer.Sound(os.path.join(sounds_folder, 'collect_sound.mp3')).play().set_volume(0.5)
                        self.particles.append(Particles(x + 5, y - 5, 6, 0, (255, 102, 0), self.screen, time.time()))
                        self.particles.append(Particles(x - 5, y + 5, 6, 0, (204, 51, 0), self.screen, time.time()))
                    oth.kill()

            hide = pygame.sprite.spritecollide(self.player, self.ornaments, False, pygame.sprite.collide_mask)
            if hide:
                self.all_sprites.change_layer(self.player, 2)
                pl_hide = True
            else:
                self.all_sprites.change_layer(self.player, 11)
                pl_hide = False

            if self.player.rect.y > HEIGHT:                                                                  # game over
                self.death()
            elif en_hit and not self.player.attack and not pl_hide and not self.booster:
                self.death()

            self.text = self.font.render("Punkty: " + str(int(self.score)), True, (0, 90, 90))

        if self.msg:
            if time.time() - self.time > 5:
                self.mess.rect.y += 1
                if self.mess.rect.y > 810:
                    self.mess.kill()
                    self.msg = False
            elif self.mess.rect.y > 700:
                self.mess.rect.y -= 0.0001

    def death(self):
        if self.sound_play:
            pygame.mixer.Sound(os.path.join(sounds_folder, 'game_over.mp3')).play().set_volume(0.5)
        self.get.death += 1
        end = Pause(self)
        end.end_screen()
        self.player.kill()
        self.end = True

        img = pygame.image.load(os.path.join(end_folder, 'score.png')).convert_alpha()
        img = pygame.transform.scale(img, (245, 75))
        self.end_text = PauseButton(self, 475, 400, 245, 75, img)
        self.all_end.add(self.end_text)

        img = pygame.image.load(os.path.join(end_folder, 'end.png')).convert_alpha()
        img = pygame.transform.scale(img, (600, 375))
        self.end = PauseButton(self, 300, 10, 800, 500, img)
        self.all_end.add(self.end)

        img = pygame.image.load(os.path.join(end_folder, 'again1.png')).convert_alpha()
        img = pygame.transform.scale(img, (320, 200))
        self.end_game = PauseButton(self, 230, 500, 320, 200, img)
        self.all_end.add(self.end_game)

        img = pygame.image.load(os.path.join(end_folder, 'return_menu1.png')).convert_alpha()
        img = pygame.transform.scale(img, (320, 200))
        self.end_menu = PauseButton(self, 650, 500, 320, 200, img)
        self.all_end.add(self.end_menu)

        self.text_end = self.font.render("Twój wynik: " + str(int(self.score)), True, (0, 90, 90))
        self.text_end_rect = self.text_end.get_rect()
        self.text_end_rect.topleft = (500, 420)

        self.save_score()
        pygame.mixer.music.stop()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and not self.pause:
                    self.pause = True
                    self.pauseObj = Pause(self)
                    self.pauseObj.pause_screen()

                    img = pygame.image.load(os.path.join(pause_folder, 'pause.png')).convert_alpha()
                    img = pygame.transform.scale(img, (600, 375))
                    self.pause_text = PauseButton(self, 300, 10, 800, 500, img)
                    self.all_pause.add(self.pause_text)

                    img = pygame.image.load(os.path.join(pause_folder, 'return_game1.png')).convert_alpha()
                    img = pygame.transform.scale(img, (320, 200))
                    self.pause_game = PauseButton(self, 230, 400, 320, 200, img)
                    self.all_pause.add(self.pause_game)

                    img = pygame.image.load(os.path.join(pause_folder, 'return_menu1.png')).convert_alpha()
                    img = pygame.transform.scale(img, (320, 200))
                    self.pause_menu = PauseButton(self, 650, 400, 320, 200, img)
                    self.all_pause.add(self.pause_menu)

                    self.switch = TriumpfRect(1110, 10, 80, 40)
                    self.all_pause.add(self.switch)

                elif event.key == pygame.K_ESCAPE and self.pause:
                    for obj in self.all_pause:
                        obj.kill()
                    self.pause = False

                if event.key == pygame.K_UP and not self.pause and not self.booster:
                    self.player.jumpy(PLAYER_JUMP)
                    self.player.jump = True

            pos = pygame.mouse.get_pos()
            if self.pause and event.type == pygame.MOUSEBUTTONUP:                                                # pause
                if 230 < pos[0] < 550 and 400 < pos[1] < 600:                                                # back game
                    if self.sound_play:
                        self.click.play()
                    for obj in self.all_pause:
                        obj.kill()
                    self.pause = False
                elif 650 < pos[0] < 970 and 400 < pos[1] < 600:                                              # back menu
                    if self.sound_play:
                        self.click.play()
                    for obj in self.all_pause:
                        obj.kill()
                    for obj in self.all_sprites:
                        obj.kill()

                    self.save_score()
                    self.pause = False
                    self.menu.new()
                    self.new()

                elif 1110 < pos[0] < 1150 and 10 < pos[1] < 50:
                    if self.sound_play:
                        self.sound_play = False
                    else:
                        self.sound_play = True
                elif 1150 < pos[0] < 1190 and 10 < pos[1] < 50:
                    if self.music_play:
                        self.music_play = False
                        pygame.mixer.music.pause()
                    else:
                        self.music_play = True
                        pygame.mixer.music.unpause()

            if self.end and event.type == pygame.MOUSEBUTTONUP:                                                    # end
                if 230 < pos[0] < 550 and 500 < pos[1] < 700:                                                 # new game
                    if self.sound_play:
                        self.click.play()
                    for obj in self.all_end:
                        obj.kill()
                    for obj in self.all_sprites:
                        obj.kill()
                    self.end = False
                    self.save_score()
                    self.new()

                if 650 < pos[0] < 970 and 500 < pos[1] < 700:                                                # back menu
                    if self.sound_play:
                        self.click.play()
                    for obj in self.all_end:
                        obj.kill()
                    for obj in self.all_sprites:
                        obj.kill()
                    self.end = False
                    self.save_score()
                    self.menu.new()
                    self.new()

    def save_score(self):
        self.score = int(self.score)
        nick = []
        for i in range(0, len(self.get.score) - 1):
            nick.append(self.get.score[i][0])

        k = (self.get.nick, self.score)
        have = self.get.nick in nick
        if have:
            index = nick.index(self.get.nick)
            if self.get.score[index][1] < self.score:
                self.get.score[index] = k

        if not have:
            self.get.score.append(k)

        file = open("Set.obj", "wb")
        try:
            pickle.dump(self.get, file)
        finally:
            file.close()

    def draw(self):
        pygame.display.update()
        if not self.start:
            if self.pause:
                background = pygame.image.load(os.path.join(pause_folder, 'screen.png')).convert()
                background_rect = background.get_rect()
                background_rect.center = WIDTH // 2, HEIGHT // 2
                self.screen.blit(background, background_rect)
                pygame.draw.rect(self.screen, (0, 0, 0), background_rect, 1)
                self.all_pause.draw(self.screen)
                self.menu.mouse.update()
                self.mouse.draw(self.screen)
            elif self.end:
                background = pygame.image.load(os.path.join(end_folder, 'screen.png')).convert()
                background_rect = background.get_rect()
                background_rect.center = WIDTH // 2, HEIGHT // 2
                self.screen.blit(background, background_rect)
                pygame.draw.rect(self.screen, (0, 0, 0), background_rect, 1)
                self.all_end.draw(self.screen)
                self.screen.blit(self.text_end, self.text_end_rect)
                self.menu.mouse.update()
                self.mouse.draw(self.screen)

            else:
                self.all_sprites.draw(self.screen)
                self.screen.blit(self.text, self.text_rect)

                for par in self.particles:
                    if time.time() - par.time < 2:
                        par.add_particles()
                    par.emit()
                    if len(par.particles) == 0:
                        self.particles.remove(par)

        pygame.display.flip()

    def check(self):
        if not self.get.triumpfs[4]:
            if self.score >= 500:
                self.get.triumpfs[4] = True
                self.message()
        if not self.get.triumpfs[5]:
            if self.score >= 1000:
                self.get.triumpfs[5] = True
                self.message()
        if not self.get.triumpfs[6]:
            if self.get.boost >= 50:
                self.get.triumpfs[6] = True
                self.message()
        if not self.get.triumpfs[7]:
            if self.get.boost >= 100:
                self.get.triumpfs[7] = True
                self.message()
        if not self.get.triumpfs[8]:
            if self.kill >= 50:
                self.get.triumpfs[8] = True
                self.message()
        if not self.get.triumpfs[9]:
            if self.get.death >= 100:
                self.get.triumpfs[9] = True
                self.message()
        if not self.get.triumpfs[10]:
            if self.get.death >= 200:
                self.get.triumpfs[10] = True
                self.message()
        if not self.get.triumpfs[11]:
            if self.get.cactus >= 50:
                self.get.triumpfs[11] = True
                self.message()
        if not self.get.triumpfs[12]:
            if self.get.snowflake >= 50:
                self.get.triumpfs[12] = True
                self.message()
        if not self.get.triumpfs[13]:
            if self.get.pumpkin >= 50:
                self.get.triumpfs[13] = True
                self.message()
        if not self.get.triumpfs_map[1]:
            if self.get.star >= 50:
                self.get.triumpfs_map[1] = True
                self.message()
        if not self.get.triumpfs_map[2]:
            if self.get.star >= 100:
                self.get.triumpfs_map[2] = True
                self.message()
        if not self.get.triumpfs_map[3]:
            if self.get.star >= 150:
                self.get.triumpfs_map[3] = True
                self.message()

    def message(self):
        self.mess = TriumpfRect(900, 810, 300, 100)
        self.mess.image = pygame.image.load(os.path.join(triumpf_folder, 'message.png')).convert_alpha()
        self.all_sprites.add(self.mess)
        self.all_end.add(self.mess)
        self.time = time.time()
        self.msg = True
        if self.sound_play:
            effect = pygame.mixer.Sound(os.path.join(sounds_folder, 'msg_sound.mp3'))
            effect.set_volume(0.5)
            effect.play()

    def music(self):
        if not self.music_play:
            pygame.mixer.music.pause()


engine = Engine()
while engine.running:
    engine.menu.new()
    engine.new()

pygame.quit()
