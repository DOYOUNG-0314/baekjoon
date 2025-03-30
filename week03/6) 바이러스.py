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
