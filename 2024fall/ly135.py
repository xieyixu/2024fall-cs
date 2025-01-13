a=list(map(int,input().split()))
n=len(a)
candy=[1]*n
for i in range(1,n):
    if a[i]>a[i-1]:
        candy[i]=candy[i-1]+1
for i in range(n-2,-1,-1):
    if a[i]>a[i+1]:
        candy[i]=max(candy[i],candy[i+1]+1)
print(sum(candy))