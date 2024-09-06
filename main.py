import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField



def main():
    # Initialize pygame
    pygame.init()

    # Set up the clock
    clock = pygame.time.Clock()
    dt = 0

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create some groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Create the player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    # Create the asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Create the asteroid field
    AsteroidField()


    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Use the screen's fill method to fill the screen with a solid "black" color.
        screen.fill((0, 0, 0))

        # Update the player
        for updatables in updatable:
            updatables.update(dt)

        # Draw the player
        for drawables in drawable:
            drawables.draw(screen)

        # Use pygame's display.flip() method to refresh the screen.
        pygame.display.flip()

        # Update the delta time
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
    