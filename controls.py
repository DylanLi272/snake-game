# functions used to control graphics and game

from tkinter import *
from game import *
from random import randint

cell_size = 40
apple_size = 20
snake_size = 40

def init_graphics(canvas: Canvas, game: Game):
    for y in range(15):
        for x in range(17):
            canvas.create_rectangle(x*cell_size, y*cell_size, 
                                    x*cell_size + cell_size, y*cell_size + cell_size, 
                                    fill= '#4eb54c' if (x+y) % 2 == 0 else '#44a142', width=0)
    draw_snake(canvas, game)
    draw_apple(canvas, game)

def draw_snake(canvas: Canvas, game: Game):
    canvas.delete('snake')
    snake = game.snake
    for s in snake:
        x, y = s
        gap = (cell_size - snake_size) // 2
        canvas.create_rectangle(x*cell_size + gap, y*cell_size + gap, 
                                x*cell_size + gap + snake_size, y*cell_size + gap + snake_size, 
                                fill= '#0f66f2', width=0, tags='snake')

def draw_apple(canvas: Canvas, game: Game):
    x, y = game.apple_pos
    gap = (cell_size - apple_size) // 2
    canvas.delete('apple')
    canvas.create_rectangle(x*cell_size + gap, y*cell_size + gap, 
                            x*cell_size + gap + apple_size, y*cell_size + gap + apple_size, 
                            fill= '#e61515', width=0, tags='apple')

def update_snake(canvas: Canvas, game: Game) -> bool:
    # collision check
    if game.collision():
        return False

    # if it eats an apple
    if game.snake_move():
        game.score += 1
        update_apple(canvas, game)
    
    draw_snake(canvas, game)

    return True

def update_apple(canvas: Canvas, game: Game):
    game.new_apple()
    draw_apple(canvas, game)

def change_dir(canvas: Canvas, game: Game, direction: int):
    if direction // 2 == game.face // 2:
        return
    game.change_direction(direction)



# use for debugging
def move(canvas: Canvas, game: Game, direction: int):
    game.change_direction(direction)
    game.snake_move()
    draw_snake(canvas, game)

