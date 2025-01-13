T=int(input())
answer=[]
for _ in range(T):
    E,F=map(int,input().split())
    N=int(input())
    a=[]
    for _ in range(N):
        a.append(list(map(int,input().split())))
    dp=[float('inf')]*(F-E+1)
    dp[0]=0
    for i in range(N):
        for j in range(a[i][1],F-E+1):
            dp[j]=min(dp[j],dp[j-a[i][1]]+a[i][0])
    answer.append(dp[F-E])
for s in answer:
    if s>1000000000:
        print(f"This is impossible.")
    else:
        print(f"The minimum amount of money in the piggy-bank is {s}.")