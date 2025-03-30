from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
n, m, v = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 간선 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 것부터 방문하기 위해 정렬
for i in range(1, n + 1):
    graph[i].sort()

# DFS
visited_dfs = [False] * (n + 1)
def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited_dfs[neighbor]:
            dfs(neighbor)

# BFS
visited_bfs = [False] * (n + 1)
def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for neighbor in graph[cur]:
            if not visited_bfs[neighbor]:
                visited_bfs[neighbor] = True
                queue.append(neighbor)

# 실행
dfs(v)
print()
bfs(v)
