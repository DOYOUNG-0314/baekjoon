import sys
input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))

stack = []
top_num = []

for i in range(1, N):  # 1번 인덱스부터 시작
    while stack and top[stack[-1]] < top[i]:
        stack.pop()
    if stack:
        top_num.append(stack[-1] + 1)
    else:
        top_num.append(0)
    stack.append(i)

print(0, *top_num)
