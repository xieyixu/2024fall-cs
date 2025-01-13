n=int(input())
a=list(map(int,input().split()))
dp=[[0]*2 for _ in range(n+1)]
for i in range(n):
    if a[i]==0:
        dp[i+1][0]=dp[i][0]+1
        dp[i+1][1]=0
    elif a[i]==1:
        dp[i+1][1]=1
        if dp[i+1][1]==dp[i][1]:
            dp[i+1][0]=dp[i][0]+1
            dp[i+1][1]=0
        else:
            dp[i+1][0]=dp[i][0]
    elif a[i]==2:
        dp[i+1][1]=2
        if dp[i+1][1]==dp[i][1]:
            dp[i+1][0]=dp[i][0]+1
            dp[i+1][1]=0
        else:
            dp[i+1][0]=dp[i][0]
    elif a[i]==3:
        dp[i+1][1]=3-dp[i][1]
        dp[i+1][0]=dp[i][0]
print(dp[n][0])