N,B=map(int,input().split())
cost=list(map(int,input().split()))
weight=list(map(int,input().split()))
dp=[0]*(B+1)
for i in range(N):
    for j in range(B,weight[i]-1,-1):
        if j>=weight[i]:
            dp[j]=max(dp[j],dp[j-weight[i]]+cost[i])
print(dp[B])
