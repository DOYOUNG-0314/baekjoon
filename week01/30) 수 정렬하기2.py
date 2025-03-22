import sys
n = int(sys.stdin.readline())
C=[]
for _ in range(n):
    B=int(sys.stdin.readline())
    C.append(B)
    
C.sort()

for j in range(len(C)):
    print(C[j])
