# NOTE : To run this program you need graphics.py module otherwise it will shoe error

import UI as ui
import apple as fruit
from graphics import *
from button import Button
from snake import Snake

def snake_game() :
    w = 0   # width of the ground(declared in line 29)
    h = 0   # heigth of the ground(declared in line 28)
    r = 20  # ratio of the boxes of ground
    interval = 0.5 # time interval for snake movement
    shiftHori = 50 # shifting the ground horizontly
    shiftVert = 100 # shifting the ground Vertically
    snk_color = "yellow" # snake colour(should i have to write it)
    grd_color = "green" # ground colour


    win = GraphWin("Snake Game by Tejas Varshney", 600, 600) # making a window
    grd = [[]] # ground array

    # declaring grd array
    for i in range (0, int((win.getWidth() - shiftHori)/r)) :
        for j in range (0, int((win.getHeight() - shiftVert)/r)) :
            grd [i].append(Rectangle(Point((i*r) + 25, (j*r) + 25), Point((i+1)*r + 25, (j+1)*r + 25)))
            grd [i][j].setFill(grd_color)
            grd [i][j].draw(win)
        grd.append([])

    # read comment in line 8 and 9
    h = len(grd[0])
    w = len(grd)

    # making a snake object from Snake class
    snake = Snake(snk_color, grd_color, Point(int(w/2), int(h/2)), grd, Point(0,0), win)
    # storing the fruit position
    applePos = fruit.show(w, h, grd, snake.getBodyPos())
    # sending the apple position to snake class
    snake.set_applePos(applePos)

    # making a start and exit button(Don't think that button function was pre installed, I have make it :( )
    button1 = Button("Start", win.getWidth()/3, grd[int(w/2)][int(h-1)].getP2().y + 10, win.getWidth()/1.5, grd[int(w/2)][int(h-1)].getP2().y + 60, color_rgb(0, 255, 0), win)
    button1.show()

    # making a score variable
    score = 0
    # score text varable
    score_txt = Text(Point(win.getWidth()/2, 10), "Score : " +  str(score))
    score_txt.draw(win)

    # Now the game start when the start button click
    while True :
        try :
            if button1.isClicked(win.getMouse()) :
                # when button is clicked, then the button changes to exit button(Clever idea :) )
                button1.setText("EXIT")
                button1.setColour("red")

                # I will not tell what is happening here. Figure it out by yourself
                if ui.game(snake, score, score_txt, "Up", button1, interval, applePos, grd, grd_color, w, h, win):
                    win.close()
                    return True
                else :
                    win.close()
                    return False

        except GraphicsError:
            print("Game is closed")
            return False

# It is the starting of our program
while True :
    if not snake_game() :
        break
