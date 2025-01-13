t=int(input())
for _ in range(t):
    M,N=map(int,input().split())
    dp=[[0]*(N+1) for _ in range(M+1)]
    for j in range(N+1):
        dp[0][j]=1
    for i in range(1,M+1):
        for j in range(1,N+1):
            dp[i][j]=dp[i][j-1]+(dp[i-j][j] if i-j>=0 else 0)
    print(dp[M][N])