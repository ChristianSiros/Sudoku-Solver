import math

class Board:

    def __init__(self):
        self.grid = [[0 for i in range(9)] for j in range(9)]     
        self.found_solution = False

    def set_grid(self, grid):
        self.grid = grid
    
    def print(self):
        for i in range(9):
            for j in range(9):
                print(self.grid[i][j], " ", end = "")
            print()
        print()

    def is_valid(self, index, num):
        row = math.floor(index/9)
        col = index % 9

        for x in range(9):
            if self.grid[row][x] == num:
                return False

        for x in range(9):
            if self.grid[x][col] == num:
                return False
    
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[i + startRow][j + startCol] == num:
                    return False
        return True
 
    def solve_by_backtracking(self, index):
        row = math.floor(index/9)
        col = index % 9

        if (index == 80):
            return True

        if self.grid[row][col] > 0:
            return self.solve_by_backtracking(index + 1)

        for num in range(1, 10):
        
            if self.is_valid(index, num):
            
                self.grid[row][col] = num

                if self.solve_by_backtracking(index + 1):
                    return True
    
            self.grid[row][col] = 0
        return False
