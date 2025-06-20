from collections import defaultdict
n=int(input())
graph_1=defaultdict(list)
graph_2=defaultdict(list)
for _ in range(n):
    l=input()
    x,y=l[0],l[-1]
    if l[1]=='=':
        graph_1[x].append(y)
        graph_1[y].append(x)
    elif l[1]=='!':
        graph_2[x].append(y)
        graph_2[y].append(x)
visited=set()
find=True
for x in graph_1:
    component=[]
    if x not in visited:
        stack=[x]
        component.append(x)
        visited.add(x)
        while stack:
            xi=stack.pop()
            for neighbours in graph_1[xi]:
                if neighbours not in visited:
                    visited.add(neighbours)
                    stack.append(neighbours)
                    component.append(neighbours)
    for y in component:
        for z in graph_2[y]:
            if z in component:
                find=False
                break
if find:
    print('True')
else:
    print('False')