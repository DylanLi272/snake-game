from random import randint

class Game:
    def __init__(self) -> None:
        self.map = [[False * 17] * 15]
        self.apple_pos = (randint(0, 16), randint(0, 14))
        self.snake = []
        # head of snake
        # tail of snake
        pass
    
    # create a new place for the apple
    def new_apple(self):
        while True:
            self.apple_pos = (randint(0, 16), randint(0, 14))
            x, y = self.apple_pos
            if not self.map[y][x]:
                break
        print(self.apple_pos)
        return self.apple_pos

    
