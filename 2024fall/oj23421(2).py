N,B=map(int,input().split())
p=list(map(int,input().split()))
w=list(map(int,input().split()))
dp=[0]*(B+1)
for i in range(N):
    for j in range(B,w[i]-1,-1):
        dp[j]=max(dp[j-1],dp[j-w[i]]+p[i])
print(dp[B])