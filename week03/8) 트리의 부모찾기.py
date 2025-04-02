import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

# 간선 입력 받기
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 함수 정의
def dfs(node, par):
    parent[node] = par
    for neighbor in graph[node]:
        if parent[neighbor] == 0:
            dfs(neighbor, node)

# 루트는 1번
dfs(1, 0)

# 결과 출력 (2번 노드부터)
for i in range(2, n + 1):
    print(parent[i])
