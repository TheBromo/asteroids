from pygame import Vector2
import pygame
from circleshape import CircleShape
from constants import SHOOT_RADIUS


class Shot(CircleShape):
    def __init__(self, position: Vector2):
        super().__init__(position.x, position.y, SHOOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
