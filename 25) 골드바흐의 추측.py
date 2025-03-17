"""T = int(input())

targets = []                         
for _ in range(T):
    targets.append(int(input())) 


max_val = max(targets)              

X = []      
minority = [] 


for i in range(max_val + 1):         
    X.append(i)
    Y = 0
    
    if i >= 2:                       
        for j in range(1, i + 1):   
            if i % j == 0:
                Y += 1
    if Y == 2:
        minority.append(i)           


result = []                        


for t in targets:                   
    if t >= 4 and t % 2 == 0:      
        best = None
        w_diff = float('inf')
        
        for h in range(len(minority)):
            for g in range(h, len(minority)):  
                if minority[h] + minority[g] == t:  
                    w = abs(minority[h] - minority[g])  
                    if w < w_diff:
                        w_diff = w
                        best = (minority[h], minority[g])
        if best is not None:
            result.append((t, best))  

for item in result:               
    print(item[1][0], item[1][1]) 
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    target = int(input())
    mid = target // 2  
    offset = 0         
    found = False
    while mid - offset >= 2:   
        left = mid - offset
        right = target - left  
        if left > right:
            break
        if is_prime(left) and is_prime(right):
            print(left, right)
            found = True
            break
        offset += 1
  


