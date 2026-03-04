def count_components(graph):
    visited = set()
    def dfs(node):
        visited.add(node)
        for nbr in graph.get(node,[]):
            if nbr not in visited:
                dfs(nbr)
    count = 0
    for u in graph:
        if u not in visited:
            dfs(u)
            count +=1
    return count

g = {
    1 : [2],
    2 : [1,3],
    3 : [2],
    4 : [],
    5 : [6],
    6 : [5]
}
print(count_components(g))