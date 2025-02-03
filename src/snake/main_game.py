import pygame
from src.snake.start_screen import draw_start_screen, handle_start_screen_events

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
game_started = False

def start_game():
    """
    게임을 시작합니다.
    """
    # ...existing code...

def game_loop():
    """
    게임 루프를 실행합니다.
    """
    global game_started
    while True:
        if not game_started:
            game_started = handle_start_screen_events()
            draw_start_screen(screen)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                # ...existing code...

            # ...existing code...

        pygame.display.flip()
        clock.tick(60)

game_loop()
