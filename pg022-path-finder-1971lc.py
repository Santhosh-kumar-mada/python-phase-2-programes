def pathfinder(n,edges,source,destination):
    def creategraph(n,edges):
        graph = {i:[] for i in range(n)}
        for u,v in edges :
            graph[u].append(v)
            graph[v].append(u)
        return graph
    def path_dfs(g,start,end,visited=None):
        if visited == None:
            visited = set()
        if start == destination:
            return True
        visited.add(start)
        for nbr in g[start]:
            if nbr not in visited :
                if path_dfs(g,nbr,end,visited):
                    return True
        return False



    g=creategraph(n,edges)
    return path_dfs(g,source,destination)


n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
print(pathfinder(n,edges,source,destination))