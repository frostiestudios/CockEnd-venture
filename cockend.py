import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants for the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("The Chronicles of Cock End")


# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (100, WINDOW_HEIGHT / 2)
        self.speed_y = 0

    def update(self):
        # Move the player up or down based on key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.speed_y = -5
        elif keys[pygame.K_DOWN]:
            self.speed_y = 5
        else:
            self.speed_y = 0
        self.rect.y += self.speed_y
        # Keep the player within the screen boundaries
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT


# Define the obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, random.randint(50, 150)))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = -5

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right < 0:
            self.kill()


# Create sprite groups for the player and obstacles
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Create the player and add it to the sprite group
player = Player()
all_sprites.add(player)

# Set up the game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn new obstacles
    if random.randint(0, 100) < 10:
        obstacle = Obstacle(WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT))
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    # Update all sprites
    all_sprites.update()

    # Check for collisions between the player and obstacles
    if pygame.sprite.spritecollide(player, obstacles, False):
        running = False

    # Draw everything to the screen
    window.fill((0, 0, 0))
    all_sprites.draw(window)
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

# Clean up and exit
pygame.quit()
