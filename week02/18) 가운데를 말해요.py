'''import sys
input = sys.stdin.readline
N=int(input())
su=[]
for _ in range(N):
    num=int(input())
    su.append(num)
    su.sort()
    if len(su)%2==1:
        print(su[len(su)//2])
    else:
        if su[len(su)//2-1] < su[len(su)//2]:
            print(su[len(su)//2-1])
        else:
            print(su[len(su)//2])'''

import sys, heapq
input = sys.stdin.readline

N = int(input())
left = []   # 최대 힙
right = []  # 최소 힙

for _ in range(N):
    num = int(input())

    # 1. 왼쪽과 오른쪽 균형을 먼저 맞춤
    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    # 2. 힙의 값이 교차될 경우 교환 (정렬 조건 유지)
    if right and -left[0] > right[0]:
        max_left = -heapq.heappop(left)
        min_right = heapq.heappop(right)
        heapq.heappush(left, -min_right)
        heapq.heappush(right, max_left)

    # 3. 중앙값 출력 (항상 왼쪽 루트)
    print(-left[0])