import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(start_node):
    q = deque([start_node])
    while q:
        now = q.popleft()
        
        print(now, end=' ')
        
        for next_node in graph[now]:
            if visited[next_node]:
                continue
            
            visited[next_node] = 1
            q.append(next_node)

V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    
visited = [0] * (V + 1)
visited[1] = 1
bfs(1)