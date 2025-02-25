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
BLACK = (0, 0, 0)

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
        self.speed = 10
        self.apple_pos = [random.randint(0, WIDTH - 20) // 20 * 20,
                          random.randint(0, HEIGHT - 20) // 20 * 20]
        self.snake_body = [[WIDTH / 2, HEIGHT / 2], [WIDTH / 2 - 10, HEIGHT / 2], [WIDTH / 2 - 20, HEIGHT / 2]]
        self.score = 0
        self.direction_change_time = pygame.time.get_ticks()

    def update_snake_pos(self):
        current_head_x, current_head_y = self.snake_body[-1]
        if self.direction == 'RIGHT':
            new_head_pos = [current_head_x + 20, current_head_y]
        elif self.direction == 'LEFT':
            new_head_pos = [current_head_x - 20, current_head_y]
        elif self.direction == 'UP':
            new_head_pos = [current_head_x, current_head_y - 20]
        elif self.direction == 'DOWN':
            new_head_pos = [current_head_x, current_head_y + 20]

        # Boundary checking
        if (new_head_pos[0] < 0 or new_head_pos[0] >= WIDTH or
            new_head_pos[1] < 0 or new_head_pos[1] >= HEIGHT):
            return False

        # Collision detection with itself
        for body_part in self.snake_body[:-1]:
            if body_part == new_head_pos:
                return False

        # If no collision, update the snake's position
        self.snake_body.append(new_head_pos)
        if new_head_pos == self.apple_pos:
            self.score += 1
            self.speed = random.randint(10, 20)
            self.apple_pos = [random.randint(0, WIDTH - 20) // 20 * 20,
                              random.randint(0, HEIGHT - 20) // 20 * 20]
        else:
            if len(self.snake_body) > 1:
                self.snake_body.pop(0)

        return True

    def draw_snake(self):
        screen.fill(BLACK)
        for body_part in self.snake_body:
            pygame.draw.rect(screen, WHITE, (body_part[0], body_part[1], 10, 10))
        score_text = font.render(f'Score: {self.score}', True, WHITE)
        screen.blit(score_text, (10, 10))

    def handle_events(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.direction_change_time > 200:
            self.direction_change_time = current_time
            if self.direction == 'RIGHT':
                self.direction = 'UP'
            elif self.direction == 'LEFT':
                self.direction = 'DOWN'
            elif self.direction == 'UP':
                self.direction = 'LEFT'
            elif self.direction == 'DOWN':
                self.direction = 'RIGHT'

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update_snake_pos()
            if not self.update_snake_pos():
                print("Snake crashed.")
                break
            self.handle_events()
            self.draw_snake()
            clock.tick(self.speed)

if __name__ == "__main__":
    try:
        snake_game = SnakeGame()
        snake_game.run()
    except Exception as e:
        print(f"Error running game: {e}")