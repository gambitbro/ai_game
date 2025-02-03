import pygame
from settings import Settings
from snake import Snake
from food import Food

class Game:
    """
    Game 클래스는 게임의 주요 로직을 관리합니다.

    속성:
        settings (Settings): 게임 설정 객체.
        screen (pygame.Surface): 게임 화면 Surface 객체.
        clock (pygame.time.Clock): 게임 클록 객체.
        running (bool): 게임 실행 여부.
        snake (Snake): 뱀 객체.
        food (Food): 음식 객체.
    """
    def __init__(self):
        """
        Game 클래스의 생성자. 게임의 초기 상태를 설정합니다.
        """
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.snake = Snake(self.settings.screen_width // 20, self.settings.screen_height // 20)
        self.food = Food(self.settings.screen_width // 20, self.settings.screen_height // 20)

    def run(self):
        """
        게임 루프를 실행합니다.
        """
        while self.running:
            self._check_events()
            self.snake.move()
            self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        """
        게임 이벤트를 처리합니다.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """
        키다운 이벤트를 처리합니다.

        매개변수:
            event (pygame.event.Event): 키다운 이벤트 객체.
        """
        if event.key == pygame.K_w:
            self.snake.change_direction('UP')
        elif event.key == pygame.K_a:
            self.snake.change_direction('LEFT')
        elif event.key == pygame.K_s:
            self.snake.change_direction('DOWN')
        elif event.key == pygame.K_d:
            self.snake.change_direction('RIGHT')

    def _check_collisions(self):
        """
        뱀의 충돌을 확인하고 처리합니다.
        """
        for food_position in self.food.positions:
            if self.snake.head_position() == food_position:
                self.snake.grow()
                self.food.refresh()
                break
        if self.snake.check_collision():
            self.running = False

    def _update_screen(self):
        """
        화면을 업데이트합니다.
        """
        self.screen.fill(self.settings.bg_color)
        self.snake.draw(self.screen)
        for food_position in self.food.positions:
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(food_position[0] * 20, food_position[1] * 20, 20, 20))
        pygame.display.flip()
