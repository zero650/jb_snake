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
        self.obstacle_timer = pygame.time.get_ticks()

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
        for i in range(1, len(self.snake_body)):
            if self.snake_body[-1] == [self.snake_body[i][0], self.snake_body[i][1]]:
                return True

        return True

    def run(self):
        clock = pygame.time.Clock()
        running = True
        obstacles = []
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Add obstacle at random interval
            if self.obstacle_timer < pygame.time.get_ticks() - 3000:
                obstacles.append([random.randint(0, WIDTH - 20) // 20 * 20, random.randint(0, HEIGHT - 20) // 20 * 20])

            # Move snake
            new_head_pos = [self.snake_body[0][0] + 20, self.snake_body[0][1]]
            if not self.update_snake_pos():
                print(f"Game over! Final score: {self.score}")
                running = False

            # Clear screen and draw everything
            screen.fill(BLACK)

            # Draw obstacles
            for obstacle in obstacles:
                pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], 10, 10))

            # Update snake body
            self.snake_body.append(new_head_pos)
            if len(self.snake_body) > 3:
                self.snake_body.pop(0)

            # Draw snake body
            for part in self.snake_body:
                pygame.draw.rect(screen, WHITE, (part[0], part[1], 10, 10))

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    snake_game = SnakeGame()
    snake_game.run()