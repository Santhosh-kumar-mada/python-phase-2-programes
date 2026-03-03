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
    10:[30],
    20 : [10,50,60],
    30 : [60],
    40 : [10,20],
    50 : [70],
    60 : [70],
    70 : []
}
bfs(graph,40)