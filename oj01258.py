import heapq
def prim(n,graph):
    visited=[False]*n
    min_edge=[float('inf')]*n
    min_edge[0]=0
    heap=[(0,0)]
    total_weight=0
    while heap:
        cost,u=heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u]=True
        total_weight+=cost
        for v in range(n):
            if not visited[v] and graph[u][v]<min_edge[v]:
                min_edge[v]=graph[u][v]
                heapq.heappush(heap,(graph[u][v],v))
    return total_weight
while True:
    try:
        N=int(input())
        graph=[]
        for _ in range(N):
            graph.append(list(map(int,input().split())))
        print(prim(N,graph))
    except EOFError:
        break