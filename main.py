import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



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
    shots = pygame.sprite.Group()

    # Create the player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    # Create the asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Create the shots
    Shot.containers = (shots, updatable, drawable)

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

        # Update the sprites
        for updatables in updatable:
            updatables.update(dt)

        # Check if any asteroids have collided with the player or shot
        for asteroid in asteroids:
            if CircleShape.collide(player, asteroid) is True:
                print("Game over!")
                running = False
            for shot in shots:
                if CircleShape.collide(asteroid, shot) is True:
                    # Destroy the asteroid and the shot object
                    shot.kill()
                    asteroid.kill()

        # Draw the sprites
        for drawables in drawable:
            drawables.draw(screen)

        # Use pygame's display.flip() method to refresh the screen.
        pygame.display.flip()

        # Update the delta time
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
    