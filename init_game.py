"""
This module initializes the Pygame library, sets up the game window,
and starts the main game loop for the Sisters Quest game.
"""

# Dependencies
import pygame
import sys

# Game Initialization Function
def init_game():
    # Start pygame environment
    pygame.init()

    # Set up display (800x600)
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))

    # Set title
    pygame.display.set_caption("Sisters Quest")

    # Define colors
    WHITE = (255,255,255)

    # Set up a clock to control frame rate
    clock = pygame.time.Clock()

    # Game loop
    while run:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Fill the screen with white color
        screen.fill(WHITE)

        # Update display
        pygame.display.flip()

        # Cap frame rate to 60 FPS
        clock.tick(60)

    # Clean up and close game
    pygame.quit()
    sys.quit()