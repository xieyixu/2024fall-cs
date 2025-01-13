def optimize_memory(N,M,K,a):
    dp_previous=[[0]*(M+1) for _ in range(N+1)]
    dp_current=[[0]*(M+1) for _ in range(N+1)]  #一个三维数组dp太耗空间了，可以采用两个二维数组dp来代替三维数组。
    for i in range(1,K+1):
        need_ball,damage=a[i-1]
        for j in range(1,N+1):
            for k in range(1,M+1):
                dp_current[j][k]=dp_previous[j][k]
                if j>=need_ball and k>=damage:
                    dp_current[j][k]=max(dp_current[j][k],dp_previous[j-need_ball][k-damage]+1)
        dp_previous,dp_current=dp_current,dp_previous
    max_c=dp_previous[N][M]
    i=M-1
    while i>=0:
        if dp_previous[N][i]==max_c:
            i-=1
        else:
            break
    remaining_health=M-(i+1)
    return max_c,remaining_health

N,M,K = map(int,input().split())
a=[list(map(int,input().split())) for _ in range(K)]
max_c,remaining_health=optimize_memory(N,M,K,a)
print(max_c,remaining_health)