import random

class Food:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.positions = [self.random_position() for _ in range(5)]

    def random_position(self):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        return (x, y)

    def refresh(self):
        self.positions = [self.random_position() for _ in range(5)]
