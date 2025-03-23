import sys

input = sys.stdin.readline

N = int(input())

stick = [int(input()) for _ in range(N)]

visible = set()   
height = 0

for h in reversed(stick):
    if h > height:
        visible.add(h)  # set이니까 중복 자동 제거
        height = h

print(len(visible))
