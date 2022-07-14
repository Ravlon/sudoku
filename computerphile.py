import numpy as np


unsolved = "060800510502013006080005007003000900950081000001304260200906700600000009790102043"
solved = "367849512542713896189625437423567981956281374871394265214936758635478129798152643"

grid = [[] for i in range(9)]
h = 0
for i in range(9):
    for j in range(9):
        grid[i].append(int(unsolved[h]))
        h+=1

def possible(x,y,n):
    global grid
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(x,y,n):
                        grid[y][x] = n
                        #print(y,"|",x,"|",n)
                        solve()
                        grid[y][x] = 0
                return 0
    print(np.matrix(grid))


def main():
    global grid
    solve()  

if __name__ == "__main__":
    main()