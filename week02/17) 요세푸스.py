N, K = map(int, input().split())
queue = list(range(1, N + 1))
result = []
count = 0

while queue:
    count = (count + K - 1) % len(queue)
    result.append(queue.pop(count))  

print("<" + ", ".join(map(str, result)) + ">")
