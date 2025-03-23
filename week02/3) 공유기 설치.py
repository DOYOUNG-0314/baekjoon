import sys
input = sys.stdin.readline

N, C = map(int, input().split())

house = [int(input()) for _ in range(N)]

house.sort()

low = 1
high = house[-1]-house[0]
ans = 0

def place(D):
    count = 1
    last = house[0]
    for i in range(1, N):
        if house[i] - last >= D:
            count += 1
            last = house[i]
    return count >=C
while low <= high:
    mid = (low + high) // 2
    if place(mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
print(ans)


