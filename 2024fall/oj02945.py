k=int(input())
h=list(map(int,input().split()))
n=len(h)
dp=[1]*n
for i in range(n):
    for j in range(i):
        if h[i]<=h[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))