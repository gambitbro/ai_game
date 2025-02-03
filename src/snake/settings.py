class Settings:
    """
    Settings 클래스는 게임 설정을 관리합니다.

    속성:
        screen_width (int): 화면의 가로 크기.
        screen_height (int): 화면의 세로 크기.
        bg_color (tuple): 배경 색상 (RGB).
        fps (int): 초당 프레임 수.
    """
    def __init__(self):
        """
        Settings 클래스의 생성자. 기본 설정을 초기화합니다.
        """
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.fps = 30
