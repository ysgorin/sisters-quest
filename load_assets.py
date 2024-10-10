import pygame
def load_assets():
    # Create assets dictionary
    assets = {}

    # Load intro screen assets
    assets['intro_background'] = pygame.image.load('assets/images/intro_background.png').convert()
    assets['play_button'] = pygame.image.load('assets/images/play_button.png').convert_alpha()
    assets['title_text'] = pygame.image.load('assets/images/title_text.png').convert_alpha()

    # return the loaded assets
    return assets