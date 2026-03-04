#traversal in graphs

from collections import deque              
                
def dfs(graph , node, visited = None):
    if visited  is None:
        visited = set()
    visited.add(node)
    print(node,end=" ")
    for nbr in graph[node]:
        if nbr not in visited:
            dfs(graph,nbr,visited)
                

graph = {
    0:[1,3,4],
    1:[0,2,4],
    2:[1,4,5,6],
    3:[0,4],
    4:[0,1,2,3,5],
    5:[2,4,6],
    6:[2,5]
}
dfs(graph,0)