n,m=map(int,input())
dp=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if 