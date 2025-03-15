A=input()
B=A.split()

C=[int(digit)for digit in B[0]]
D=[int(digit)for digit in B[1]]


if C[2] > D[2]:
    print(C[2],end='')
    print(C[1],end='')
    print(C[0])
elif C[2] == D[2]:
    if C[1] > D[1]:
        print(C[2],end='')
        print(C[1],end='')
        print(C[0])
    elif C[1] == D[1]:
        if C[0] > D[0]:
            print(C[2],end='')
            print(C[1],end='')
            print(C[0]) 
        else:
            print(D[2],end='')
            print(D[1],end='')
            print(D[0])
    else:
        print(D[2],end='')
        print(D[1],end='')
        print(D[0])
else:
    print(D[2],end='')
    print(D[1],end='')
    print(D[0])

