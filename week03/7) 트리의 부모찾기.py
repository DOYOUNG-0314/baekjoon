import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
visited = [False] * (n + 1)

# 트리(무방향 그래프) 입력
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS로 부모 찾기
def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            parent[neighbor] = node  # 부모 기록
            dfs(neighbor)

dfs(1)

# 2번 노드부터 부모 출력
for i in range(2, n + 1):
    print(parent[i])
