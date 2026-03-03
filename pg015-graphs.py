def adj(v,edges):
    al = {}
    for i in range(v):
        al[i]=[]
    print(al)
    
    #add edges
    for edge in edges:
        v1, v2 = edge
        al[v1].append(v2)
    print(al)
v=4
edges=[[0,1],[1,2],[1,3],[2,3],[3,0]]
adj(v,edges)