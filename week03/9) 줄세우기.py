from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)

# 간선 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

# 진입 차수 0인 노드부터 시작
queue = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)

result = []

while queue:
    now = queue.popleft()
    result.append(now)

    for neighbor in graph[now]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

# 결과 출력
print(' '.join(map(str, result)))