import pygame 

pygame.init()
screen_width = 450
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Puzzle Bobble")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60) # Meaning FPS = 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()