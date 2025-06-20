import sys
data=list(map(int,sys.stdin.read().split()))
N=data[0]
matrix=data[1:]
A=[matrix[i*N:(i+1)*N] for i in range(N)]
dp=[[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]+A[i-1][j-1]-dp[i-1][j-1]
max_sum=float('-inf')
for i1 in range(1,N+1):
    for i2 in range(i1,N+1):
        temp=[0]*N
        for j in range(1,N+1):
            temp[j-1]=dp[i2][j]-dp[i1-1][j]
        current=float('-inf')
        end_here=temp[0]
        for k in range(1,N):
            end_here=max(temp[k]-temp[k-1],end_here+temp[k]-temp[k-1])
            current=max(end_here,current)
        max_sum=max(max_sum,current)
print(max_sum)