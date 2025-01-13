a=list(map(int,input().split()))
n=len(a)
dp=[0]*(n+1)
dp[0]=0
dp[1]=a[0]
if n>1:
    for i in range(2,n+1):
        dp[i]=max(dp[i-1],dp[i-2]+a[i-1])
    print(dp[n])
else:
    print(a[0])