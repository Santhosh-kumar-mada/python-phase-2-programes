#flood color
def colorsfinder(image,sr,sc,color):
    org = image[sr][sc]
    if org == color:
        return
    row,col = len(image),len(image[0])
    def dfs(r,c):
        
        if r<0 or r>=row or c<0 or c>=col or image[r][c] != org:
            return 
        image[r][c]=color
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)
        
    dfs(sr,sc)
    print(image)
    


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
colorsfinder(image,sr,sc,color)