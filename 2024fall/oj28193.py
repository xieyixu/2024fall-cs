n,m=map(int,input().split())
cost=list(map(int,input().split()))
graph={i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=set()
results=[]
for i in range(1,n+1):
    result=[]
    if i not in visited:
        stack=[i]
        visited.add(i)
        result.append(i)
        while stack:
            x=stack.pop()
            for y in graph[x]:
                if y not in visited:
                    stack.append(y)
                    visited.add(y)
                    result.append(y)
    if result:
        results.append(result)
sum_value=0
for result in results:
    min_value=float('inf')
    for x in result:
        min_value=min(min_value,cost[x-1])
    sum_value+=min_value
print(sum_value)