import sys
sys.stdin = open("input.txt", "r")

def dfs(node):
    print(f"node: {node}")
    
    for next_node, next_weight in graph[node]:
        if visited[next_node]:
            continue
    
        visited[next_node] = 1
        dfs(next_node)
    
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    graph[end].append((start, weight))
    
visited = [0] * (V + 1)
visited[1] = 1
dfs(1)