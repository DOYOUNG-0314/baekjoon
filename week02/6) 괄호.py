T=int(input())


for _ in range(T):
    balance=0
    n=input()
    result=True
    for ch in n:    
        if ch == "(" :
            balance+=1
        else:
            balance-=1
        
        if balance < 0:
            result=False
            break
    
    if balance != 0:
        result=False
    if result==True:
        print("YES")
    else:
        print("NO")