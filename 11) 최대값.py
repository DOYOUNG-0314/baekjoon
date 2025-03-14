A=[]
for i in range(9):
    A.append(int(input()))

B= max(A)
print(B)

for j in range(9):
    if A[j] == B:
        print(j+1)

