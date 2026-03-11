def creategraph(edges):
    graph = {v:[] for v in range(V)}
    for u,v in edges:
        graph[u].append(v)
    return graph
def topo_order(graph):
    visited = set()
    stack =[]
    def dfs(node):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)
                
        stack.append(node)
    
    for node in graph:
        if node not in visited:
            dfs(node)
            
    return stack[::-1]
def is_valid_topo(V,edges,order):
    if len(order)!= V:
        return False
    pos = {node: i for i , node in enumerate(order)}
    for u,v in edges:
        if pos[u] >= pos[v]:
            return False
    return True
V = 6
E = 6
edges = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]]

g = creategraph(edges)
order = topo_order(g)
print(is_valid_topo(V,edges,order)) 