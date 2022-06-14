from tkinter import *
from game import Game
import controls
import time

print('Hello World')

window = Tk()
window.title('Snake Game')
canvas = Canvas(master=window, height=600, width=680)
canvas.pack()
game = Game()

controls.init_graphics(canvas, game)


window.bind('<Return>', lambda event: controls.update_apple(canvas, game))
# 0 - up, 1 - down, 2 - left, 3 - right
window.bind('<Up>', lambda event: controls.change_dir(canvas, game, 0))
window.bind('<Down>', lambda event: controls.change_dir(canvas, game, 1))
window.bind('<Left>', lambda event: controls.change_dir(canvas, game, 2))
window.bind('<Right>', lambda event: controls.change_dir(canvas, game, 3))
# window.bind('<Key>', lambda event: print(event.keysym))

speed = 300

def update_snake():
    if len(game.direction) == 0:
        game.direction.append(game.face)
    controls.update_snake(canvas, game)
    window.after(speed, update_snake)

window.after(speed, update_snake)

window.mainloop()