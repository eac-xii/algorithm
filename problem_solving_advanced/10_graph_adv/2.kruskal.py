import sys
sys.stdin = open("mst_input.txt", "r")

def make_set(n):
    parents = [i for i in range(n)]
    ranks = [0] * n
    return parents, ranks

def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)
    if rx == ry:
        return
    if ranks[rx] < ranks[ry]:
        parents[rx] = ry
    elif ranks[rx] > ranks[ry]:
        parents[ry] = rx
    else:
        parents[ry] = rx
        ranks[rx] += 1
        


V, E = map(int, input().split())

edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))
    
edges.sort(key=lambda x: x[2])

count = 0
result = 0
parents, ranks = make_set(V)

for u, v, w in edges:
    if find_set(u) != find_set(v):
        print(u, v, w)
        union(u, v)
        count += 1
        result += w
        
        if count == V - 1:
            break

print(f"minimum cost = {result}")