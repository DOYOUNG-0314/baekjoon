"""high = []
for _ in range(9):
    num = int(input())
    high.append(num)

result = 0
for i in range(len(high)):
    result += high[i]

high.sort()

high_1 = result - high[1]
high_2 = result - high[2]
high_3 = result - high[3]
high_4 = result - high[4]
high_5 = result - high[5]
high_6 = result - high[6]
high_7 = result - high[7]
high_8 = result - high[8]

found = False  
rem_i = -1  
rem_j = -1  

for j in range(2, 9):
    if high_1 - high[j] == 100:
        rem_i = 1
        rem_j = j
        found = True
        break

if not found:
    for k in range(3, 9):
        if high_2 - high[k] == 100:
            rem_i = 2
            rem_j = k
            found = True
            break

if not found:
    for l in range(4, 9):
        if high_3 - high[l] == 100:
            rem_i = 3
            rem_j = l
            found = True
            break

if not found:
    for m in range(5, 9):
        if high_4 - high[m] == 100:
            rem_i = 4
            rem_j = m
            found = True
            break

if not found:
    for n in range(6, 9):
        if high_5 - high[n] == 100:
            rem_i = 5
            rem_j = n
            found = True
            break

if not found:
    for o in range(7, 9):
        if high_6 - high[o] == 100:
            rem_i = 6
            rem_j = o
            found = True
            break

if not found:
    for p in range(8, 9):
        if high_7 - high[p] == 100:
            rem_i = 7
            rem_j = p
            found = True
            break


if found:
    for index in sorted([rem_i, rem_j], reverse=True):
        high.pop(index)

for num in high:
    print(num)"""
high = []
for _ in range(9):
    num = int(input())
    high.append(num)

result = 0
for i in range(len(high)):
    result += high[i]

high.sort()

# 두 난쟁이의 키 합이 result - 100가 되어야 함
# 원래 코드에서 high_1 ~ high_8 등으로 검사했지만,
# 모든 가능한 두 난쟁이 조합을 검사하는 이중 for문으로 대체합니다.
rem_i = -1
rem_j = -1
found = False
for i in range(9):
    for j in range(i+1, 9):
        if result - (high[i] + high[j]) == 100:
            rem_i = i
            rem_j = j
            found = True
            break
    if found:
        break

# 인덱스 변경 문제를 피하기 위해, 큰 인덱스부터 제거합니다.
if found:
    for index in sorted([rem_i, rem_j], reverse=True):
        high.pop(index)

high.sort()
for num in high:
    print(num)

