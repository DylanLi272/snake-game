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
                                    fill= '#4eb54c' if (x+y) % 2 == 0 else '#40943e', width=0)
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

# def animate_snake(canvas: Canvas, game: Game, count: int, direction: int):
#     canvas.delete('snake')
#     snake = game.snake
#     for s in snake:
#         x, y = s
#         # 0 - up, 1 - down, 2 - left, 3 - right
#         if direction == 0:
#             x_gap = 0
#             y_gap = count * -4
#         elif direction == 1:
#             x_gap = 0
#             y_gap = count * 4
#         elif direction == 2:
#             x_gap = count * -4
#             y_gap = 0
#         elif direction == 3:
#             x_gap = count * 4
#             y_gap = 0
#         canvas.create_rectangle(x*cell_size + x_gap, y*cell_size + y_gap, 
#                                 x*cell_size + x_gap + snake_size, y*cell_size + y_gap + snake_size, 
#                                 fill= '#0f66f2', width=0, tags='snake')

def draw_apple(canvas: Canvas, game: Game):
    x, y = game.apple_pos
    gap = (cell_size - apple_size) // 2
    canvas.delete('apple')
    canvas.create_rectangle(x*cell_size + gap, y*cell_size + gap, 
                            x*cell_size + gap + apple_size, y*cell_size + gap + apple_size, 
                            fill= '#e61515', width=0, tags='apple')

def update_snake(canvas: Canvas, game: Game):
    # collision check

    game.snake_move()
    
    # if it eats an apple
    if game.head == game.apple_pos:
        game.score += 1
        update_apple(canvas, game)
    
    draw_snake(canvas, game)

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

