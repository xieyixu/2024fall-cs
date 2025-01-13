import heapq
N=int(input())
heap=[]
a=list(map(int,input().split()))
for s in a:
    heapq.heappush(heap,s)
count=0
for i in range(N-1):
    x1=heapq.heappop(heap)
    x2=heapq.heappop(heap)
    count+=x1+x2
    heapq.heappush(heap,x1+x2)
print(count)