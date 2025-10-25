from typing import dataclass_transform
from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * MOVE_SPEED * dt

    def shoot(self, dt):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED

    def update(self, dt):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.rotate(dt * -1)

        if key[pygame.K_d]:
            self.rotate(dt)

        if key[pygame.K_s]:
            self.move(dt * -1)

        if key[pygame.K_w]:
            self.move(dt)

        if key[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot(dt)
                self.timer = SHOT_COUNTDOWN
        self.timer -= dt
