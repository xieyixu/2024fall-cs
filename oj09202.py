from collections import deque
def has_cycle(graph):
    in_degree=[0]*len(graph)
    for u in range(len(graph)):
        for v in graph[u]:
            in_degree[v]+=1
    queue=deque()
    for node in range(len(graph)):
        if in_degree[node]==0:
            queue.append(node)
    count=0
    while queue:
        u=queue.popleft()
        count+=1
        for v in graph[u]:
            in_degree[v]-=1
            if in_degree[v]==0:
                queue.append(v)
    return count!=len(graph)
T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    graph={i:[] for i in range(N)}
    for _ in range(M):
        x,y=map(int,input().split())
        graph[x-1].append(y-1)
    if has_cycle(graph):
        print('Yes')
    else:
        print('No')