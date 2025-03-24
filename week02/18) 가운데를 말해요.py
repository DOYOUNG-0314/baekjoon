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
left = []   # 최대 힙 (음수로 저장)
right = []  # 최소 힙

for _ in range(N):
    num = int(input())

    # 왼쪽 힙에 우선 삽입
    heapq.heappush(left, -num)

    # 왼쪽 최대값이 오른쪽 최소값보다 크면 이동
    if right and -left[0] > right[0]:
        heapq.heappush(right, -heapq.heappop(left))

    # 왼쪽이 오른쪽보다 한 개 이상 더 많도록 조정
    if len(left) < len(right):
        heapq.heappush(left, -heapq.heappop(right))

    # 중앙값은 왼쪽 힙의 루트
    print(-left[0])
