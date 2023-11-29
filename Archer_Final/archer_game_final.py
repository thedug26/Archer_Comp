import pygame
from adventurer import Adventurer
from target import Target
from archer_game_constants import *
from archer_background import *

# Set the width and height of the game window
#WIDTH = 1200
#HEIGHT = 600

pygame.init()
# create clock
clock = pygame.time.Clock()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# make arrows group
arrows = pygame.sprite.Group()

#create font
#custom_font = pygame.font.Font("../Archer_Final/assets/fonts/Kenney Future.ttf", 48)
#text = custom_font.render("Archer", True, (255, 0, 0))

# Create an adventurer at left of the screen
my_adventurer = Adventurer(4*TILE_SIZE, SCREEN_HEIGHT - 100, arrows, screen)

# Create a target
my_target = Target(SCREEN_WIDTH//2 + 200, SCREEN_HEIGHT - TILE_SIZE * 5 -5, screen)

# Set the running flag to True
running = True

background=screen.copy()
draw_background(background)

# Main game loop
while running:
    # Check for events
    for event in pygame.event.get():
        # If the user closes the window, set running to False
        if event.type == pygame.QUIT:
            running = False

    # Set the game's FPS
    clock.tick(120)

    screen.fill('black')

    screen.blit(background, (0, 0))
    # Update the adventurer & arrows
    my_adventurer.update()
    arrows.update()

    # Draw the adventurer, arrows, & target
    [b.draw(my_target, screen) for b in arrows]
    my_adventurer.draw()
    my_target.draw()
    background = screen.copy()
    draw_background(background)
    # Update the display
    pygame.display.flip()

pygame.quit()
