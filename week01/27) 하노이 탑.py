import sys
def hanoi(n, A, C, B):
    if n == 1:
        print(A,C)
        return
    hanoi(n-1, A, B, C)
    print(A,C)
    hanoi(n-1, B, C, A)
   

n = int(sys.stdin.readline())

k=2**n-1

print(k)

if n <= 20:
    hanoi(n, 1, 3, 2)



    
