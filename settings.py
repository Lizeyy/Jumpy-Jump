import os
import pygame

TITLE = "Jumpy Jump!"

WIDTH = 1200
HEIGHT = 800
FPS = 60

PLAYER_SPEED_X = 1.4
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 0.8
PLAYER_JUMP = 20

PLATFORM_LIST = [(-10, HEIGHT - 60, WIDTH + 20, 80),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 200, 40),
                 (125, HEIGHT - 350, 150, 40),
                 (350, 300, 180, 40),
                 (WIDTH - 550, HEIGHT - 650, 300, 40)]

game_folder = os.path.dirname(__file__)
data_folder = os.path.join(game_folder, 'data')
graphics_folder = os.path.join(data_folder, 'graphics')
menu_folder = os.path.join(graphics_folder, 'menu')
sprites_folder = os.path.join(graphics_folder, 'sprites')
editor_folder = os.path.join(graphics_folder, 'editor')
themes_folder = os.path.join(graphics_folder, 'themes')
pause_folder = os.path.join(graphics_folder, 'pause')
end_folder = os.path.join(graphics_folder, 'end')
other_folder = os.path.join(graphics_folder, 'other')
triumpf_folder = os.path.join(graphics_folder, 'triumpf')
credits_folder = os.path.join(graphics_folder, 'credits')
music_folder = os.path.join(data_folder, 'sounds\music')
sounds_folder = os.path.join(data_folder, 'sounds\effects')

ICON = pygame.image.load(os.path.join(other_folder, 'cloud1.png'))
