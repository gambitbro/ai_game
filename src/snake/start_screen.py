import pygame

def draw_start_screen(screen):
    """
    시작 화면을 그립니다.

    매개변수:
        screen (pygame.Surface): 게임 화면 Surface 객체.
    """
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 74)
    text = font.render("Snake Game", True, (255, 255, 255))
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - 50))
    
    font = pygame.font.Font(None, 36)
    text = font.render("Press Enter to Start", True, (255, 255, 255))
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2))
    pygame.display.flip()

def handle_start_screen_events():
    """
    시작 화면에서 이벤트를 처리합니다.

    반환값:
        bool: 게임이 시작되면 True, 그렇지 않으면 False.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return True
    return False
