import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root  

V, E = map(int, input().split())  # 정점 수, 간선 수
edges = []

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))  # 가중치 기준 정렬할 거니까 cost를 먼저 넣음

# 부모 초기화
parent = [i for i in range(V + 1)]

# 간선 정렬 (가중치 기준 오름차순)
edges.sort()

total = 0
count = 0

for cost, a, b in edges:
    if find(a) != find(b):  # 사이클이 없으면
        union(a, b)
        total += cost
        count += 1
        if count == V - 1:  # MST 완성
            break

print(total)