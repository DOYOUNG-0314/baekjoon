import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [ i for i in range(N+1)]
def find(x):
    if parent[x]!= x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_b!=parent_a:
        for i in range(N+1):
            if parent[i] == parent_b:
                parent[i] = parent_a


for _ in range(M):
    a ,b = map(int, input().split())

    union(a,b)

par=set(parent)
print(len(par)-1)