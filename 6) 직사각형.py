x, y, w, h = map(int,input().split())

a = min(x,y)
b = w-x
c = h-y

print(min(a,b,c))