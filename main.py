import pygame

# Game initialization
pygame.init()
screen = pygame.display.set_mode((500,600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False


pygame.quit()
