import pygame
from game import Game

def main():
    """
    게임의 메인 함수. 게임을 초기화하고 실행합니다.
    """
    pygame.init()
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
