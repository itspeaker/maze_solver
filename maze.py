import random
import time
from cell import Cell
from graphics import Window


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Window | None = None,
        seed: int | None = None,
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        if seed:
            random.seed(seed)
        self._win = win
        self._cells: list[list[Cell]] = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for _ in range(self._num_cols):
            self._cells.append([Cell(self._win) for _ in range(self._num_rows)])

        for i in range(len(self._cells)):
            col = self._cells[i]
            for j in range(len(col)):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self, path=False):
        if self._win is None:
            return
        self._win.redraw()
        if path:
            time.sleep(0.1)
        else:
            time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        c: Cell = self._cells[i][j]
        c.visited = True
        while True:
            to_visit = []
            if j - 1 >= 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if i + 1 <= len(self._cells) - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j + 1 <= len(self._cells[0]) - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            if i - 1 >= 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            rand_index = random.randint(0, len(to_visit) - 1)
            i_next, j_next = to_visit[rand_index]
            c_next: Cell = self._cells[i_next][j_next]

            if i < i_next:
                c.has_right_wall = False
                c_next.has_left_wall = False

            if i > i_next:
                c.has_left_wall = False
                c_next.has_right_wall = False

            if j < j_next:
                c.has_bottom_wall = False
                c_next.has_top_wall = False

            if j > j_next:
                c.has_top_wall = False
                c_next.has_bottom_wall = False

            self._break_walls_r(i_next, j_next)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate(path=True)
        cell: Cell = self._cells[i][j]
        cell.visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        if j - 1 >= 0:
            to_cell: Cell = self._cells[i][j - 1]
            if not to_cell.visited and not to_cell.has_bottom_wall:
                cell.draw_move(to_cell)
                if self._solve_r(i, j - 1):
                    return True
                cell.draw_move(to_cell, undo=True)

        if i + 1 <= len(self._cells) - 1:
            to_cell: Cell = self._cells[i + 1][j]
            if not to_cell.visited and not to_cell.has_left_wall:
                cell.draw_move(to_cell)
                if self._solve_r(i + 1, j):
                    return True
                cell.draw_move(to_cell, undo=True)

        if j + 1 <= len(self._cells[0]) - 1:
            to_cell: Cell = self._cells[i][j + 1]
            if not to_cell.visited and not to_cell.has_top_wall:
                cell.draw_move(to_cell)
                if self._solve_r(i, j + 1):
                    return True
                cell.draw_move(to_cell, undo=True)

        if i - 1 >= 0:
            to_cell: Cell = self._cells[i - 1][j]
            if not to_cell.visited and not to_cell.has_right_wall:
                cell.draw_move(to_cell)
                if self._solve_r(i - 1, j):
                    return True
                cell.draw_move(to_cell, undo=True)

        return False
