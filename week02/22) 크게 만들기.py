N, K=map(int,input().split())
number = input().strip()
stack=[]
count = 0
for digit in number:
    while stack and count < K and stack[-1]<digit:
        stack.pop()
        count += 1
    stack.append(digit)

while count < K:
    stack.pop()
    count += 1

print(''.join(stack))


    