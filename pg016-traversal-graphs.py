#traversal in graphs
from collections import deque
def bfs(graph,start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node,end = " ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                

graph = {
    0 : [1,2],
    1 : [0,3,4],
    2 : [0,3],
    3 : [1,2,4],
    4 : [1,3]
}
bfs(graph,1)


