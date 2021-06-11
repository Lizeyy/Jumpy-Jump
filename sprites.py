import pygame
from settings import *


def load2(path, names):
    images = []
    for i in range(1, 3):
        name = names + str(i) + '.png'
        images.append(pygame.image.load(os.path.join(path, name)))
    return images


def load8(path, names):
    images = []
    for i in range(1, 9):
        name = names + str(i) + '.png'
        images.append(pygame.image.load(os.path.join(path, name)))
    return images


def load10(path, names):
    images = []
    for i in range(1, 11):
        name = names + str(i) + '.png'
        images.append(pygame.image.load(os.path.join(path, name)))
    return images


def load11(path, names):
    images = []
    for i in range(1, 12):
        name = names + str(i) + '.png'
        images.append(pygame.image.load(os.path.join(path, name)))
    return images


def load13(path, names):
    images = []
    for i in range(1, 14):
        name = names + str(i) + '.png'
        images.append(pygame.image.load(os.path.join(path, name)))
    return images


def load15(path, names):
    images = []
    for i in range(1, 16):
        name = names + str(i) + '.png'
        images.append(pygame.image.load(os.path.join(path, name)))
    return images


def load16(path, names):
    images = []
    for i in range(1, 17):
        name = names + str(i) + '.png'
        images.append(pygame.image.load(os.path.join(path, name)))
    return images


def transform(images):
    transforms = []
    for img in images:
        transforms.append(pygame.transform.flip(img, True, False))
    return transforms


# folders --------------------------------------------------------------------------------------------------------------
adventure_boy_folder = os.path.join(sprites_folder, 'adventure_boy')
adventure_girl_folder = os.path.join(sprites_folder, 'adventure_girl')
boy_folder = os.path.join(sprites_folder, 'boy')
cat_folder = os.path.join(sprites_folder, 'cat')
dog_folder = os.path.join(sprites_folder, 'dog')
girl_folder = os.path.join(sprites_folder, 'girl')
jack_folder = os.path.join(sprites_folder, 'jack')
knight_folder = os.path.join(sprites_folder, 'knight')
ninja_boy_folder = os.path.join(sprites_folder, 'ninja_boy')
ninja_girl_folder = os.path.join(sprites_folder, 'ninja_girl')
robot_folder = os.path.join(sprites_folder, 'robot')
santa_folder = os.path.join(sprites_folder, 'santa')
zombie_boy_folder = os.path.join(sprites_folder, 'zombie_boy')
zombie_girl_folder = os.path.join(sprites_folder, 'zombie_girl')


# ----------------------------------------------------------------------------------------------------------------------
adventure_boy_run_right = load10(adventure_boy_folder, 'run')
adventure_boy_run_left = transform(adventure_boy_run_right)
adventure_boy_idle_right = load10(adventure_boy_folder, 'idle')
adventure_boy_idle_left = transform(adventure_boy_idle_right)
adventure_boy_jump_right = load10(adventure_boy_folder, 'jump')
adventure_boy_jump_left = transform(adventure_boy_jump_right)

adventure_girl_run_right = load8(adventure_girl_folder, 'run')
adventure_girl_run_left = transform(adventure_girl_run_right)
adventure_girl_idle_right = load8(adventure_girl_folder, 'idle')
adventure_girl_idle_left = transform(adventure_girl_idle_right)
adventure_girl_jump_right = load8(adventure_girl_folder, 'jump')
adventure_girl_jump_left = transform(adventure_girl_jump_right)

boy_run_right = load15(boy_folder, 'run')
boy_run_left = transform(boy_run_right)
boy_idle_right = load15(boy_folder, 'idle')
boy_idle_left = transform(boy_idle_right)
boy_jump_right = load15(boy_folder, 'jump')
boy_jump_left = transform(boy_jump_right)

cat_run_right = load8(cat_folder, 'run')
cat_run_left = transform(cat_run_right)
cat_idle_right = load8(cat_folder, 'idle')
cat_idle_left = transform(cat_idle_right)
cat_jump_right = load8(cat_folder, 'jump')
cat_jump_left = transform(cat_jump_right)

dog_run_right = load8(dog_folder, 'run')
dog_run_left = transform(dog_run_right)
dog_idle_right = load8(dog_folder, 'idle')
dog_idle_left = transform(dog_idle_right)
dog_jump_right = load8(dog_folder, 'jump')
dog_jump_left = transform(dog_jump_right)

girl_run_right = load16(girl_folder, 'run')
girl_run_left = transform(girl_run_right)
girl_idle_right = load16(girl_folder, 'idle')
girl_idle_left = transform(girl_idle_right)
girl_jump_right = load16(girl_folder, 'jump')
girl_jump_left = transform(girl_jump_right)

jack_run_right = load8(jack_folder, 'run')
jack_run_left = transform(jack_run_right)
jack_idle_right = load8(jack_folder, 'idle')
jack_idle_left = transform(jack_idle_right)
jack_jump_right = load8(jack_folder, 'jump')
jack_jump_left = transform(jack_jump_right)

