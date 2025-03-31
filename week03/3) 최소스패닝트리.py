import sys
sys.setrecursionlimit(10**6)
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
    edges.append((cost, a, b))

parent = [i for i in range(V + 1)]

edges.sort()

total = 0
count = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        total += cost
        count += 1
        if count == V - 1:
            break

print(total)
