import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED


class Player(CircleShape):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def turn(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        # https://en.wikipedia.org/wiki/Unit_vector
        # create a vector from (0,0) to (0,1), rotate vector by players
        # rotation to point in the direction the player is facing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # the vector is added to current position to move player
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.turn(-dt)
        if keys[pygame.K_d]:
            self.turn(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
