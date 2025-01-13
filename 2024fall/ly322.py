n=int(input())
a=list(map(int,input().split()))
m=len(a)
dp=[float('inf')]*(n+1)
dp[0]=0
for i in range(m):
      for j in range(a[i],n+1):
          dp[j]=min(dp[j],dp[j-a[i]]+1)
print(dp[n])