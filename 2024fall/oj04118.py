T=int(input())
answer=[]
for _ in range(T):
    n,k=map(int,input().split())
    m=list(map(int,input().split()))
    p=list(map(int,input().split()))
    dp=[0]*(n)
    dp[0]=p[0]
    for i in range(1,n):
        dp[i]=p[i]
        for j in range(i):
            if m[i]-m[j]>k:
                dp[i]=max(dp[i],dp[j]+p[i])
    answer.append(max(dp))
for s in answer:
    print(s)