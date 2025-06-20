n=int(input())
graph={i:[] for i in range(n)}
for _ in range(n-1):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
ban=set(list(map(int,input().split())))
stack=[0]
visited=set()
visited.add(0)
count=1
while stack:
    x=stack.pop()
    for y in graph[x]:
        if y not in visited and y not in ban:
            visited.add(y)
            stack.append(y)
            count+=1
print(count)