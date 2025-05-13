import random
from turtle import position
from circleshape import CircleShape
import pygame

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        deg = random.uniform(20, 50)
        vel1 = self.velocity.rotate(deg) * 1.2
        vel2 = self.velocity.rotate(-deg) * 1.2
        radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, radius)
        a2 = Asteroid(self.position.x, self.position.y, radius)
        a1.velocity = vel1
        a2.velocity = vel2
