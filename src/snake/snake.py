import pygame

class Snake:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.body = [(grid_width // 2, grid_height // 2)]
        self.direction = 'UP'
        self.growing = False

    def move(self):
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
        if direction == 'UP' and self.direction != 'DOWN':
            self.direction = direction
        elif direction == 'DOWN' and self.direction != 'UP':
            self.direction = direction
        elif direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = direction
        elif direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = direction

    def grow(self):
        self.growing = True

    def head_position(self):
        return self.body[0]

    def check_collision(self):
        head = self.body[0]
        return (
            head in self.body[1:] or
            head[0] < 0 or head[0] >= self.grid_width or
            head[1] < 0 or head[1] >= self.grid_height
        )

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment[0] * 20, segment[1] * 20, 20, 20))
