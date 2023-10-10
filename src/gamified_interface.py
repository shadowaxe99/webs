```python
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
FPSCLOCK = pygame.time.Clock()

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the player
player = pygame.image.load('player.png')
player_rect = player.get_rect()

# Set up the game loop
while True:
    # Check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    # Draw the background
    DISPLAYSURF.fill(WHITE)

    # Draw the player
    DISPLAYSURF.blit(player, player_rect)

    # Update the display
    pygame.display.update()

    # Run the game at 60 frames per second
    FPSCLOCK.tick(FPS)
```