import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import player
from asteroids import *
import asteroidfield
import sys
import shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    shot.Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = updatable
    player.Player.containers = (updatable, drawable)
    player_triangle = player.Player(x, y)
    asteroids_field = asteroidfield.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        updatable.update(dt)
        # checking for collition of player and asteroids
        for asteroid in asteroids:
            if asteroid.collition(player_triangle):
                sys.exit("Game Over!")

            for bullet in shots:
                if bullet.collition(asteroid):
                    bullet.kill()
                    asteroid.split()

        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
