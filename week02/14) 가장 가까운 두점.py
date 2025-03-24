import math
n=int(input())
min_D=0
a, b = map(int, input().split())
for i in range(n-1):
    x, y = map(int, input().split())
    D= math.hypot(a-x, b-y) 
    if D > min_D:
        min_D=D
    
print(int(D**2))