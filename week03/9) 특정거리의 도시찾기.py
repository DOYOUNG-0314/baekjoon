from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 그래프 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 거리 배열: 처음엔 모두 -1 (방문 안 함 의미)
distance = [-1] * (n + 1)
distance[x] = 0  # 출발 도시는 거리 0

# BFS 시작
queue = deque([x])
while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

# 거리 K인 노드들 출력
found = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        found = True

if not found:
    print(-1)
