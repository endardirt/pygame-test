import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 100
player_speed = 7

# Enemy
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = -enemy_size
enemy_speed = 6

# Font
font = pygame.font.SysFont(None, 40)

# Score
score = 0

running = True

while running:
    clock.tick(FPS)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player on screen
    player_x = max(0, min(WIDTH - player_size, player_x))

    # Move enemy
    enemy_y += enemy_speed

    # Respawn enemy
    if enemy_y > HEIGHT:
        enemy_y = -enemy_size
        enemy_x = random.randint(0, WIDTH - enemy_size)
        score += 1
        enemy_speed += 0.2

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

    if player_rect.colliderect(enemy_rect):
        running = False

    # Drawing
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)

    # Score text
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (20, 20))

    pygame.display.flip()

# Game over screen
screen.fill(WHITE)
game_over = font.render("Game Over!", True, RED)
final_score = font.render(f"Final Score: {score}", True, BLACK)

screen.blit(game_over, (WIDTH // 2 - 100, HEIGHT // 2 - 40))
screen.blit(final_score, (WIDTH // 2 - 120, HEIGHT // 2 + 10))

pygame.display.flip()

time.sleep(3)

pygame.quit()