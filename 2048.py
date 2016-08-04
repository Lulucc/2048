"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    new_line = [tile for tile in line if tile] + [0] * line.count(0)
    for index in range(len(new_line)-1):
        if new_line[index] == new_line[index+1]:
            new_line[index] *= 2
            new_line[index+1:] = new_line[index+2:] + [0]
    return new_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
        self._direction = {UP: [(0, i) for i in range(grid_width)],
                          DOWN: [(grid_height-1, i) for i in range(grid_width)],
                          LEFT: [(i, 0) for i in range(grid_height)],
                          RIGHT: [(i, grid_width-1) for i in range(grid_height)]}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._cells = [ [0 for dummy_col in range(self._grid_width)] 
                      for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return "hello!"

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        changed = False
        for index1 in self._direction[direction]:
            my_list = []
            for index2 in range(self._grid_width + self._grid_height - len(self._direction[direction])):
                row = list(index1)[0]+index2*list(OFFSETS[direction])[0]
                col = list(index1)[1]+index2*list(OFFSETS[direction])[1]
                my_list.append([row, col])
            my_list_value = []
            for index3 in my_list:
                my_list_value.append(self._cells[index3[0]][index3[1]])
            new_list_value = merge(my_list_value)
            if my_list_value!= new_list_value:
                changed = True
            for index4 in range(len(my_list)):
                self.set_tile(my_list[index4][0], my_list[index4][1], new_list_value[index4])
        if changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        the_range = [(row, col) for row in range(self.get_grid_height())
                       for col in range(self.get_grid_width()) if self.get_tile(row,col) == 0]
        the_tile = random.choice(the_range)
        random_choice = [2] * 9 + [4]
        self.set_tile(the_tile[0],the_tile[1], random.choice(random_choice))

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._cells[row][col] = value
        #pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._cells[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(5, 4))
