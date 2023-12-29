import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
IMAGE = "blank_states_img.gif"

screen.addshape(IMAGE)
turtle.shape(IMAGE)

instruction = turtle.Turtle()
instruction.hideturtle()
instruction.penup()
instruction.goto(0, -300)
instruction.write("Write 'Exit' to quit the game at any time. Then click screen.", align="center", font=("Arial", 12, "normal"))


data = pd.read_csv("50_states.csv")
guessed_states = []
while len(guessed_states) < 50:
    guess = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    guess = str(guess).title()
    if guess == "Exit":
        break
    if guess in data.state.values:
        guessed_states.append(guess)
        t = turtle.Turtle() #make word
        t.hideturtle()
        t.penup() #go to location without trail
        state_location = data[data.state == guess]
        t.goto(int(state_location.x.iloc[0]), int(state_location.y.iloc[0]))
        t.write(guess)

if (len(guessed_states) == 50):
    message = "Congrats! You got guessed all 50 states!"
    win_message = turtle.Turtle()
    win_message.hideturtle()
    win_message.penup()
    win_message.goto(0, 250)
    win_message.write(message, align="center", font=("Arial", 24, "normal"))

# Generate a list of states that need to be studied
missed_states = pd.DataFrame([state for state in data.state if state not in guessed_states])
missed_states.to_csv("states_to_learn.csv")

screen.exitonclick()