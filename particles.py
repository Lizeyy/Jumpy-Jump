import pygame
import random


class Particles:
    def __init__(self, x, y, radius, dir, color, surface, time):
        self.particles = []
        self.x = x
        self.y = y
        self.radius = radius
        self.dir = dir
        self.color = color
        self.surface = surface
        self.time = time

    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][0]
                particle[0][0] += particle[2][1]
                particle[1] -= 0.02
                pygame.draw.circle(self.surface, self.color, particle[0], int(particle[1]))

    def add_particles(self):
        if self.dir == 0:
            dir_x = random.randint(-10, 10) / 10
            dir_y = random.randint(-10, 10) / 10 - 1
            x = random.randint(self.x - 20, self.x + 20)
            y = random.uniform(self.y - 20, self.y + 20)
            par = [[x, y], random.randint(3, 6), [dir_y, dir_x]]
            self.particles.append(par)
        if self.dir == 1:
            dir_x = random.randint(-2, 2)
            dir_y = random.randint(0, 10) / 10
            x = random.randint(self.x - 20, self.x + 20)
            y = random.uniform(self.y - 20, self.y + 20)
            par = [[x, y], random.randint(0, 3), [dir_y, dir_x]]
            self.particles.append(par)
        if self.dir == -1:
            dir_x = random.randint(-2, 2)
            dir_y = random.randint(-10, 0) / 10
            x = random.randint(self.x - 20, self.x + 20)
            y = random.uniform(self.y - 20, self.y + 20)
            par = [[x, y], random.randint(3, 7), [dir_y, dir_x]]
            self.particles.append(par)

    def delete_particles(self):
        par_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = par_copy
