# functions used to control graphics and game

from tkinter import *
from game import *
from random import randint

cell_size = 40
apple_size = 20

def init_graphics(canvas: Canvas):
    for y in range(15):
        for x in range(17):
            canvas.create_rectangle(x*cell_size, y*cell_size, 
                                    x*cell_size + cell_size, y*cell_size + cell_size, 
                                    fill= '#23e826' if (x+y) % 2 == 0 else '#159e17', width=0)

def update_apple(canvas: Canvas, game: Game):
    x, y = game.new_apple()
    gap = (cell_size - apple_size) // 2
    canvas.delete('apple')
    canvas.create_rectangle(x*cell_size + gap, y*cell_size + gap, 
                            x*cell_size + gap + apple_size, y*cell_size + gap + apple_size, 
                            fill= '#e61515', width=0, tags='apple')
    