knight_run_right = load8(knight_folder, 'run')
knight_run_left = transform(knight_run_right)
knight_idle_right = load8(knight_folder, 'idle')
knight_idle_left = transform(knight_idle_right)
knight_jump_right = load8(knight_folder, 'jump')
knight_jump_left = transform(knight_jump_right)
knight_attack_right = load10(knight_folder, 'attack')
knight_attack_left = transform(knight_attack_right)

ninja_boy_run_right = load10(ninja_boy_folder, 'run')
ninja_boy_run_left = transform(ninja_boy_run_right)
ninja_boy_idle_right = load10(ninja_boy_folder, 'idle')
ninja_boy_idle_left = transform(ninja_boy_idle_right)
ninja_boy_jump_right = load10(ninja_boy_folder, 'jump')
ninja_boy_jump_left = transform(ninja_boy_jump_right)
ninja_boy_attack_right = load10(ninja_boy_folder, 'attack')
ninja_boy_attack_left = transform(ninja_boy_attack_right)

ninja_girl_run_right = load10(ninja_girl_folder, 'run')
ninja_girl_run_left = transform(ninja_girl_run_right)
ninja_girl_idle_right = load10(ninja_girl_folder, 'idle')
ninja_girl_idle_left = transform(ninja_girl_idle_right)
ninja_girl_jump_right = load10(ninja_girl_folder, 'jump')
ninja_girl_jump_left = transform(ninja_girl_jump_right)
ninja_girl_attack_right = load10(ninja_girl_folder, 'attack')
ninja_girl_attack_left = transform(ninja_girl_attack_right)

robot_run_right = load8(robot_folder, 'run')
robot_run_left = transform(robot_run_right)
robot_idle_right = load8(robot_folder, 'idle')
robot_idle_left = transform(robot_idle_right)
robot_jump_right = load8(robot_folder, 'jump')
robot_jump_left = transform(robot_jump_right)

santa_run_right = load11(santa_folder, 'run')
santa_run_left = transform(santa_run_right)
santa_idle_right = load11(santa_folder, 'idle')
santa_idle_left = transform(santa_idle_right)
santa_jump_right = load11(santa_folder, 'jump')
santa_jump_left = transform(santa_jump_right)

zombie_boy_run_right = load10(zombie_boy_folder, 'run')
zombie_boy_run_left = transform(zombie_boy_run_right)
zombie_boy_idle_right = load10(zombie_boy_folder, 'idle')
zombie_boy_idle_left = transform(zombie_boy_idle_right)
zombie_boy_jump_right = load10(zombie_boy_folder, 'jump')
zombie_boy_jump_left = transform(zombie_boy_jump_right)

zombie_girl_run_right = load10(zombie_girl_folder, 'run')
zombie_girl_run_left = transform(zombie_girl_run_right)
zombie_girl_idle_right = load10(zombie_girl_folder, 'idle')
zombie_girl_idle_left = transform(zombie_girl_idle_right)
zombie_girl_jump_right = load10(zombie_girl_folder, 'jump')
zombie_girl_jump_left = transform(zombie_girl_jump_right)


# ----------------------------------------------------------------------------------------------------------------------
en_ghost_folder = os.path.join(sprites_folder, 'en_ghost')
en_monster_blue_folder = os.path.join(sprites_folder, 'en_monster_blue')
en_monster_orange_folder = os.path.join(sprites_folder, 'en_monster_orange')
en_monster_green_folder = os.path.join(sprites_folder, 'en_monster_green')
en_folder = os.path.join(sprites_folder, 'en')

en_ghost_run_left = load11(en_ghost_folder, 'idle')
en_ghost_run_right = transform(en_ghost_run_left)

en_monster_blue_run_left = load13(en_monster_blue_folder, 'run')
en_monster_blue_run_right = transform(en_monster_blue_run_left)

en_monster_orange_run_left = load13(en_monster_orange_folder, 'run')
en_monster_orange_run_right = transform(en_monster_orange_run_left)

en_monster_green_run_left = load13(en_monster_green_folder, 'run')
en_monster_green_run_right = transform(en_monster_green_run_left)

en_left = load2(en_folder, 'idle')
en_right = transform(en_left)


# ----------------------------------------------------------------------------------------------------------------------
run_left = [girl_run_left, boy_run_left, dog_run_left, cat_run_left, adventure_boy_run_left, adventure_girl_run_left,
            ninja_girl_run_left, ninja_boy_run_left, knight_run_left, zombie_boy_run_left, zombie_girl_run_left,
            robot_run_left, santa_run_left, jack_run_left]

run_right = [girl_run_right, boy_run_right, dog_run_right, cat_run_right, adventure_boy_run_right,
             adventure_girl_run_right, ninja_girl_run_right, ninja_boy_run_right, knight_run_right, zombie_boy_run_right,
             zombie_girl_run_right, robot_run_right, santa_run_right, jack_run_right]

