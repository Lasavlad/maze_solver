import unittest
from main import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_of_cols = 10
        num_of_rows = 10
        m1 = Maze(0, 0, num_of_rows, num_of_cols, 10, 10)
        self.assertEqual(
            len(m1._cell), num_of_cols
        )
        self.assertEqual(
            len(m1._cell[0]),
            num_of_rows
        )
    
    def test_maze_very_big_cells(self):
        num_of_cols = 20
        num_of_rows = 15
        m2 = Maze(0,0,num_of_rows,num_of_cols, 30,30)
        self.assertEqual(
            len(m2._cell), num_of_cols
        )
        self.assertEqual(
            len(m2._cell[0]),
            num_of_rows
        )

        
    def test_reset_cells_visited(self):
        num_of_rows = 10
        num_of_cols = 10
        m = Maze(0,0, num_of_rows, num_of_cols, 10, 10)
        for i in range(num_of_cols):
            for j in range(num_of_rows):
                self.assertEqual(
                    m._cell[i][j].has_right_wall,
                    True
                )
                self.assertEqual(
                    m._cell[i][j].has_top_wall,
                    True
                )
                self.assertEqual(
                    m._cell[i][j].has_buttom_wall,
                    True
                )
                self.assertEqual(
                    m._cell[i][j].has_left_wall,
                    True
                )

if __name__ == "__main__":
    unittest.main()