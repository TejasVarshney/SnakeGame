from graphics import *
import time as t

class Snake :
    def __init__(self, color, grdColor, pos, grd, applePos, win) :
        self.grd = grd
        self.grdColor = grdColor
        self.applePos = applePos
        self.bodyList = [pos, Point(pos.x-1, pos.y), Point(pos.x-2, pos.y), Point(pos.x-3, pos.y), Point(pos.x-4, pos.y)]
        self.init_bodyList = self.bodyList
        self.pos = pos
        self.init_pos = pos
        self.win = win
        self.color = color
        self.size = 4

    def removeBody(self):
        #for i in range(0, self.size) :
        #    x = int(self.bodyList[i].x)
        #    y = int(self.bodyList[i].y)
        #    self.grd[x][y].setFill(self.grdColor)
        x = int(self.bodyList[0].x)
        y = int(self.bodyList[0].y)
        self.grd[x][y].setFill(self.grdColor)

        x = int(self.bodyList[self.size-1].x)
        y = int(self.bodyList[self.size-1].y)
        self.grd[x][y].setFill(self.grdColor)

    def join_Body(self) :
        for i in range(0, self.size-1) :
            x = int(self.bodyList[i].x)
            y = int(self.bodyList[i].y)
            self.grd[x][y].setFill(self.color)

    def reset(self) :
        self.pos = self.init_pos
        self.bodyList = self.init_bodyList
        self.size = 4

        for i in range(0, self.size-1) :
            x = int(self.bodyList[i].x)
            y = int(self.bodyList[i].y)
            self.grd[x][y].setFill(self.color)

    def movement(self, dir):
        posChg = False

        if dir == "Left" :
            posChg = True
            self.pos = Point(self.pos.x-1, self.pos.y)
        elif dir == "Right" :
            posChg = True
            self.pos = Point(self.pos.x+1, self.pos.y)
        elif dir == "Up" :
            posChg = True
            self.pos = Point(self.pos.x, self.pos.y-1)
        elif dir == "Down" :
            posChg = True
            self.pos = Point(self.pos.x, self.pos.y+1)

        i = self.size + 1
        while i <= self.size + 1 and i > 0 and posChg:
            i-=1
            self.bodyList[i] = self.bodyList[i-1]
        self.bodyList[0] = self.pos

    def set_applePos(self, appleL) :
        self.applePos = appleL

    def get_applePos(self) :
        return self.applePos

    def getPos(self) :
        return self.pos

    def setWin(self, win) :
        self.win = win

    def update(self) :
        #for i in range (0, self.size) :
        #    x = int(self.bodyList[i].x)
        #    y = int(self.bodyList[i].y)
        #    self.grd[x][y].setFill(self.color)
        x = int(self.bodyList[0].x)
        y = int(self.bodyList[0].y)
        self.grd[x][y].setFill(self.color)

        x = int(self.bodyList[self.size-1].x)
        y = int(self.bodyList[self.size-1].y)
        self.grd[x][y].setFill(self.color)

    def getPos(self) :
        return self.pos

    def getBodyPos(self) :
        return self.bodyList
        
    def snake_eatApple(self) :
        if(self.pos.x == self.applePos.x and self.pos.y == self.applePos.y) :
            return True
        else :
            return False

    def increaseBody(self, dir) :
        offsetX = 0
        offsetY = 1

        x = self.bodyList[self.size].x
        y = self.bodyList[self.size].y
        self.bodyList.append(Point(x, y))
        self.size += 1

    def gameOver(self) :
        for i in range(1, self.size+1) :
            if (self.bodyList[i].x == self.bodyList[0].x) and (self.bodyList[i].y == self.bodyList[0].y) :
                print("Game Over")
                return True

        return False
