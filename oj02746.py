while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    a=[1]*n
    sum_a=n
    i=0
    j=0
    while sum_a>1:
        if j==n:
            j=0
        if a[j]!=0:
            i+=1
        if i==m:
            a[j]=0
            i=0
            sum_a-=1
        j+=1
    for i in range(n):
        if a[i]==1:
            print(i+1)
            break