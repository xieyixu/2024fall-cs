T,n=map(int,input().split())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
dp=[float('-inf')]*(T+1)
dp[0]=0
for i in range(n):
    for j in range(T,a[i][0]-1,-1):
        dp[j]=max(dp[j],dp[j-a[i][0]]+a[i][1])
if dp[T]<0:
    print(-1)
else:
    print(dp[T])