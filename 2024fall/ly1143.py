text1,text2=input().split()
n1,n2=len(text1),len(text2)
dp=[[0]*(n1+1) for _ in range(n2+1)]
for i in range(1,n2+1):
    for j in range(1,n1+1):
        if text1[j-1]==text2[i-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[n2][n1])