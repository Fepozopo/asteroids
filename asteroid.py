import pygame, random
from circleshape import CircleShape
from constants import *



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        # Draw the asteroid
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)


    def update(self, dt):
        # Move the asteroid in a straight line at a constant speed
        self.position += self.velocity * dt

    
    def split(self):
        # .kill() the asteroid
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # Use random.uniform to generate a random angle between 20 and 50 degrees
            random_angle = random.uniform(20, 50)
            # Use the rotate method on the asteroid's velocity vector to create 2 new vectors, that are rotated by angle and -angle respectively
            new_vector1 = self.velocity.rotate(random_angle)
            new_vector2 = self.velocity.rotate(-random_angle)
            # Compute the new radius of the smaller asteroids using the formula old_radius - ASTEROID_MIN_RADIUS
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            # Create 2 new asteroids using the new position and velocity
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_vector1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = new_vector2 * 1.2