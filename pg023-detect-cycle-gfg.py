def crt_graph (v,edges):
    graph = { i : [] for i in range(V)}
	    
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited=set()
    
    def dfs(node,parent):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei,node):
                    return True
            elif nei != parent:
                return True
        return False
        
        
    for node in range(V):
        if node not in visited:
            if dfs(node,-1):
                return True
    return False

V = 4
E = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

print(crt_graph(V,edges))