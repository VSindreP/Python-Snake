from tkinter import *
from tkinter import ttk

def startNewGame():
    print("Starting new game")

window = Tk()
window.title("Welcome to Snake")
window.geometry("250x250")

#window.grid_columnconfigure(0, weight = 1)

lbl_welcome = Label(window, text="Welcome To My Snake Game!")
lbl_welcome.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = NSEW)

btn_start_new_game = Button(window, text = "Start", width = 30, command= startNewGame)
btn_start_new_game.grid(row = 1, column = 0, padx = 15, pady = 15, sticky = NSEW)

btn_quit = Button(window, text = "Quit", width = 30,command = window.destroy)
btn_quit.grid(row = 2, column = 0, padx = 15, pady = 15, sticky = NSEW)

window.mainloop()

