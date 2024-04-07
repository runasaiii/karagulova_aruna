import pygame
import random

# Initialize
pygame.init()

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arkanoid")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Sounds
brick_hit_sound = pygame.mixer.Sound("catch.wav")

# Game variables
ball_speed = [5, 3]
paddle_speed = 0
ball_rect = pygame.Rect(400, 300, 20, 20)
paddle_rect = pygame.Rect(350, 580, 100, 10)
bricks = []
unbreakable_bricks = []
bonus_bricks = []
speed_increment = 0.1  # Amount to increase ball speed per second
time_elapsed = 0  # Track time elapsed
clock = pygame.time.Clock()

def draw_menu(menu_text):
    # This function draws the main menu or pause menu
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    text = font.render(menu_text, True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

def draw_settings_menu():
    # This function draws the settings menu
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    text = font.render("Settings Menu (Work in Progress)", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

# Generating bricks
for i in range(5):
    for j in range(3):
        brick = pygame.Rect(i * 150 + 50, j * 40 + 40, 110, 15)
        bricks.append(brick)
        if random.randint(1, 5) == 1:
            unbreakable_bricks.append(brick)
        elif random.randint(1, 5) == 1:
            bonus_bricks.append(brick)

# Main menu loop
menu_running = True
while menu_running:
    draw_menu("Press SPACE to start the game")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            menu_running = False  # Start the game

# Game loop
running = True
paused = False
settings_menu = False
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if paused or settings_menu:
                    paused = False
                    settings_menu = False
                    draw_menu("Press SPACE to resume")
                else:
                    paused = True
                    draw_menu("Game Paused")
            elif event.key == pygame.K_SPACE:
                if paused:
                    paused = False
                    draw_menu("Press SPACE to resume")
                elif settings_menu:
                    settings_menu = False
                    draw_menu("Press ESC to pause")
            elif event.key == pygame.K_s:
                settings_menu = True
                draw_settings_menu()
            elif event.key == pygame.K_LEFT:
                paddle_speed = -7
            elif event.key == pygame.K_RIGHT:
                paddle_speed = 7
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                paddle_speed = 0

    if not (paused or settings_menu):
        # Move paddle
        paddle_rect.x += paddle_speed
        if paddle_rect.left < 0:
            paddle_rect.left = 0
        elif paddle_rect.right > SCREEN_WIDTH:
            paddle_rect.right = SCREEN_WIDTH

        # Move ball
        ball_rect = ball_rect.move(ball_speed)
        if ball_rect.left < 0 or ball_rect.right > SCREEN_WIDTH:
            ball_speed[0] = -ball_speed[0]
        if ball_rect.top < 0:
            ball_speed[1] = -ball_speed[1]
        if ball_rect.colliderect(paddle_rect):
            ball_speed[1] = -ball_speed[1]

        # Check collision with bricks
        for brick in bricks[:]:
            if ball_rect.colliderect(brick):
                if brick in unbreakable_bricks:
                    ball_speed[1] = -ball_speed[1]
                else:
                    bricks.remove(brick)
                    ball_speed[1] = -ball_speed[1]
                    brick_hit_sound.play()

        # Speed increment every second
        time_elapsed += clock.tick() / 1000  # Time since the last frame in seconds
        if time_elapsed >= 1:
            ball_speed[0] *= (1 + speed_increment)
            ball_speed[1] *= (1 + speed_increment)
            time_elapsed = 0

        # Check collision with bonus bricks
        for brick in bonus_bricks[:]:
            if ball_rect.colliderect(brick):
                bonus_bricks.remove(brick)
                brick_hit_sound.play()

        # Draw paddle, ball, and bricks
        pygame.draw.rect(screen, BLUE, paddle_rect)
        pygame.draw.ellipse(screen, WHITE, ball_rect)
        for brick in bricks:
            pygame.draw.rect(screen, WHITE, brick)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
