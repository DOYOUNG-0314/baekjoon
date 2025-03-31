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





import sys
sys.setrecursionlimit(1000)
input = sys.stdin.readline

n = int(input())  # 컴퓨터 수
m = int(input())  # 연결된 쌍 수

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 간선 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

def dfs(v):
    global count
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            count += 1
            dfs(neighbor)

dfs(1)
print(count)
