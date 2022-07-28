import math
from Cell import Cell

class Board:

    def __init__(self):
        self.grid = [[Cell(row, col) for col in range(9)] for row in range(9)]     

    def set_grid(self, grid):
        for row in range(9):
            for col in range(9):
                self.grid[row][col].set_value(grid[row][col])
    
    def print(self):
        for row in range(9):
            for col in range(9):
                print(self.grid[row][col].get_value(), " ", end = "")
            print()
        print()

    def is_valid(self, index, num):
        row = math.floor(index/9)
        col = index % 9

        for x in range(9):
            if self.grid[row][x].get_value() == num:
                return False

        for x in range(9):
            if self.grid[x][col].get_value() == num:
                return False
    
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[i + startRow][j + startCol].get_value() == num:
                    return False
        return True
 
    def solve_by_backtracking(self, index):
        row = math.floor(index/9)
        col = index % 9

        if (index == 81):
            return True

        if (self.grid[row][col].get_value() > 0):
            return self.solve_by_backtracking(index + 1)

        for num in range(1, 10):
        
            if self.is_valid(index, num):
            
                self.grid[row][col].set_value(num)

                if self.solve_by_backtracking(index + 1):
                    return True
    
            self.grid[row][col].set_value(0)
        return False
