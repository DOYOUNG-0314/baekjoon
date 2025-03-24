from collections import deque

count = 0
queue = deque()
N, K = map(int,input().split())
for i in range(0,N):
    queue.append(i+1)

result = []

while queue:
    count = (count + K -1)% len(queue)
    result.append(queue[count])
    queue.remove(queue[count])

print("<", ", ".join(map(str,result)), ">")