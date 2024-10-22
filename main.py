import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    print("Starting asteroids!")
    pygame.init()
    # use pygame to set gui window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # restrict fps to 60 by counting delta time since last frame drawn
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player_0 = Player(x, y)

    # simple game loop using an infinite loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # black screen
        # pygame.Surface.fill(screen, (0, 0, 0))

        # white screen
        # pygame.Surface.fill(screen, (255, 255, 255))

        # better way to display black/white screen
        screen.fill("black")

        # redraws player
        player_0.draw(screen)

        # refreshes screen
        pygame.display.flip()

        # limit frame rate to 60 fps
        tick = clock.tick(60)
        dt = tick / 1000


if __name__ == "__main__":
    main()
