import random

class Food:
    """
    Food 클래스는 게임 내에서 뱀이 먹을 수 있는 음식의 위치를 관리합니다.

    속성:
        width (int): 음식이 생성될 수 있는 가로 범위.
        height (int): 음식이 생성될 수 있는 세로 범위.
        positions (list): 음식의 위치를 저장하는 리스트.
    """
    def __init__(self, width, height):
        """
        Food 클래스의 생성자. 음식의 위치를 초기화합니다.

        매개변수:
            width (int): 음식이 생성될 수 있는 가로 범위.
            height (int): 음식이 생성될 수 있는 세로 범위.
        """
        self.width = width
        self.height = height
        self.positions = [self.random_position() for _ in range(5)]

    def random_position(self):
        """
        음식의 랜덤한 위치를 생성합니다.

        반환값:
            tuple: 음식의 랜덤한 위치 (x, y).
        """
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        return (x, y)

    def refresh(self):
        """
        음식의 위치를 새로 고칩니다.
        """
        self.positions = [self.random_position() for _ in range(5)]
