from random import randint
import numpy as np

class Game:
    x_dir = [0, 0, -1, 1]
    y_dir = [-1, 1, 0, 0]

    def __init__(self) -> None:
        self.map = np.zeros((15, 17))
        self.init_snake()
        self.new_apple()
        # 0 - up, 1 - down, 2 - left, 3 - right
        self.direction = []
        self.face = 3
        self.score = 0
    
    def init_snake(self):
        self.snake = [(2, 10), (3, 10), (4, 10)]
        for i in self.snake:
            x, y = i
            self.map[y][x] = 1
        self.head = self.snake[len(self.snake) - 1]
        # self.tail = self.snake[0]

    # create a new place for the apple
    def new_apple(self):
        while True:
            self.apple_pos = (randint(0, 16), randint(0, 14))
            x, y = self.apple_pos
            if not self.map[y][x]:
                break

    def change_direction(self, dir):
        self.direction.append(dir)
        self.face = dir

    def collision(self):
        x, y = self.head
        dir = self.direction[0]
        x += self.x_dir[dir]
        y += self.y_dir[dir]
        return x < 0 or 16 < x or y < 0 or 14 < y or self.map[y][x]

    def snake_move(self) -> bool:
        # add head
        x, y = self.head
        dir = self.direction.pop(0)
        x += self.x_dir[dir]
        y += self.y_dir[dir]

        if x < 0 or 16 < x or y < 0 or 14 < y or self.map[y][x]:
            # crashed into something (wall or snake)
            # end game
            print('Snake crashed into something')
        else:
            pos = (x, y)
            self.snake.append(pos)
            self.head = pos
            self.map[y][x] = 1
    
            # if it eats an apple
            if self.head == self.apple_pos:
                return True

            # remove tail
            x, y = self.snake.pop(0)
            self.map[y][x] = 0
            return False
            