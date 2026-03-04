#traversal in graphs
from collections import deque
# def bfs(graph,start):
#     visited = {start}
#     queue = deque([start])
#     while queue:
#         node = queue.popleft()
#         print(node,end = " ")
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)


def dfs(graph,start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        print(node,end=" ")
        visited.add(node)
        for nbr in reversed(graph.get(node,[])):
            if nbr not in visited:
                
                stack.append(nbr)
                

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