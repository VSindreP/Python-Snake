from tkinter import *
import random
WIDTH = 500
HEIGHT = 500
SPACE_SIZE = 20
SPEED = 200
SNAKE_SIZE = 2
SNAKE_COLOUR = "WHITE"
FOOD_COLOUR = "BLUE"
BACKGROUND_COLOUR = "BLACK"

direction_changed = False

#class for designing snake
class Snake: 

    def __init__(self):
        self.body_size = SNAKE_SIZE
        self.coordinates = []
        self.squares = []

        for i in range(0,SNAKE_SIZE):
            self.coordinates.append([0,0])
        
        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag = "snake")
            self.squares.append(square)
#Class for food
class Food:
    def __init__(self):
        x = random.randint(0, (WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOUR, tag = "food")

#Class for deciding the next turn
def next_turn(snake, food):
    global direction_changed
    direction_changed = False
    
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score

        score += 1

        label.config(text="Points:{}".format(score))

        canvas.delete("food")

        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    if check_collisions(snake):
        game_over()
    else: 
        window.after(SPEED, next_turn, snake, food)

#Class for changing direction of the snake
def change_direction(new_direction):
    global direction
    global direction_changed

    if direction_changed:
        return

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
            direction_changed = True

    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
            direction_changed = True

    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
            direction_changed = True

    elif new_direction == "down":
        if direction != "up":
            direction = new_direction
            direction_changed = True

#Class for checking if snake has crashed
def check_collisions(snake):
    x,y = snake.coordinates[0]

    if x < 0 or x >= WIDTH:
        return True
    elif y < 0 or y >= HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

#Class for restarting game
def restart_game():
    global score, direction, snake, food
    score = 0
    direction = "down"
    label.config(text = "Points:{}".format(score))
    canvas.delete(ALL)
    snake = Snake()
    food = Food()
    next_turn(snake, food)
    btn_restart.place_forget()
    btn_quit.place_forget()

#Class for when the snake has crashed
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,
                       canvas.winfo_height()/2,
                       font = ("consolas", 70),
                       text = "GAME OVER", fill = "red",
                       tag = "gameover")
    btn_restart.place(relx = 0.4, rely = 0.8, anchor = "se")
    btn_quit.place(relx = 0.6, rely = 0.8, anchor = "sw")

window = Tk()
window.title("Welcome to Snake")

score = 0
direction = "down"

label = Label(window, text= "Points:{}".format(score), font=("consolas", 20))
label.pack()

canvas = Canvas(window, bg = BACKGROUND_COLOUR, width = WIDTH, height = HEIGHT)
canvas.pack()

btn_restart = Button(window, text = "Restart", font = ("consolas", 20), command = restart_game)
btn_quit = Button (window, text = "Quit", font = ("consolas", 20), command = window.destroy)
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake, food)


window.mainloop()

