import pygame

# how to display a window?
width, height = 300, 500
background_colour = (255,255,255)
screen = pygame.display.set_mode((width, height)) #dlaczego tu sa dwa nawiasy lol
screen.fill(background_colour)
pygame.display.flip()
pygame.display.set_caption('moje okienko')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
