import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting asteroids!")
    pygame.init()
    # use pygame to set gui window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group
    # intended to hold and manage multiple game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # groups added to static field containers, do this before a class instance init
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    # restrict fps to 60 by counting delta time since last frame drawn
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player_0 = Player(x, y)
    asteroid_field = AsteroidField()

    # simple game loop using an infinite loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update player position before redraw to prevent lag
        # player_0.update(dt)

        # update all updatable items with iter pygame Group()
        for obj in updatable:
            obj.update(dt)

        # black screen
        # pygame.Surface.fill(screen, (0, 0, 0))

        # white screen
        # pygame.Surface.fill(screen, (255, 255, 255))

        # better way to display black/white screen
        screen.fill("black")

        # redraws player
        # player_0.draw(screen)

        # draw all drawable items with iter pygame Group()
        for obj in drawable:
            obj.draw(screen)

        # refreshes screen
        pygame.display.flip()

        # limit frame rate to 60 fps
        tick = clock.tick(60)
        dt = tick / 1000


if __name__ == "__main__":
    main()
