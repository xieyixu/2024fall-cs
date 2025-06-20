from collections import deque
n,m=map(int,input().split())
c=list(map(int,input().split()))
parent=list(range(n))
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
for i in range(m):
    x,y=map(int,input().split())
    x,y=x-1,y-1
    root_x=find(x)
    root_y=find(y)
    if root_x!=root_y:
        if c[root_x]<c[root_y]:
            parent[root_y]=root_x
            c[root_x]=min(c[root_y],c[root_x])
        else:
            parent[root_x]=root_y
            c[root_y]=min(c[root_x],c[root_y])
total_cost=0
for i in range(n):
    if parent[i]==i:
        total_cost+=c[i]
print(total_cost)