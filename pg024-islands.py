def numIslands(grid):
    if not grid or not grid[0]:
        return 0
    m,n = len(grid), len(grid[0])
    def dfs(r,c):
        if r<0 or r>=m or c<0 or c>=n or grid[r][c] != '1':
            return 
        grid[r][c]='0'
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)
    count=0
    for r in range(m):
        for c in range(n):
            if grid[r][c]=='1':
                count +=1
                dfs(r,c)
    return count
    
        


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","1"]
]

print(numIslands(grid))