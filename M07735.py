import heapq
K=int(input())
N=int(input())
R=int(input())
graph={i:[] for i in range(1,N+1)}
for _ in range(R):
    S,D,L,T=map(int,input().split())
    graph[S].append((D,L,T))
heap=[(0,1,K)]
ans=-1
while heap:
    c,x,m=heapq.heappop(heap)
    if x==N:
        ans=c
        break
    for d,l,t in graph[x]:
        if m-t>=0:
            heapq.heappush(heap,(c+l,d,m-t))
print(ans)