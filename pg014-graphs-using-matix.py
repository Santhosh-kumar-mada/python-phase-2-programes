#number of vertices
v = 4
#empty the matrix
adj = [[0 for i in range(v)]for j in range(v)]

adj[0][1]=1
adj[0][3]=1
adj[1][2]=1
adj[1][3]=1
adj[2][0]=1
adj[2][1]=1
adj[3][0]=1
adj[3][2]=1
print(adj)

for i in range(len(adj)):
    for j in range(len(adj)):
        print(adj[i][j], end = " ")
    print("\n")