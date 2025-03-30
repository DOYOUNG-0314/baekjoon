#유니온 파인드

# 초기화 
parent = [i for i in range(n + 1)]

# find (경로 압축)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# union
def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

#DFS(깊이 우선 탐색)
visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)

# BFS(너비 우선 탐색)
from collections import deque
visited = [False] * (n + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
