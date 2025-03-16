A=int(input())
B=input()
C=B.split()

Y=0
for i in range (A):
    X=0
    
    for j in range(1,(int(C[i])+1)):
        if (int(C[i])) % j == 0:
            X+=1
    if X == 2:
        Y+=1
print(Y)