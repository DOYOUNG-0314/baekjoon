T = int(input())

for _ in range(T):
    R,S = input().split(maxsplit=1)
    R=int(R)
    for j in S:
        print(j*R, end='')
    print() 
        


