import sys
stack = []
input = sys.stdin.readline

def push(X):
    stack.append(X)

def pop():
    if stack:
        return stack.pop()
    else:
        return -1


def size():
    return len(stack)

def empty():
    return 0 if stack else 1

def top():
    return stack[-1] if stack else -1

n = int(input())

for _ in range(n):
    command = input().split()
    
    if command[0] == "push":
        push(int(command[1]))
    elif command[0] == "pop":
        print(pop())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "top":
        print(top())

