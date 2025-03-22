N = int(input())
A = list(map(int, input().split()))


M = int(input())
B = list(map(int, input().split()))

A.sort()

for i in range (len(B)):
    left=0
    right=len(A)-1
    found = False
    while left <= right:
        mid=(left+right)//2

        if A[mid] == B[i]:
            print(1)
            found = True
            break
        elif A[mid] < B[i]:
            left = mid + 1
        else:
            right = mid - 1
    if not found:        
        print(0)

