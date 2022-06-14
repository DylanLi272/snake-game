from tkinter import *
from game import Game
import controls

print('Hello World')

window = Tk()
window.title('Snake Game')
canvas = Canvas(master=window, height=600, width=680)
canvas.pack()
controls.init_graphics(canvas)

game = Game()


window.bind('<Return>', lambda event: controls.update_apple(canvas, game))


window.mainloop()