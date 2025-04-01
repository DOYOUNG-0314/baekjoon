T = int(input())
E=int(input())
parent=[i for i in range(T+1)]
def find(a):
    if a!=parent[a]:
        parent[a]=find(parent[a])
    return parent[a]
def union(a,b):
    parent_a=find(a)
    parent_b=find(b)
    if parent_a!=parent_b:
        for i in range(1,T+1):
            if parent[i]==parent_b:
                parent[i]=parent_a
        
for _ in range(E):
    a,b=sorted(map(int, input().split()))
    union(a,b)

count=0

for i in range(1, T+1):
    if parent[i]==parent[1]:
        count+=1
print(count-1)