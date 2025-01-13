a=list(map(int,input().split(',')))
n=len(a)
dp=[0]*n
dp[0]=a[0]
max_value=a[0]
for i in range(1,n):
    dp[i]=max(dp[i-1]+a[i],a[i])
    max_value=max(max_value,dp[i])
dp_skip=[0]*n
max_value_skip=a[0]
for i in range(1,n):
    dp_skip[i]=max(dp_skip[i-1]+a[i],dp[i-1])
    max_value_skip=max(dp_skip[i],max_value_skip)
max_value=max(max_value_skip,max_value)
print(max_value)