import sys

input_data=sys.stdin.read().splitlines()
answer=[]
for line in input_data:
    X, Y = line.split()
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i - 1] ==Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j-1])
    answer.append(dp[m][n])
for a in answer:
    print(a)