MOD=1000000007
t,k=map(int,input().split())
queries=[]
max_b=0
for _ in range(t):
    a,b=map(int,input().split())
    queries.append((a,b))
    max_b=max(max_b,b)
dp=[0]*(max_b+1)
prefix=[0]*(max_b+1)
dp[0]=1
for i in range(1,max_b+1):
    dp[i]=dp[i-1]
    if i>=k:
        dp[i]=(dp[i]+dp[i-k])%MOD
    prefix[i]=(prefix[i-1]+dp[i])%MOD
answer=[]
for a,b in queries:
    result=(prefix[b]-prefix[a - 1])%MOD
    answer.append(result)
print("\n".join(map(str, answer)))