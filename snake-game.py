from tkinter import *
from game import Game
import controls
import time

print('Hello World')

game = Game()

window = Tk()
window.title('Snake Game')
score_lbl = Label(master=window, text='Score: ' + str(game.score), font=('Helvetica', 30))
score_lbl.pack()
canvas = Canvas(master=window, height=600, width=680)
canvas.pack()

controls.init_graphics(canvas, game)


# 0 - up, 1 - down, 2 - left, 3 - right
window.bind('<Up>', lambda event: controls.change_dir(canvas, game, 0))
window.bind('<Down>', lambda event: controls.change_dir(canvas, game, 1))
window.bind('<Left>', lambda event: controls.change_dir(canvas, game, 2))
window.bind('<Right>', lambda event: controls.change_dir(canvas, game, 3))
# window.bind('<Key>', lambda event: print(event.keysym))

speed = 250

def update_snake():
    if len(game.direction) == 0:
        game.direction.append(game.face)
    if not controls.update_snake(canvas, game):
        # if update_snake returns False, end game
        canvas.create_text(340, 300, text='Game Over', font=('Helvetica', 60))
        return
    score_lbl.config(text='Score: ' + str(game.score))
    window.after(speed, update_snake)

def start_game(event):
    canvas.delete('start_message')
    update_snake()


canvas.create_text(340, 300, text='Press <Enter>\nto start', font=('Helvetica', 60), tags='start_message', justify=CENTER)

window.bind('<Return>', start_game)
# window.after(speed, update_snake)

window.mainloop()