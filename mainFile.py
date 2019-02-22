from tkinter import *
from copy import deepcopy

import rectangle


RECTANGLE_SIDE_LENGTH = 10
RECTS_IN_A_ROW = 600 / RECTANGLE_SIDE_LENGTH
RECTS_IN_A_COLUMN = 600 / RECTANGLE_SIDE_LENGTH

class GameOfLife:
    def __init__(self):
        self.root = Tk()
        self.root.after(100, self.update)
        self.c = Canvas(self.root, bg='white', width=601, height=601, name="canvas")
        self.c.pack()

        self.b = Button(self.root, text="START", command=self.startButtonIsClicked, name="startButton")
        self.b.pack()

        self.rectList = []
        self.mouseButtonIsClicked = False
        self.rectsWhereUpdatedDuringInitMode = True
        self.initModeIsRunning = True

        self.initRects()
        self.drawRects()

        self.root.bind('<Motion>', self.motion)
        self.root.bind('<ButtonRelease-1>', self.button_released)
        self.root.bind('<Button-1>', self.clicked)


        self.root.mainloop()

    def startButtonIsClicked(self):
        self.initModeIsRunning = False

    def clicked(self, event):
        self.mouseButtonIsClicked = True
        x, y = event.x, event.y

        if self.initModeIsRunning and event.widget != self.b and x/self.rectList[0][0].length < RECTS_IN_A_ROW and y/self.rectList[0][0].length < RECTS_IN_A_COLUMN:
            self.rectList[int(x/self.rectList[0][0].length)][int(y/self.rectList[0][0].length)].alive = True
            self.rectList[int(x/self.rectList[0][0].length)][int(y/self.rectList[0][0].length)].modified = True
            self.rectsWhereUpdatedDuringInitMode = True

    def button_released(self, event):
        self.mouseButtonIsClicked = False

    def motion(self, event):
        x, y = event.x, event.y

        if self.mouseButtonIsClicked:
            if self.initModeIsRunning and event.widget != self.b and x / self.rectList[0][0].length < RECTS_IN_A_ROW and y / self.rectList[0][0].length < RECTS_IN_A_COLUMN:
                self.rectList[int(x/self.rectList[0][0].length)][int(y/self.rectList[0][0].length)].alive = True
                self.rectList[int(x/self.rectList[0][0].length)][int(y/self.rectList[0][0].length)].modified = True
                self.rectsWhereUpdatedDuringInitMode = True

    def initRects(self):
        for rows in range(int(RECTS_IN_A_ROW)):
            rowList = []
            for columns in range(int(RECTS_IN_A_COLUMN)):
                r = rectangle.Rectangle(rows, columns, rows * RECTANGLE_SIDE_LENGTH + 2, columns * RECTANGLE_SIDE_LENGTH + 2, RECTANGLE_SIDE_LENGTH)
                rowList.append(r)
            self.rectList.append(rowList)


    def update(self):
        if not self.initModeIsRunning:
            bufferList = deepcopy(self.rectList)
            for rows in range(int(RECTS_IN_A_ROW)):
                for columns in range(int(RECTS_IN_A_COLUMN)):
                    self.rectList[rows][columns].checkLife(bufferList, RECTS_IN_A_ROW, RECTS_IN_A_COLUMN)

            self.drawRects()

        if self.rectsWhereUpdatedDuringInitMode and self.initModeIsRunning:
            self.drawRects()
            self.rectsWhereUpdatedDuringInitMode = False

        self.root.after(100, self.update)


    def drawRects(self):
        for rows in range(int(RECTS_IN_A_ROW)):
            for columns in range(int(RECTS_IN_A_COLUMN)):
                self.rectList[rows][columns].drawMe(self.c)

if __name__ == '__main__':
    GameOfLife()

