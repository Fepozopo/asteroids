import pygame, constants, player



def main():
    # Initialize pygame
    pygame.init()

    # Set up the clock
    clock = pygame.time.Clock()
    dt = 0

    # Create the screen
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    # Create the player
    player_object = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.PLAYER_RADIUS)


    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Use the screen's fill method to fill the screen with a solid "black" color.
        screen.fill((0, 0, 0))

        # Draw the player
        player_object.draw(screen)

        # Update the player
        player_object.update(dt)

        # Use pygame's display.flip() method to refresh the screen.
        pygame.display.flip()

        # Update the delta time
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
    