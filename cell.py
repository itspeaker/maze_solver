from graphics import Window, Line, Point


class Cell:
    def __init__(self, window: Window | None = None) -> None:
        self.has_right_wall = True
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self._win is None:
            return

        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        if self.has_right_wall:
            self._win.draw_line(right_wall, fill_color="white")
        else:
            self._win.draw_line(right_wall, fill_color="black")

        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.has_left_wall:
            self._win.draw_line(left_wall, fill_color="white")
        else:
            self._win.draw_line(left_wall, fill_color="black")

        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        if self.has_top_wall:
            self._win.draw_line(top_wall, fill_color="white")
        else:
            self._win.draw_line(top_wall, fill_color="black")

        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, fill_color="white")
        else:
            self._win.draw_line(bottom_wall, fill_color="black")

    def draw_move(self, to_cell, undo=False):
        color = "grey"
        if not undo:
            color = "red"

        half_cell = abs(self._x2 - self._x1) // 2
        x_center = half_cell + self._x1
        y_center = half_cell + self._y1

        half_cell2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_cell2 + to_cell._x1
        y_center2 = half_cell2 + to_cell._y1

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, color)
