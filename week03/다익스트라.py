import heapq

INF = int(1e9)  # 무한을 의미하는 값
n, m = map(int, input().split())  # 노드 개수, 간선 개수
start = int(input())  # 시작 노드 번호

graph = [[] for _ in range(n + 1)]  # 인접 리스트
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # u에서 v로 가는 가중치 w인 간선

def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))  # (거리, 노드)

    while q:
        dist, now = heapq.heappop(q)

        # 이미 처리된 적 있는 노드는 무시
        if distance[now] < dist:
            continue

        for neighbor, weight in graph[now]:
            cost = dist + weight
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(q, (cost, neighbor))

    return distance

# 실행 및 출력
result = dijkstra(start)
for i in range(1, n + 1):
    if result[i] == INF:
        print("INF")
    else:
        print(result[i])
