"""
This module initializes the Pygame library, sets up the game window,
and starts the main game loop for the Sisters Quest game.
"""

# Dependencies
import pygame
import sys
from load_assets import load_assets

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

    # Load assets
    assets = load_assets()

    # Game loop flag
    run = True

    # Intro screen loop
    while run:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    play_button_rect = assets['play_button'].get_rect(topleft=(300,400))
                    if play_button_rect.collidepoint(mouse_pos):
                        run = False

        # Draw the intro screen
        screen.blit(assets['intro_background'], (0,0))
        screen.blit(assets['title_text'], (100,100))
        screen.blit(assets['play_button'], (300,400))

        # Update display
        pygame.display.flip()

        # Cap frame rate to 60 FPS
        clock.tick(60)

    # Clean up and close game
    pygame.quit()
    sys.exit()