# Creator : Tejas Varshney
# Since there was no button function in graphics.py, therefore it may helf you

from graphics import*

class Button :

    def __init__(self, text, x1, y1, x2, y2, colour, win) :
        self.text = text
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.colour = colour
        self.win = win
        self.layout = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))
        self.label = Text(Point((self.x2 - self.x1)/2 + self.x1, (self.y2 - self.y1)/2 + self.y1), self.text)

    def show(self) :
        self.layout.setFill(self.colour)
        self.layout.draw(self.win)
        self.label.draw(self.win)

    def isClicked(self, p1) :
        if((p1.x > self.x1) and (p1.y > self.y1) and (p1.x < self.x2) and (p1.y < self.y2)) :
            return True
        else :
            return False

    def setText(self, txt) :
        self.text = txt
        self.label.setText(self.text)

    def getText(self) :
        return self.text

    def setColour(self, color) :
        self.colour = color
        self.layout.setFill(self.colour)

    def startP(self) :
        return Point(self.x1, self.y1)

    def setWin(self, win) :
        self.win = win

    def endP(self) :
        return Point(self.x2, self.y2)

    def __del__(self) :
        self.layout.undraw()
        self.label.undraw()
