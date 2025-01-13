n,t=map(int,input().split())
a=list(map(int,input().split()))
sum_a=sum(a)
dp=[False]*(sum_a+1)
dp[0]=True
for price in a:
    for j in range(sum_a,price-1,-1):
        if dp[j-price]:
            dp[j]=True
a=0
for i in range(t,sum_a+1):
    if dp[i]:
        a=i
        break
print(a) #不同的dp思路差别非常大。还是要把问题分解成小问题，这个dp的核心就是对于和来dp。要灵活。