s = input()
stack = []

for ch in s:
    if ch == '(' or ch == '[':
        stack.append(ch)
    elif ch == ')':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                stack.append(2 if temp == 0 else 2 * temp)
                break
            elif isinstance(top, int):
                temp += top
            else:
                print(0)
                exit()
    elif ch == ']':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                stack.append(3 if temp == 0 else 3 * temp)
                break
            elif isinstance(top, int):
                temp += top
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()

# 최종 계산
result = 0
for item in stack:
    if isinstance(item, int):
        result += item
    else:
        print(0)
        exit()

print(result)
