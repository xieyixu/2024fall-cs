N,K=map(int,input().split())
count=0
parent=list(range(N+1))
d=[0]*(N+1)
def find(u):
    if parent[u]!=u:
        orig_parent=parent[u]
        parent[u]=find(parent[u])
        d[u]+=d[orig_parent]
        d[u]%=3
    return parent[u]
for i in range(K):
    D,X,Y=map(int,input().split())
    if X>N or Y>N:
        count+=1
        continue
    elif D==2 and X==Y:
        count+=1
        continue
    X,Y=X-1,Y-1

    rx=find(X)
    ry=find(Y)
    if rx!=ry:
        parent[rx]=ry
        if D==1:
            delta=(d[Y]-d[X])%3
        else:
            delta=(d[Y]-d[X]+1)%3
        d[rx]=delta
    else:
        if D==1:
            if (d[X]-d[Y])%3!=0:
                count+=1
        else:
            if (d[X]-d[Y])%3!=1:
                count+=1
print(count)