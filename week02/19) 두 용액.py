import sys
import bisect
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
arr.sort()

min_sum = float('inf')
answer = (0, 0)

for i in range(N-1):
    target = -arr[i]
    idx = bisect.bisect_left(arr, target, i+1, N)

    for j in [idx - 1, idx]:
        if i < j < N:
            total = arr[i] + arr[j]
            if abs(total) < min_sum:
                min_sum = abs(total)
                answer = (arr[i], arr[j])

print(answer[0], answer[1])
