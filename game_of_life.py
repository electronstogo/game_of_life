#2018 - electronstogo

from tkinter import *
import square


# Side length of the rectangles.
# Use this value to define the resolution of the field.
SQUARE_SIDE_LENGTH = 10

# Define the game square size here.
GAME_SQUARE_SIDE_LENGTH = 600

# Calculate the squares per row and column.
SQUARES_IN_A_ROW = int(GAME_SQUARE_SIDE_LENGTH / SQUARE_SIDE_LENGTH)
SQUARES_IN_A_COLUMN = int(GAME_SQUARE_SIDE_LENGTH / SQUARE_SIDE_LENGTH)




# class that handles the implemented game of life.
class GameOfLife:
    def __init__(self):
        self.root = Tk()
        self.root.title('Game of life')
        self.root.after(100, self.update)
        self.c = Canvas(self.root, bg='white', width=GAME_SQUARE_SIDE_LENGTH + 1, height=GAME_SQUARE_SIDE_LENGTH + 1,
                        name="canvas")
        self.c.pack()

        self.b = Button(self.root, text="START", command=self.start_button_clicked, name="startButton")
        self.b.pack()

        self.square_list = []
        self.mouse_button_clicked = False
        self.squares_updated_during_init = True
        self.init_active = True

        self.init_squares()
        self.draw_squares()

        self.root.bind('<Motion>', self.motion)
        self.root.bind('<ButtonRelease-1>', self.button_released)
        self.root.bind('<Button-1>', self.clicked)


        self.root.mainloop()

    # method activated by start button.
    def start_button_clicked(self):
        self.init_active = False


    # method activated by clicked mouse button.
    def clicked(self, event):
        # handle click only during init mode and for clicks inside the game field.
        if self.init_active and event.widget != self.b:
            self.mouse_button_clicked = True
            x, y = event.x, event.y

            if x / SQUARE_SIDE_LENGTH < SQUARES_IN_A_ROW and y / SQUARE_SIDE_LENGTH < SQUARES_IN_A_COLUMN:
                self.square_list[int(x / SQUARE_SIDE_LENGTH)][int(y / SQUARE_SIDE_LENGTH)].alive = True
                self.square_list[int(x / SQUARE_SIDE_LENGTH)][int(y / SQUARE_SIDE_LENGTH)].modified = True
                self.squares_updated_during_init = True


    # method activated by released mouse button.
    def button_released(self, event):
        self.mouse_button_clicked = False


    # method activated by movement of mouse.
    def motion(self, event):
        # react only during clicked mouse button on field, while the init mode is active.
        if self.mouse_button_clicked and self.init_active and event.widget != self.b:
            x, y = event.x, event.y

            # modify square if index is valid.
            if x / SQUARE_SIDE_LENGTH < SQUARES_IN_A_ROW and y / SQUARE_SIDE_LENGTH < SQUARES_IN_A_COLUMN:
                self.square_list[int(x / SQUARE_SIDE_LENGTH)][int(y / SQUARE_SIDE_LENGTH)].alive = True
                self.square_list[int(x / SQUARE_SIDE_LENGTH)][int(y / SQUARE_SIDE_LENGTH)].modified = True
                self.squares_updated_during_init = True


    # Init the squares on field with side length and position.
    def init_squares(self):
        for rows in range(SQUARES_IN_A_ROW):
            row_square_list = []

            for columns in range(SQUARES_IN_A_COLUMN):
                r = square.Square(rows, columns, rows * SQUARE_SIDE_LENGTH + 2, columns * SQUARE_SIDE_LENGTH + 2, SQUARE_SIDE_LENGTH)
                row_square_list.append(r)

            self.square_list.append(row_square_list)


    # Screen update.
    def update(self):
        if not self.init_active:
            square_buffer_list = self.square_list[:]

            for rows in range(int(SQUARES_IN_A_ROW)):
                for columns in range(int(SQUARES_IN_A_COLUMN)):
                    self.square_list[rows][columns].check_life(square_buffer_list, SQUARES_IN_A_ROW, SQUARES_IN_A_COLUMN)

            self.draw_squares()

        if self.squares_updated_during_init and self.init_active:
            self.draw_squares()
            self.squares_updated_during_init = False

        self.root.after(100, self.update)


    # draw all squares into the game field.
    def draw_squares(self):
        for rows in range(int(SQUARES_IN_A_ROW)):
            for columns in range(int(SQUARES_IN_A_COLUMN)):
                self.square_list[rows][columns].draw_me(self.c)


if __name__ == '__main__':
    GameOfLife()
