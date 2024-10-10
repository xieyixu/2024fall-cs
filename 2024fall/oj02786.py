n = int(input())
a = [int(input()) for _ in range(n)]
dp=[0]*(10**6)
dp[0]=1
dp[1]=2
for i in range(2,10**6):
    dp[i]=(2*dp[i-1]+dp[i-2])%32767

for x in a:
    print(dp[x-1])
