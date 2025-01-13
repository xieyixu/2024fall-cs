m=int(input())
n=int(input())
dp=[[0]*n for _ in range(m)]
for i in range(n):
    dp[0][i]=1
for i in range(m):
    dp[i][0]=1
for i in range(1,m):
    for j in range(1,n):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(dp[m-1][n-1])  #关于leetcode上的代码，只要提交一个函数的形式，而不需要写输入输出。