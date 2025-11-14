# 그래프 구조
# 
#         A
#       / | \
#      B  D  E
#     / \
#    C   D

graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A']
}

def dfs(graph, cur_v, visited=[]):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            visited = dfs(graph, v, visited)
    return visited

print(dfs(graph, 'A'))