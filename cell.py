from tkinter import BOTH

class Cell():
    def __init__(
            self,
            p1,
            p2,
            visited = False
            
    ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        self.p1 = p1
        self.p2 = p2
        self.visited = False

    def draw(self, canvas, fill_color="black"):
        if self.has_left_wall:
            canvas.create_line(
                self.p1.x,
                self.p1.y,
                self.p1.x,
                self.p2.y,
                fill = fill_color,
                width = 2
            )
            canvas.pack(fill = BOTH, expand=1)
        else: 
            canvas.create_line(
                self.p1.x,
                self.p1.y,
                self.p1.x,
                self.p2.y,
                fill = "white",
                width = 2
            )
            canvas.pack(fill = BOTH, expand=1)
        if self.has_right_wall:
            canvas.create_line(
                self.p2.x,
                self.p1.y,
                self.p2.x,
                self.p2.y,
                fill = fill_color,
                width = 2
            )
            canvas.pack(fill = BOTH, expand=1)
        else:
            canvas.create_line(
                self.p2.x,
                self.p1.y,
                self.p2.x,
                self.p2.y,
                fill = "white",
                width = 2
            )
            canvas.pack(fill = BOTH, expand=1)
        if self.has_top_wall:
            canvas.create_line(
                self.p1.x,
                self.p1.y,
                self.p2.x,
                self.p1.y,
                fill = fill_color,
                width = 2
            )
            canvas.pack(fill = BOTH, expand=1)
        else:
            canvas.create_line(
                self.p1.x,
                self.p1.y,
                self.p2.x,
                self.p1.y,
                fill = "white",
                width = 2
            )
            canvas.pack(fill = BOTH, expand=1)
        if self.has_bottom_wall:
            canvas.create_line(
                self.p1.x,
                self.p2.y,
                self.p2.x,
                self.p2.y,
                fill = fill_color,
                width = 2
            )
            canvas.pack(fill = BOTH, expand=1)
        else:
            canvas.create_line(
                self.p1.x,
                self.p2.y,
                self.p2.x,
                self.p2.y,
                fill = "white",
                width = 2
            )
            canvas.pack(fill = BOTH, expand=1)

    def draw_move(self, to_cell, canvas, undo=False):
        center_x1 = (self.p1.x + self.p2.x) / 2
        center_y1 = (self.p1.y + self.p2.y) / 2
        center_x2 = (to_cell.p1.x + to_cell.p2.x) / 2
        center_y2= (to_cell.p1.y + to_cell.p2.y) / 2

        fill_colour = "red"
        if undo:
            fill_colour = "grey"

        canvas.create_line(
            center_x1,
            center_y1,
            center_x2,
            center_y2,
            fill = fill_colour,
            width = 2
        )
        canvas.pack(fill=BOTH, expand=1)