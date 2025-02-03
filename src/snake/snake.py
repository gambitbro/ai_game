import pygame

class Snake:
    """
    Snake 클래스는 게임 내에서 뱀의 상태와 동작을 관리합니다.

    속성:
        grid_width (int): 그리드의 가로 크기.
        grid_height (int): 그리드의 세로 크기.
        body (list): 뱀의 몸을 구성하는 좌표 리스트.
        direction (str): 뱀의 현재 이동 방향.
        growing (bool): 뱀이 성장 중인지 여부.
    """
    def __init__(self, grid_width, grid_height):
        """
        Snake 클래스의 생성자. 뱀의 초기 상태를 설정합니다.

        매개변수:
            grid_width (int): 그리드의 가로 크기.
            grid_height (int): 그리드의 세로 크기.
        """
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.body = [(grid_width // 2, grid_height // 2)]
        self.direction = 'UP'
        self.growing = False

    def move(self):
        """
        뱀을 현재 방향으로 이동시킵니다.
        """
        head_x, head_y = self.body[0]
        if self.direction == 'UP':
            head_y -= 1
        elif self.direction == 'DOWN':
            head_y += 1
        elif self.direction == 'LEFT':
            head_x -= 1
        elif self.direction == 'RIGHT':
            head_x += 1

        new_head = (head_x, head_y)
        if self.growing:
            self.body.insert(0, new_head)
            self.growing = False
        else:
            self.body = [new_head] + self.body[:-1]

    def change_direction(self, direction):
        """
        뱀의 이동 방향을 변경합니다.

        매개변수:
            direction (str): 변경할 방향 ('UP', 'DOWN', 'LEFT', 'RIGHT').
        """
        if direction == 'UP' and self.direction != 'DOWN':
            self.direction = direction
        elif direction == 'DOWN' and self.direction != 'UP':
            self.direction = direction
        elif direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = direction
        elif direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = direction

    def grow(self):
        """
        뱀이 성장하도록 설정합니다.
        """
        self.growing = True

    def head_position(self):
        """
        뱀의 머리 위치를 반환합니다.

        반환값:
            tuple: 뱀의 머리 위치 (x, y).
        """
        return self.body[0]

    def check_collision(self):
        """
        뱀이 충돌했는지 확인합니다.

        반환값:
            bool: 충돌 시 True, 그렇지 않으면 False.
        """
        head = self.body[0]
        return (
            head in self.body[1:] or
            head[0] < 0 or head[0] >= self.grid_width or
            head[1] < 0 or head[1] >= self.grid_height
        )

    def draw(self, screen):
        """
        화면에 뱀을 그립니다.

        매개변수:
            screen (pygame.Surface): 게임 화면 Surface 객체.
        """
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment[0] * 20, segment[1] * 20, 20, 20))
