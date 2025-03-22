import sys


N = int(sys.stdin.readline())  
count = [0] * 10001  


for _ in range(N):
    count[int(sys.stdin.readline())] += 1


for num in range(10001):
    if count[num] > 0:
        sys.stdout.write((str(num) + "\n") * count[num])  
