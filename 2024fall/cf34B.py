n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
i=0
sum=0
while i<m and a[i]<0:
    sum+=a[i]
    i+=1
print(-sum)