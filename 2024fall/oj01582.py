m=int(input())
T=[]
for i in range(m):
    l,n=map(int,input().split())
    x=list(map(int,input().split()))
    t = []
    for j in range(n):
        t1=x[j]
        t2=l-x[j]
        t.append(t1)
        t.append(t2)
    t=sorted(t)
    T.append((t[n-1],t[2*n-1]))
for i in range(m):
    print(T[i][0],T[i][1])
