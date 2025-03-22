B,A=map(int,input().split())
cutting_su=int(input())

g=[]    #가로 0
l=[]    #세로 1

for _ in range (cutting_su):   
    G,L = map(int,input().split())
    if G==0:
        g.append(L)
    else:
        l.append(L)

g.append(0)
g.append(A)
l.append(0)
l.append(B)

g.sort()
l.sort()

max_g= max(g[i] - g[i - 1] for i in range(1, len(g)))

max_l= max(l[i] - l[i - 1] for i in range(1, len(l)))

print(max_g*max_l)