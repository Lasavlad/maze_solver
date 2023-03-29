from tkinter import Tk, BOTH, Canvas
from maze import Maze
import sys

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.title = self.__root.title("the maze app")
        self.canvas = Canvas()
        self.canvas.pack(fill=BOTH, expand=1)
        self.window_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def draw_cell(self, cell, fill_color):
        cell.draw(self.canvas, fill_color)
        
    def draw_move(self, cell, to_cell, undo=False):
        cell.draw_move(to_cell, self.canvas, undo)

    def close(self):
        self.window_running = False

    
def main():
    screen_x = 600
    screen_y = 400
    margin = 50
    num_of_rows = 50
    num_of_cols = 50
    cell_size_x = screen_x /num_of_rows
    cell_size_y = screen_y / num_of_cols
    win = Window(screen_x, screen_y)

    sys.setrecursionlimit(10000)

    maze = Maze(margin, margin, num_of_rows, num_of_cols, cell_size_x, cell_size_y, win)
    solved = maze.solve()
    if not solved:
        print('Not solved')
    else:
        print('solved')

    win.wait_for_close()

main()