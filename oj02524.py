k=1
while True:
    count=0
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    graph={i+1:[] for i in range(n)}
    for _ in range(m):
        i,j=map(int,input().split())
        graph[i].append(j)
        graph[j].append(i)
    visited=set()
    for i in range(1,n+1):
        if i not in visited:
            visited.add(i)
            stack=[i]
            while stack:
                x=stack.pop()
                for y in graph[x]:
                    if y not in visited:
                        visited.add(y)
                        stack.append(y)
            count+=1
    print(f'Case {k}: {count}')
    k+=1