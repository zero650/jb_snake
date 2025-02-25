import pygame
import sys
import random

# Initialize Pygame
try:
    pygame.init()
except Exception as e:
    print(f"Error initializing Pygame: {e}")
    sys.exit(1)

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
try:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
except Exception as e:
    print(f"Error setting up display: {e}")
    sys.exit(1)

# Set up the font for the score
font = pygame.font.Font(None, 36)

class SnakeGame:
    def __init__(self):
        self.direction = 'RIGHT'
        self.speed = 20
        self.apple_pos = [random.randint(0, WIDTH - 20) // 20 * 20,
                          random.randint(0, HEIGHT - 20) // 20 * 20]

    def update_snake_pos(self):
        head_x, head_y = self.snake_pos
        if self.direction == 'RIGHT':
            new_head_pos = [head_x + 20, head_y]
        elif self.direction == 'LEFT':
            new_head_pos = [head_x - 20, head_y]
        elif self.direction == 'UP':
            new_head_pos = [head_x, head_y - 20]
        elif self.direction == 'DOWN':
            new_head_pos = [head_x, head_y + 20]

        # Boundary checking
        if (new_head_pos[0] < 0) or (new_head_pos[0] >= WIDTH) or (new_head_pos[1] < 0) or (new_head_pos[1] >= HEIGHT):
            return False

        # Collision detection with itself
        for body_part in self.snake_body[:-1]:
            if body_part == new_head_pos:
                return False

        # If no collision, update the snake's position
        self.snake_body.insert(0, new_head_pos)
        if new_head_pos == self.apple_pos:
            self.score += 1
            self.speed = 20
            self.apple_pos = [random.randint(0, WIDTH - 20) // 20 * 20,
                              random.randint(0, HEIGHT - 20) // 20 * 20]

        return True

    def draw_snake(self):
        for body_part in self.snake_body:
            pygame.draw.rect(screen, WHITE, (body_part[0], body_part[1], 10, 10))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                    self.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                    self.direction = 'RIGHT'
                elif event.key == pygame.K_UP and self.direction != 'DOWN':
                    self.direction = 'UP'
                elif event.key == pygame.K_DOWN and self.direction != 'UP':
                    self.direction = 'DOWN'

    def run(self):
        while True:
            screen.fill((0, 0, 0))
            self.update_snake_pos()
            if not self.update_snake_pos():
                print("Snake crashed.")
                break
            self.draw_snake()

            pygame.display.flip()
            self.handle_events()
            clock.tick(60)

if __name__ == "__main__":
    try:
        snake_game = SnakeGame()
        snake_game.run()
    except Exception as e:
        print(f"Error running game: {e}")