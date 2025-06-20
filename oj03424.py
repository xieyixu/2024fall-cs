import heapq
N,M=map(int,input().split())
graph={i:[] for i in range(1,N+1)}
for _ in range(M):
    A,B,C=map(int,input().split())
    graph[A].append((B,C))
heap=[(0,1)]
dist=[float('inf')]*(N+1)
dist[1]=0
ans=-1
while heap:
    l,x=heapq.heappop(heap)
    if x==N:
        ans=l
        break
    if l>dist[x]:
        continue
    for y,t in graph[x]:
        if dist[y]>l+t:
            dist[y]=l+t
            heapq.heappush(heap,(dist[y],y))
print(ans)
