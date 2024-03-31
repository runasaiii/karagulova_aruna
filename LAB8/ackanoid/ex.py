import pygame
import random


WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BALL_RADIUS = 10
BALL_SPEED_INCREMENT = 0.2  # Increment to ball speed per frame
PADDLE_SHRINK_INCREMENT = 0.1  # Decrease in paddle width per frame

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")

# sound effect
brick_hit_sound = pygame.mixer.Sound("catch.wav")

# or controlling the frame rate
clock = pygame.time.Clock()

# Classes for paddle, ball, and bricks
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 8

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(WIDTH, self.rect.right)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2))
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, BLACK, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = 5
        self.speed_y = 5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y
        if self.rect.bottom >= HEIGHT:
            # Reset ball position if it goes below the screen
            self.rect.center = (WIDTH // 2, HEIGHT // 2)
            self.speed_x = 5
            self.speed_y = 5

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Function to create bricks
def create_bricks():
    bricks = pygame.sprite.Group()
    for row in range(5):
        for col in range(10):
            brick = Brick(col * BRICK_WIDTH + 80, row * BRICK_HEIGHT + 60)
            bricks.add(brick)
    return bricks

# Function to handle ball collision with bricks
def handle_brick_collision(ball, bricks):
    brick_collisions = pygame.sprite.spritecollide(ball, bricks, True)
    for brick in brick_collisions:
        ball.speed_y = -ball.speed_y
        brick_hit_sound.play()

# Function to handle paddle collision with ball
def handle_paddle_collision(ball, paddle):
    if pygame.sprite.collide_rect(ball, paddle):
        ball.speed_y = -ball.speed_y

# Create sprites groups
all_sprites = pygame.sprite.Group()
bricks = create_bricks()
all_sprites.add(bricks)

# Create paddle and ball instances
paddle = Paddle()
ball = Ball()
all_sprites.add(paddle, ball)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Handle collisions
    handle_brick_collision(ball, bricks)
    handle_paddle_collision(ball, paddle)

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
