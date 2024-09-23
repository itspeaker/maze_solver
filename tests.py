import unittest
from maze import Maze


class MazeTests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 20
        num_cols = 20
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_maze_create_cells_with_margin(self):
        num_rows = 30
        num_cols = 30
        maze = Maze(5, 5, num_rows, num_cols, 5, 5)
        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_entrance_and_exit(self):
        num_rows = 20
        num_cols = 20
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(maze._cells[0][0].has_top_wall, False)
        self.assertEqual(maze._cells[num_cols - 1][num_rows - 1].has_bottom_wall, False)


if __name__ == "__main__":
    unittest.main()
