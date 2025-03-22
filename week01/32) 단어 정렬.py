N=int(input())
A=[]
for _ in range(N):
    A.append(input())
A=list(set(A))
A.sort(key=lambda A: (len(A), A))


for i in range(len(A)):
        print(A[i])
   