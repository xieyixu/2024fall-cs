n=int(input())
graph={i:[] for i in range(n)}
result={0}
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
ban=set(map(int,input().split()))
stack=[0]
while stack:
    x=stack.pop()
    for r in graph[x]:
        if r not in ban and r not in result:
            result.add(r)
            stack.append(r)
print(len(result))