import sys
input = sys.stdin.readline

N = int(input())

top = list(map(int, sys.stdin.readline().split()))

height = 0
top_num = 0
for h in reversed(top):
    if h > height:
        
        top_num.add(h)
        height = h

height = 0
top_num[0] = 0

print(*top_num)
