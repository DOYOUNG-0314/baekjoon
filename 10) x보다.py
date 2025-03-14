N, X = map(int, input().split(' '))

A=input()
B=A.split(' ')
for i in range(len(B)):
    if int(B[i]) < X :
        print(B[i],end=' ')

