A=input()
B=list(A)


if len(B) <= 2:
    print(A) 
else:
    B=0
    A=int(A)
    X=0
    for i in range (A):
        B=A-i
        B=str(B)
        if len(B) <=2:
            X+=99
            break 

        C=list(B)
        if int(C[0])-int(C[1]) == int(C[1])-int(C[2]):
            X+=1
    print(X)


        

    
