import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    command = input().strip()

    if command.startswith('push'):
        # "push X" → 숫자만 분리해서 넣기
        _, x = command.split()
        queue.append(int(x))

    elif command == 'pop':
        print(queue.popleft() if queue else -1)

    elif command == 'size':
        print(len(queue))

    elif command == 'empty':
        print(1 if not queue else 0)

    elif command == 'front':
        print(queue[0] if queue else -1)

    elif command == 'back':
        print(queue[-1] if queue else -1)
