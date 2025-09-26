import sys
sys.stdin = open("input.txt", "r")

V, E = map(int, input().split())

# 인접 행렬
def adj_matrix():
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start][end] = weight
        graph[end][start] = weight

    print("인접 행렬")
    for row in graph[1:]:
        print(row[1:])
    print()

def adj_list():    
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start].append((end, weight))
        graph[end].append((start, weight))
    
    print("인접 리스트")
    for row in graph[1:]:
        print(row)

adj_matrix()
# adj_list()