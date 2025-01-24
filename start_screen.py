import pygame

def draw_start_screen(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 74)
    text = font.render("Snake Game", True, (255, 255, 255))
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - 50))
    
    font = pygame.font.Font(None, 36)
    text = font.render("Press Enter to Start", True, (255, 255, 255))
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2))
    pygame.display.flip()

def handle_start_screen_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return True
    return False
