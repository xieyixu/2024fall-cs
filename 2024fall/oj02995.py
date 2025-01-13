N=int(input())
heights=list(map(int,input().split()))
dp=[[1,1] for _ in range(N)]
for i in range(N):
    for j in range(i):
        if heights[j]<heights[i]:
            dp[i][0]=max(dp[i][0],dp[j][0]+1)
        if heights[j]>heights[i]:
            dp[i][1]=max(dp[i][1],dp[j][0]+1)
            dp[i][1]=max(dp[i][1],dp[j][1]+1)
print(max(max(dp[i][0],dp[i][1]) for i in range(N)))