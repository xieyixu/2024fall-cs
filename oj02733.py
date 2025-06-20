T,M=map(int,input().split())
a=[]
for _ in range(M):
    a.append(list(map(int,input().split())))
dp=[[0]*(T+1) for _ in range(M+1)]
for i in range(1,M+1):
    for j in range(T+1):
        if a[i-1][0]<=j:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-a[i-1][0]]+a[i-1][1])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[M][T])