idle_left = [girl_idle_left, boy_idle_left, dog_idle_left, cat_idle_left, adventure_boy_idle_left,
             adventure_girl_idle_left, ninja_girl_idle_left, ninja_boy_idle_left, knight_idle_left,
             zombie_boy_idle_left, zombie_girl_idle_left, robot_idle_left, santa_idle_left, jack_idle_left]

idle_right = [girl_idle_right,  boy_idle_right, dog_idle_right, cat_idle_right, adventure_boy_idle_right,
              adventure_girl_idle_right, ninja_girl_idle_right, ninja_boy_idle_right, knight_idle_right,
              zombie_boy_idle_right, zombie_girl_idle_right, robot_idle_right, santa_idle_right, jack_idle_right]

jump_left = [girl_jump_left, boy_jump_left, dog_jump_left, cat_jump_left, adventure_boy_jump_left,
             adventure_girl_jump_left, ninja_girl_jump_left, ninja_boy_jump_left, knight_jump_left,
             zombie_boy_jump_left, zombie_girl_jump_left, robot_jump_left, santa_jump_left, jack_run_left]

jump_right = [girl_jump_right, boy_jump_right, dog_jump_right, cat_jump_right, adventure_boy_jump_right,
              adventure_girl_jump_right, ninja_girl_jump_right, ninja_boy_jump_right, knight_jump_right,
              zombie_boy_jump_right, zombie_girl_jump_right, robot_jump_right, santa_jump_right, jack_jump_right]

attack_left = [ninja_boy_attack_left, ninja_girl_attack_left, knight_attack_left]

attack_right = [ninja_boy_attack_right, ninja_girl_attack_right, knight_attack_right]


en_run_left = [en_monster_green_run_left, en_monster_orange_run_left, en_monster_blue_run_left, en_ghost_run_left,
               en_left]

en_run_right = [en_monster_green_run_right, en_monster_orange_run_right, en_monster_blue_run_right, en_ghost_run_right,
                en_right]


# ----------------------------------------------------------------------------------------------------------------------
default_folder = os.path.join(themes_folder, 'default')
default_icon = pygame.image.load(os.path.join(default_folder, 'icon.png'))
default_back = pygame.image.load(os.path.join(default_folder, 'back.png'))
default_platform0 = pygame.image.load(os.path.join(default_folder, 'platform0.png'))
default_platform1 = pygame.image.load(os.path.join(default_folder, 'platform1.png'))
default_platform2 = pygame.image.load(os.path.join(default_folder, 'platform2.png'))
default_platform3 = pygame.image.load(os.path.join(default_folder, 'platform3.png'))

desert_folder = os.path.join(themes_folder, 'desert')
desert_icon = pygame.image.load(os.path.join(desert_folder, 'icon.png'))
desert_back = pygame.image.load(os.path.join(desert_folder, 'back.png'))
desert_platform0 = pygame.image.load(os.path.join(desert_folder, 'platform0.png'))
desert_platform1 = pygame.image.load(os.path.join(desert_folder, 'platform1.png'))
desert_platform2 = pygame.image.load(os.path.join(desert_folder, 'platform2.png'))
desert_platform3 = pygame.image.load(os.path.join(desert_folder, 'platform3.png'))

winter_folder = os.path.join(themes_folder, 'winter')
winter_icon = pygame.image.load(os.path.join(winter_folder, 'icon.png'))
winter_back = pygame.image.load(os.path.join(winter_folder, 'back.png'))
winter_platform0 = pygame.image.load(os.path.join(winter_folder, 'platform0.png'))
winter_platform1 = pygame.image.load(os.path.join(winter_folder, 'platform1.png'))
winter_platform2 = pygame.image.load(os.path.join(winter_folder, 'platform2.png'))
winter_platform3 = pygame.image.load(os.path.join(winter_folder, 'platform3.png'))

spooky_folder = os.path.join(themes_folder, 'spooky')
spooky_icon = pygame.image.load(os.path.join(spooky_folder, 'icon.png'))
spooky_back = pygame.image.load(os.path.join(spooky_folder, 'back.png'))
spooky_platform0 = pygame.image.load(os.path.join(spooky_folder, 'platform0.png'))
spooky_platform1 = pygame.image.load(os.path.join(spooky_folder, 'platform1.png'))
spooky_platform2 = pygame.image.load(os.path.join(spooky_folder, 'platform2.png'))
spooky_platform3 = pygame.image.load(os.path.join(spooky_folder, 'platform3.png'))


icons_list = [default_icon, desert_icon, winter_icon, spooky_icon]
back_list = [default_back, desert_back, winter_back, spooky_back]
platform0_list = [default_platform0, desert_platform0, winter_platform0, spooky_platform0]
platform1_list = [default_platform1, desert_platform1, winter_platform1, spooky_platform1]
platform2_list = [default_platform2, desert_platform2, winter_platform2, spooky_platform2]
platform3_list = [default_platform3, desert_platform3, winter_platform3, spooky_platform3]


# ----------------------------------------------------------------------------------------------------------------------
