import pygame
from src.settings import Settings
from src.snake.snake import Snake
from src.snake.food import Food

class Game:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.snake = Snake(self.settings.screen_width // 20, self.settings.screen_height // 20)
        self.food = Food(self.settings.screen_width // 20, self.settings.screen_height // 20)

    def run(self):
        while self.running:
            self._check_events()
            self.snake.move()
            self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_w:
            self.snake.change_direction('UP')
        elif event.key == pygame.K_a:
            self.snake.change_direction('LEFT')
        elif event.key == pygame.K_s:
            self.snake.change_direction('DOWN')
        elif event.key == pygame.K_d:
            self.snake.change_direction('RIGHT')

    def _check_collisions(self):
        for food_position in self.food.positions:
            if self.snake.head_position() == food_position:
                self.snake.grow()
                self.food.refresh()
                break
        if self.snake.check_collision():
            self.running = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.snake.draw(self.screen)
        for food_position in self.food.positions:
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(food_position[0] * 20, food_position[1] * 20, 20, 20))
        pygame.display.flip()
