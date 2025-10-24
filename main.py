import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player_triangle = player.Player(x, y)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        player_triangle.draw(screen)
        dt = clock.tick(60) / 1000
        player_triangle.update(dt)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
