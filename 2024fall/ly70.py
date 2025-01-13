n=int(input())
dp=[0]*(n)
if n>2:
    dp[0]=1
    dp[1]=2
    for i in range(2,n):
        dp[i]=dp[i-2]+dp[i-1]
    print(dp[n-1])
elif n==2:
    print(2)
elif n==1:
    print(1)