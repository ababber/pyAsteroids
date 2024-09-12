import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    print("Starting asteroids!")
    pygame.init()
    # use pygame to set gui window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # simple game loop using an infinite loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # black screen
        # pygame.Surface.fill(screen, (0, 0, 0))

        # white screen
        pygame.Surface.fill(screen, (255, 255, 255))

        pygame.display.flip()


if __name__ == "__main__":
    main()
