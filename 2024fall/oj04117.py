import sys
data=sys.stdin.read().split()
answer=[]
for s in data:
    n=int(s)
    dp=[[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[0][i]=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j>i :
                dp[i][j]=dp[i][i]
            else:
                dp[i][j]=dp[i][j-1]+dp[i-j][j]
    answer.append(dp[n][n])
for s in answer:
    print(s)