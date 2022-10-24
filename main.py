import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

quiz_on = True
correct_guesses = 0

while quiz_on:

    answer_state = screen.textinput(title=f"{correct_guesses}/50 Guess the State", prompt="What's another state's name?").title()
    states = pandas.read_csv('50_states.csv')
    if answer_state in states.values:
        coor = states[states.state == answer_state]
        x_coor = coor.iloc[0, 1]
        y_coor = coor.iloc[0, 2]
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(x_coor, y_coor)
        state_name.write(answer_state)
        correct_guesses += 1



# Get coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
turtle.mainloop()
