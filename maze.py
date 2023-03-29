import random
import time
from cell import Cell
from point import Point


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1= x1
        self.y1= y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cell = []
        self.seed = seed
        self.win = win
        self._create_cells()
        self._break_entrance_and_exit()
        self.break_walls_r(0,0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        p1 = None
        p2 = None
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(p1, p2))
            self._cell.append(col_cells)
        for i in range(self.num_cols):

            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        self._cell[i][j].p1, self._cell[i][j].p2 = p1, p2
        cell = self._cell[i][j]
        self.win.draw_cell(cell, "black")
        self.animate()
    
    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.001)
    
    def _break_entrance_and_exit(self):
        self._cell[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        last_cell_col = len(self._cell) - 1
        last_cell_row = len(self._cell[0]) - 1
        self._cell[last_cell_col][last_cell_row].has_right_wall = False
        self._draw_cell(last_cell_col, last_cell_row)
        

    def break_walls_r(self, i, j):
        self._cell[i][j].visited = True
        while True:
            next_to_visit = []
            possible_index = 0

            #left
            if i > 0 and not self._cell[i - 1][j].visited:
                next_to_visit.append((i - 1, j))
                possible_index += 1
            #right
            if i < self.num_cols - 1 and not self._cell[i + 1][j].visited:
                next_to_visit.append((i + 1, j))
                possible_index += 1
            #up
            if j > 0 and not self._cell[i][j - 1].visited:
                next_to_visit.append((i, j-1))
                possible_index += 1
            #down
            if j < self.num_rows - 1 and not self._cell[i][j + 1].visited:
                next_to_visit.append((i, j + 1))
                possible_index += 1

            if possible_index == 0:
                self._draw_cell(i, j)
                return
            
            direction_index = random.randrange(possible_index)
            next_index = next_to_visit[direction_index]

            #remove walls
            #right
            if next_index[0] == i + 1:
                self._cell[i][j].has_right_wall = False
                self._cell[i + 1][j].has_left_wall = False
            #left
            if next_index[0] == i - 1:
                self._cell[i][j].has_left_wall = False
                self._cell[i - 1][j].has_right_wall = False
            #down
            if next_index[1] == j + 1:
                self._cell[i][j].has_bottom_wall = False
                self._cell[i][j + 1].has_top_wall = False
            #up
            if next_index[1] == j - 1:
                self._cell[i][j].has_top_wall = False
                self._cell[i][j - 1].has_right_wall = False
            
            # recursively visit the next cell
            self.break_walls_r(next_index[0], next_index[1])
        
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cell[i][j].visited = False

    def _solve_r(self, i, j):
        self.animate()

        self._cell[i][j].visited = True
        
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        if i > 0 and not self._cell[i][j].has_left_wall and not self._cell[i - 1][j].visited:
            self.win.draw_move(self._cell[i][j], self._cell[i - 1][j])
            if self._solve_r( i - 1, j):
                return True
            else:
                self.win.draw_move(self._cell[i][j], self._cell[i - 1][j], undo=True)

        if i < self.num_cols - 1 and not self._cell[i][j].has_right_wall and not self._cell[i + 1][j].visited:
            self.win.draw_move(self._cell[i][j], self._cell[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self.win.draw_move(self._cell[i][j], self._cell[i + 1][j], undo=True)

        if j > 0 and not self._cell[i][j].has_top_wall and not self._cell[i][j - 1].visited:
            self.win.draw_move(self._cell[i][j], self._cell[i][j - 1])
            if self._solve_r( i, j-1):
                return True
            else:
                self.win.draw_move(self._cell[i][j], self._cell[i][j - 1], undo=True)

        if j < self.num_rows - 1 and not self._cell[i][j].has_bottom_wall and not self._cell[i][j + 1].visited:
            self.win.draw_move(self._cell[i][j], self._cell[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self.win.draw_move(self._cell[i][j], self._cell[i][j + 1], undo=True)

        return False
    
    def solve(self):
        return self._solve_r(0, 0)