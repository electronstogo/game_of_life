



class Rectangle():
    def __init__(self, coordX, coordY, xpos, ypos, length):
        self.coordX = coordX
        self.coordY = coordY
        self.xpos = xpos
        self.ypos = ypos

        self.length = length

        self.alive = False
        self.modified = True


    def drawMe(self, canvas):
        if self.modified:
            canvas.create_line(self.xpos, self.ypos, self.xpos + self.length, self.ypos, fill="#000000", width=1)
            canvas.create_line(self.xpos, self.ypos, self.xpos, self.ypos + self.length, fill="#000000", width=1)
            canvas.create_line(self.xpos + self.length, self.ypos, self.xpos + self.length, self.ypos + self.length, fill="#000000", width=1)
            canvas.create_line(self.xpos, self.ypos + self.length, self.xpos + self.length, self.ypos + self.length, fill="#000000", width=1)

            if self.alive:
                canvas.create_rectangle(self.xpos, self.ypos, self.xpos + self.length, self.ypos + self.length, fill='red')
            else:
                canvas.create_rectangle(self.xpos, self.ypos, self.xpos + self.length, self.ypos + self.length, fill='white')

        self.modified = False

    def checkLife(self, rectBufferList, rectsInARow, rectsInAColumn):
         neighbourCounter = 0

         if self.coordX + 1 < rectsInARow:
             if(rectBufferList[self.coordX + 1][self.coordY].alive):
                 neighbourCounter += 1
             if self.coordY + 1 < rectsInAColumn:
                 if rectBufferList[self.coordX + 1][self.coordY + 1].alive:
                     neighbourCounter += 1
             if self.coordY - 1 >= 0:
                 if rectBufferList[self.coordX + 1][self.coordY - 1].alive:
                     neighbourCounter += 1

         if self.coordX - 1 >= 0:
             if(rectBufferList[self.coordX - 1][self.coordY].alive):
                 neighbourCounter += 1
             if self.coordY + 1 < rectsInAColumn:
                 if rectBufferList[self.coordX - 1][self.coordY + 1].alive:
                     neighbourCounter += 1
             if self.coordY - 1 >= 0:
                 if rectBufferList[self.coordX - 1][self.coordY - 1].alive:
                     neighbourCounter += 1

         if self.coordY - 1 >= 0:
             if(rectBufferList[self.coordX][self.coordY - 1].alive):
                 neighbourCounter += 1

         if self.coordY + 1 < rectsInAColumn:
             if(rectBufferList[self.coordX][self.coordY + 1].alive):
                 neighbourCounter += 1


         if neighbourCounter == 3 and self.alive == False:
             self.alive = True
             self.modified = True
         elif neighbourCounter < 2 and self.alive == True:
             self.alive = False
             self.modified = True
         elif neighbourCounter > 3 and self.alive == True:
             self.alive = False
             self.modified = True