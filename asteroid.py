import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        radius = self.radius
        velocity = self.velocity
        xpos = self.position.x
        ypos = self.position.y
        if radius > ASTEROID_MIN_RADIUS:
            delta = random.uniform(20,50)
            for _ in range(2):
                delta = -delta
                asteroid = Asteroid(xpos, ypos, radius - ASTEROID_MIN_RADIUS)
                asteroid.velocity = velocity.rotate(delta) * 1.2
                #asteroid.velocity += pygame.Vector2(1, 1).rotate(delta) * 1.2
        self.kill()