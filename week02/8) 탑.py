import sys
input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))

stack = []
top_num = []

for i in range(N):  #  0부터 시작!
    while stack and top[stack[-1]] < top[i]:
        stack.pop()
    if stack:
        top_num.append(stack[-1] + 1)
    else:
        top_num.append(0)
    stack.append(i)

print(*top_num)
