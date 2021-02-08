# 2018 - electronstogo

# Class that keeps the square properties and includes methods to handle the squares.
class Square:
    def __init__(self, coord_x, coord_y, pos_x, pos_y, length):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.length = length

        self.alive = False
        self.modified = True


    # Draw the square.
    def draw_me(self, canvas):
        if self.modified:
            canvas.create_line(self.pos_x, self.pos_y, self.pos_x + self.length, self.pos_y, fill="#000000", width=1)
            canvas.create_line(self.pos_x, self.pos_y, self.pos_x, self.pos_y + self.length, fill="#000000", width=1)
            canvas.create_line(self.pos_x + self.length, self.pos_y, self.pos_x + self.length, self.pos_y + self.length,
                               fill="#000000", width=1)
            canvas.create_line(self.pos_x, self.pos_y + self.length, self.pos_x + self.length, self.pos_y + self.length,
                               fill="#000000", width=1)

            if self.alive:
                canvas.create_rectangle(self.pos_x, self.pos_y, self.pos_x + self.length, self.pos_y + self.length,
                                        fill='red')
            else:
                canvas.create_rectangle(self.pos_x, self.pos_y, self.pos_x + self.length, self.pos_y + self.length,
                                        fill='white')

        self.modified = False



    # check if the status of this square with the rules of the game of life.
    def check_life(self, square_buffer_list, squares_per_row, squares_per_column):
        # alive square neighbour counter.
        neighbours_alive_number = 0

        if self.coord_x + 1 < squares_per_row:
            if square_buffer_list[self.coord_x + 1][self.coord_y].alive:
                neighbours_alive_number += 1

            if self.coord_y + 1 < squares_per_column:
                if square_buffer_list[self.coord_x + 1][self.coord_y + 1].alive:
                    neighbours_alive_number += 1

            if self.coord_y - 1 >= 0:
                if square_buffer_list[self.coord_x + 1][self.coord_y - 1].alive:
                    neighbours_alive_number += 1

        if self.coord_x - 1 >= 0:
            if square_buffer_list[self.coord_x - 1][self.coord_y].alive:
                neighbours_alive_number += 1

            if self.coord_y + 1 < squares_per_column:
                if square_buffer_list[self.coord_x - 1][self.coord_y + 1].alive:
                    neighbours_alive_number += 1

            if self.coord_y - 1 >= 0:
                if square_buffer_list[self.coord_x - 1][self.coord_y - 1].alive:
                    neighbours_alive_number += 1

        if self.coord_y - 1 >= 0:
            if square_buffer_list[self.coord_x][self.coord_y - 1].alive:
                neighbours_alive_number += 1

        if self.coord_y + 1 < squares_per_column:
            if square_buffer_list[self.coord_x][self.coord_y + 1].alive:
                neighbours_alive_number += 1

        if neighbours_alive_number == 3 and not self.alive:
            self.alive = True
            self.modified = True
        elif neighbours_alive_number < 2 and self.alive:
            self.alive = False
            self.modified = True
        elif neighbours_alive_number > 3 and self.alive:
            self.alive = False
            self.modified = True
