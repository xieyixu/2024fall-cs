T=[]
while True:
    n,p,m=map(int,input().split())
    if n==0 and p==0 and m==0:
        break
    else:
        a=[1]*n
        r=n
        i=p-1
        t=0
        j=[]
        while r>1:     #求和会影响时间
            if i==n:
                i=0
            if a[i]==0:
                i+=1
            elif a[i]==1:
                t=t+1
                if t==m:
                    j.append(i)
                    a[i]=0
                    t=0
                    i+=1
                    r=r-1
                else:
                    i+=1
        for _ in range(n):
            if a[_]!=0:
                j.append(_)
                break
    T.append(j)
for j in T:
    for x in j:
        if x!=j[-1]:
            print(f"{x+1},",end="")
        else:
            print(f"{x+1}")