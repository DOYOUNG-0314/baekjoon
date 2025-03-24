import heapq

heap=[]

N=int(input())

for _ in range(N):
    x=int(input())
    heapq.heappush(heap, x)
   
count=0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    count+=a+b
    heapq.heappush(heap, a+b)
        
print(count) 
    
