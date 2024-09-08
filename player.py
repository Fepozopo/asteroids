import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot



PLAYER_SHOOT_COOLDOWN = 0.3

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.timer = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    
    def draw(self, screen):
        pygame.draw.polygon(screen, pygame.Color("white"), self.triangle(), width=2)


    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED


    def update(self, dt):
        # Decrease the timer by dt (time delta)
        if self.timer > 0:
            self.timer -= dt

        # Ensure the timer doesn't go below 0
        if self.timer < 0:
            self.timer = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Call the rotate method with the dt argument
            self.rotate(-dt)

        if keys[pygame.K_d]:
            # Call the rotate method with the dt argument
            self.rotate(dt)

        if keys[pygame.K_w]:
            # Call the move method with the dt argument
            self.move(dt)

        if keys[pygame.K_s]:
            # Call the move method with the dt argument
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            # Call the shoot method with the dt argument
            self.shoot(dt)

    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * dt * PLAYER_SPEED


    def shoot(self, dt):
        # Create a new shot if the player is allowed to
        if self.timer == 0:
            shot = Shot(self.position.x, self.position.y, PLAYER_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN