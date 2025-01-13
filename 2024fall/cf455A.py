n=int(input())
a=list(map(int,input().split()))
max_a=max(a)
dp=[0]*(max_a+1)
freq=[0]*(max_a+1)
for num in a:
    freq[num]+=1
dp[1]=freq[1]
for x in range(2,max_a+1):
    dp[x]=max(dp[x-1],dp[x-2]+freq[x]*x)
print(dp[max_a])