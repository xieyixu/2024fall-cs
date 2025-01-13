m=int(input())
n=int(input())
a=list(input().split())
for i in range(n):
    for j in range(n-i-1):
        if a[j]+a[j+1]>a[j+1]+a[j]:
            a[j],a[j+1]=a[j+1],a[j]
dp=[['']*(m+1) for _ in range(n+1)]
for k in range(m+1):
    dp[0][k]=''
for k in range(n+1):
    dp[k][0]=''
for i in range(1,n+1):
    for j in range(1,m+1):
        if len(a[i-1])>j:
            dp[i][j]=dp[i-1][j]
        else:
            if dp[i-1][j]=='':
                dp[i][j]=a[i-1]+dp[i-1][j-len(a[i-1])]
            else:
                dp[i][j]=str(max(int(dp[i-1][j]),int(a[i-1]+dp[i-1][j-len(a[i-1])])))
print(dp[n][m])