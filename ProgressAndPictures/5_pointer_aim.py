# Setting up Pointer aim (Using Arrow Keys)

import os
import pygame 

# Creating Bubble Class
class Bubble(pygame.sprite.Sprite):
    def __init__(self, image, color, position):
        super().__init__()
        self.image = image
        self.color = color
        self.rect = image.get_rect(center=position)

# Creating Pointer Class
class Pointer(pygame.sprite.Sprite):
    def __init__(self, image, position, angle):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)
        self.angle = angle
        self.original_image = image
        self.position = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Rotation
    def rotate(self, angle):
        self.angle += angle

        if self.angle < 10:
            self.angle = 10
        elif self.angle > 170:
            self.angle = 170
        
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.position)

# Creating Map
def setup():
    global map 
    map = [
        list("RRBBYYGG"),
        list("RRPPOOG/"), #  Bubble cannot be located on /
        list("GGYYOOBB"),
        list("GGYYRRB/"), 
        list("........"), # . means empty space
        list("......./"),
        list("........"),
        list("......./"),
        list("........"),
        list("......./"),
        list("........")
    ]

    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if col in [".", "/"]:
                continue
            position = get_bubble_position(row_idx, col_idx)
            image = get_bubble_image(col)
            bubble_group.add(Bubble(image, col, position))

def get_bubble_position(row_idx, col_idx):
    pos_x = col_idx * CELL_SIZE + (BUBBLE_WIDTH // 2)
    pos_y = row_idx * CELL_SIZE + (BUBBLE_HEIGHT // 2)
    if row_idx % 2 == 1:
        pos_x += CELL_SIZE // 2
    return pos_x, pos_y

def get_bubble_image(color):
    if color == "R":
        return bubble_images[0]
    elif color == "O":
        return bubble_images[1]
    elif color == "Y":
        return bubble_images[2]
    elif color == "G":
        return bubble_images[3]
    elif color == "B":
        return bubble_images[4]
    elif color == "P":
        return bubble_images[5]
    else:
        return bubble_images[-1] 


pygame.init()
screen_width = 450
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Puzzle Bobble")
clock = pygame.time.Clock()

# Importing background image
current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "background.png"))

# Importing bubble images
bubble_images = [
    pygame.image.load(os.path.join(current_path, "red.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "orange.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "yellow.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "green.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "blue.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "purple.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "black.png")).convert_alpha()
]

# Imporint pointer image
pointer_image = pygame.image.load(os.path.join(current_path, "pointer.png"))
pointer = Pointer(pointer_image, (screen_width // 2, 650), 90)

# Game related variables
CELL_SIZE = 56
BUBBLE_WIDTH = 56
BUBBLE_HEIGHT = 62

# Arrow related variables
to_angle_left = 0 
to_angle_right = 0
angle_speed = 1.5 

map = [] # Map
bubble_group = pygame.sprite.Group()
setup()

running = True
while running:
    clock.tick(60) # Meaning FPS = 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_angle_left += angle_speed
            elif event.key == pygame.K_RIGHT:
                to_angle_right -= angle_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_angle_left = 0
            elif event.key == pygame.K_RIGHT:
                to_angle_right = 0

    screen.blit(background, (0, 0))
    bubble_group.draw(screen)
    pointer.rotate(to_angle_left + to_angle_right)
    pointer.draw(screen)
    pygame.display.update()

pygame.quit()