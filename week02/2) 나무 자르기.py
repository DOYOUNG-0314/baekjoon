import sys
import bisect

N, M = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
L.sort()

top = L[-1]
bottom = 0  
result = 0  

while bottom <= top:
    line = (top + bottom) // 2
    idx = bisect.bisect_right(L, line)
    total = sum(L[i] - line for i in range(idx, N))

    if total >= M:
        result = line
        bottom = line + 1
    else:
        top = line - 1

print(result)
