K=int(input())
A=[]
for _ in range(K):
    N=int(input())
    
    if N == 0:
        A.pop()
    else:
        A.append(N)

print(sum(A))   
