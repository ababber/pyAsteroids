import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, 1)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return

        rand_angl = random.uniform(20, 50)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        v0 = self.velocity.rotate(rand_angl)
        v1 = self.velocity.rotate(-rand_angl)

        new_ast0 = Asteroid(self.position.x, self.position.y, new_rad)
        new_ast1 = Asteroid(self.position.x, self.position.y, new_rad)

        new_ast0.velocity = v0 * 1.2
        new_ast1.velocity = v1 * 1.2
