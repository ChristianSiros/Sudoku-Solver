from Board import Board
import time

start = time.time()

hard_test = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 3, 0, 8, 5],
             [0, 0, 1, 0, 2, 0, 0, 0, 0],
             [0, 0, 0, 5, 0, 7, 0, 0, 0],
             [0, 0, 4, 0, 0, 0, 1, 0, 0],
             [0, 9, 0, 0, 0, 0, 0, 0, 0],
             [5, 0, 0, 0, 0, 0, 0, 7, 3],
             [0, 0, 2, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 4, 0, 0, 0, 9]]
test = [[0, 1, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 8, 0],
        [6, 0, 0, 0, 4, 3, 0, 1, 5],
        [4, 7, 0, 0, 8, 6, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 9, 8],
        [5, 3, 0, 9, 0, 2, 0, 0, 4],
        [0, 4, 0, 6, 2, 0, 8, 7, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 9, 0, 0, 7, 0, 2, 0, 0]]

board = Board()
board.set_grid(test) 

board.print()
 
if(board.solve_by_backtracking(0)):
    board.print()
else:
    print("No Solution Exists for this Puzzle")

end = time.time()

total_time = end - start
print(total_time)