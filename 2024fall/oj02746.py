f=[]
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    else:
        a=[1]*n
        r=n
        i=0
        t=0
        while r>1:     #求和会影响时间
            if i==n:
                i=0
            if a[i]==0:
                i+=1
            elif a[i]==1:
                t=t+1
                if t==m:
                    a[i]=0
                    t=0
                    i+=1
                    r=r-1
                else:
                    i+=1
    for j in range(n):     #直接遍历会比用index更快
        if a[j]!=0:
            f.append(j+1)
            break
for _ in f:
    print(_)