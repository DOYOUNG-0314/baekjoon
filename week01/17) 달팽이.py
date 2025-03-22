Q=input()
W=Q.split(' ')

A=W[0]
B=W[1]
V=W[2]

A=int(A)
B=int(B)
V=int(V)

X = (V-B)/(A-B)
if X %1 == 0:
    print(int(X))
else :
    print(int(X)+1)

