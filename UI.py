import apple
import time as t
from button import Button
from graphics import *

# Making a window to show Game Over msg
def show_screen(msg, score_txt) :
    win = GraphWin("msg", 300, 120)
    reset_button = Button("Retry", 115, 70, 185, 100, "violet", win)
    Txt = Text(Point(win.getWidth()/2, 20), str(msg))
    Txt.draw(win)
    reset_button.show()

    while True :
        mouseP = win.getMouse()
        if(reset_button.isClicked(mouseP)) :
            win.close()
            break

    return True

#Here is the main part of the game
def game(snake, score, score_txt, keyPressed, back, interval, applePos, grd, grdColor, w, h,win) :
    while True :
        mousePos = win.checkMouse()
        keyPress = win.checkKey()

        if(snake.snake_eatApple()) :
            score += 10
            score_txt.setText("Score : " + str(score))

            apple.remove(applePos, grdColor, grd)

            snake.increaseBody(keyPressed)
            snake.set_applePos(apple.show(w, h, grd, snake.getBodyPos()))

            if snake.gameOver() :
                if show_screen("GAME OVER", mousePos) :
                    snake.removeBody()
                    return True

        snake.update()

        if(keyPress == "Left" or keyPress == "Right" or keyPress == "Up" or keyPress == "Down") :
            if((keyPressed == "Left" and keyPress != "Right") or (keyPressed == "Right" and keyPress != "Left") or (keyPressed == "Up" and keyPress != "Down") or (keyPressed == "Down" and keyPress != "Up")) :
                keyPressed = keyPress

        snake.removeBody()
        snake.join_Body()
        snake.movement(keyPressed)

        if snake.getPos().y < 0 :
            if show_screen("GAME OVER", score_txt) :
                return True

        if snake.gameOver() :
            apple.remove(applePos, grdColor, grd)
            if show_screen("GAME OVER", score_txt) :
                return True

        try :
            snake.update()
        except :
            if show_screen("GAME OVER", score_txt) :
                return True

        t.sleep(interval)

        if(mousePos != None) :
            if(back.isClicked(mousePos)) :
                back.__del__()
                break

    return False
