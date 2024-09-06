import pygame
from circleshape import CircleShape



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        # Draw the asteroid
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)


    def update(self, dt):
        # Move the asteroid in a straight line at a constant speed
        self.position += self.velocity * dt