def rott (grid):
    m = len(grid)
    n = len(grid[0])
    mins = 0
    while True:
        newGrid = [row[:] for row in grid]
        change = False
        for i in range(m):
            for j in range(n):
                if (i > 0 and grid[i-1][j]==2) or (i<m-1 and grid[i+1][j]==2) or (j<n-1 and grid[i][j+1]==2) or (j>0 and grid[i][j-1]==2):
                    grid[i][j]=2
                    change=True
        if not change:
            for row in grid:
                if 1 in row:
                    return -1
            return mins
        grid = newGrid
        mins+=1

grid = [[2,1,1],[1,1,0],[0,1,1]]

print(rott (grid))