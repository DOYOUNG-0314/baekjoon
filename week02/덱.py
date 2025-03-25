import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
dq = deque()

for _ in range(N):
    command = input().strip().split()
    
    if command[0] == 'push_front':
        dq.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        dq.append(int(command[1]))
    elif command[0] == 'pop_front':
        print(dq.popleft() if dq else -1)
    elif command[0] == 'pop_back':
        print(dq.pop() if dq else -1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        print(0 if dq else 1)
    elif command[0] == 'front':
        print(dq[0] if dq else -1)
    elif command[0] == 'back':
        print(dq[-1] if dq else -1)
