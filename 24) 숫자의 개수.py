A=int(input())
B=int(input())
C=int(input())

D=A*B*C

D=str(D)

count = [0]*10

for i in D:
    count[int(i)] += 1
for count_print in count:
    print(count_print)


