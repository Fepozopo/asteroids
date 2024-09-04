import pygame
import constants


def main():
    # Initialize pygame
    pygame.init()

    # Print a few things to the console
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    # Create the screen
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Use the screen's fill method to fill the screen with a solid "black" color.
            screen.fill((0, 0, 0))
            # Use pygame's display.flip() method to refresh the screen.
            pygame.display.flip()

        # Update
        pygame.display.update()


if __name__ == "__main__":
    main()