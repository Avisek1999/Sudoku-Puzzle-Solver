import numpy as np
from array import *

grid = [[9, 6, 0, 0, 4, 0, 1, 0, 0],
        [0, 0, 0, 3, 8, 0, 0, 0, 0],
        [7, 0, 8, 0, 6, 0, 0, 0, 9],
        [1, 2, 0, 8, 0, 0, 9, 0, 3],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [3, 0, 5, 0, 0, 2, 0, 6, 4],
        [8, 0, 0, 0, 9, 0, 4, 0, 7],
        [0, 0, 0, 0, 3, 8, 0, 0, 0],
        [0, 0, 9, 0, 2, 0, 0, 8, 5]]

def possible(y,x,n):          # x -> horizontal position    y -> vertical position 
    global grid
    for i in range (0,9):
        if grid[y][i] == n:   # check row
            return False
    for i in range (0,9):     
        if grid[i][x] == n:   # check column
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range (0,3):
        for j in range (0,3):
            if grid[y0+i][x0+j] == n:  # check 3*3 grid
                return False
    return True

possible(4,4,5)  #checks whether inserting 5 is possible in row-4 and col-4 or not

print("The solved grid is:");

def solve():
    global grid
    for y in range (9):
        for x in range (9):
            if grid[y][x] == 0:   # checks for blank grids
                for n in range (1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0  #backtracks
                return  
    print(np.matrix(grid))   
    input("")
    
solve()







