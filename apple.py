from graphics import *
from button import Button
import random as r

#genrating a random position for fruit (I know there was no need for creating a separate function when i am using show function)
def apple_generator(w, h) :
    return Point(int(r.randint(0, w)), int(r.randint(0, h)))

def show(w,h, grd, snakeBodyPos) :
    breaker = False
    
    while not breaker :
        appleL = apple_generator(int(w)-2, int(h)-2)
        for i in range(0, len(snakeBodyPos) - 1) :
            if appleL.x != snakeBodyPos[i].x or appleL.y != snakeBodyPos[i].y :
                breaker = True

    print(appleL)
    grd[int(appleL.x)][int(appleL.y)].setFill("red")
    return appleL

def remove(appleL, color, grd) :
    grd[int(appleL.x)][int(appleL.y)].setFill(color)
