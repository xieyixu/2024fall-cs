N,M=map(int,input().split())
dp=[[0]*(M) for _ in range(N+1)]
dp[1][0]=1
dp[1][1]=1
for i in range(2,N+1):
    for j in range(M):
        if j==0:
            dp[i][j]=sum(dp[i-1][k] for k in range(M))
        else:
            dp[i][j]=dp[i-1][j-1]
answer=sum(dp[N][j] for j in range(M))
print(answer)