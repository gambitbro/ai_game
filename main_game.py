import pygame
from start_screen import draw_start_screen, handle_start_screen_events
from game import Game

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
game_started = False
game = Game()
snake = game.snake

def start_game():
    global game_started
    game_started = True

def game_loop():
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        snake.change_direction('UP')
                    elif event.key == pygame.K_a:
                        snake.change_direction('LEFT')
                    elif event.key == pygame.K_s:
                        snake.change_direction('DOWN')
                    elif event.key == pygame.K_d:
                        snake.change_direction('RIGHT')

            snake.move()
            game._check_collisions()
            game._update_screen()

        pygame.display.flip()
        clock.tick(60)

game_loop()
