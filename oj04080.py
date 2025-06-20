import heapq
n=int(input())
heap=list(map(int,input().split()))
heapq.heapify(heap)
ans=0
while len(heap)>1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    ans+=a+b
    heapq.heappush(heap,a+b)
print(ans)