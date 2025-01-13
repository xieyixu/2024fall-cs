from collections import defaultdict
n=int(input())
graph_1=defaultdict(list)
graph_2=defaultdict(list)
find=True
for _ in range(n):
    data=input()
    xi,yi=data[0],data[3]
    if data[1]=='=':
        graph_1[xi].append(yi)
        graph_1[yi].append(xi)
    elif data[1]=='!':
        graph_2[xi].append(yi)
        graph_2[yi].append(xi)
visited=set()
find=True
for x in graph_1:
    component=[]
    if x not in visited:
        visited.add(x)
        stack=[x]
        component.append(x)
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