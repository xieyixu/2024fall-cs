n,a,b,c=map(int,input().split())
dp=[-1]*(n+1) #一个关于是否可以到达的小技巧。不要想得太复杂。
dp[0]=0
for j in range(0,n+1):
    if dp[j]!=-1:
        if j+a<=n:
            dp[j+a]=max(dp[j+a],dp[j]+1)
        if j+b<=n:
            dp[j+b]=max(dp[j+b],dp[j]+1)
        if j+c<=n:
            dp[j+c]=max(dp[j+c],dp[j]+1)
print(dp[n])