A=int(input())
C=[]
for i in range(A):
    B=int(input())
    C.append(B)
    
C.sort()

for j in range(len(C)):
    print(C[j])