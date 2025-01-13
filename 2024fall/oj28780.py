n,m=map(int,input().split())
a=list(map(int,input().split()))
dp=[float('inf')]*(m+1)
dp[0]=0
for i in range(n):
    for j in range(a[i],m+1):
        dp[j]=min(dp[j-a[i]]+1,dp[j])
if dp[m]>100000000:
    print(-1)
else:
    print(dp[m])