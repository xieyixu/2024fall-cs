t=[]
while True:
    N=int(input())
    if N==0:
        break
    else:
        a=[]
        for _ in range(N):
            DC=list(map(int,input().split()))
            a.append(DC)
        a=sorted(a,key=lambda x:(x[0],x[1]))
        candidate=0
        min_cost=float('inf')
        for i in range(N):
            if a[i][1]<min_cost:     #原题两个条件其实是一个条件
                candidate+=1
                min_cost=a[i][1]
        t.append(candidate)
for candidate in t:
    print(candidate)