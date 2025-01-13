mod=1000000007
n,k,d=map(int,input().split())
dp=[0]*(n+1)
dp[0]=1
for weight_sum in range(1,n+1):
    for edge_weight in range(1,k+1):
        if weight_sum>=edge_weight:
            dp[weight_sum]+=dp[weight_sum-edge_weight]
dp_restricted=[0]*(n+1)
dp_restricted[0]=1
for weight_sum in range(1,n+1):
    for edge_weight in range(1,d):
        if weight_sum>=edge_weight:
            dp_restricted[weight_sum]+=dp_restricted[weight_sum-edge_weight]
result=(dp[n]-dp_restricted[n])%mod
print(result)