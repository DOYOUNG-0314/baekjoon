from collections import deque

# n: 노드 수, m: 간선 수
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)  # 진입 차수 배열

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)   # a → b
    in_degree[b] += 1     # b의 진입 차수 +1

# 진입 차수가 0인 노드를 큐에 삽입
queue = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)

# 위상 정렬 결과 저장 리스트
result = []

# BFS
while queue:
    now = queue.popleft()
    result.append(now)

    for neighbor in graph[now]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

# 결과 출력
for node in result:
    print(node, end=' ')