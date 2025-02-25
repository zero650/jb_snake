import pygame
import sys
import time
import random

# Pygame Initialization
pygame.init()

# Screen size and colors
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Snake properties
snake_length = 10
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50], [50, 50], [40, 50]]

# Food properties
food_pos = [random.randrange(1, (screen_width // 10)) * 10, random.randrange(1, (screen_height // 10)) * 10]

# Direction variables
direction = "right"

# Score variable
score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            if event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            if event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"

    # Move snake
    if direction == "up":
        new_head_pos = [snake_pos[0], snake_pos[1] - 10]
    elif direction == "down":
        new_head_pos = [snake_pos[0], snake_pos[1] + 10]
    elif direction == "left":
        new_head_pos = [snake_pos[0] - 10, snake_pos[1]]
    elif direction == "right":
        new_head_pos = [snake_pos[0] + 10, snake_pos[1]]

    # Check for collision with food
    if new_head_pos == food_pos:
        score += 1
        food_pos = [random.randrange(1, (screen_width // 10)) * 10, random.randrange(1, (screen_height // 10)) * 10]
    else:
        snake_body.insert(0, list(new_head_pos))
        if new_head_pos in snake_body[1:]:
            game_over_screen = True
            break

    # Check for collision with wall
    if (new_head_pos[0] < 0 or new_head_pos[0] >= screen_width or 
        new_head_pos[1] < 0 or new_head_pos[1] >= screen_height):
        game_over_screen = True
        break

    # Update snake position
    snake_pos = list(new_head_pos)

    # Draw everything
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, white, [pos[0], pos[1], 10, 10])
    if game_over_screen:
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, red)
        screen.blit(text, [screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2])
        pygame.display.update()
        time.sleep(2)
    else:
        pygame.draw.rect(screen, red, [food_pos[0], food_pos[1], 10, 10])

    # Draw score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, white)
    screen.blit(text, [10, 10])

    # Update display
    pygame.display.update()

    # Cap framerate at 60 FPS
    time.sleep(0.1)