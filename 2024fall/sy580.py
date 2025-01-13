m,n=map(int,input().split())
M=[]
T=[]
for i in range(m):
    M.append(list(map(int,input().split())))
for i in range(m):
    for j in range(n):
        t=M[i][j]*(M[0][j]*1000+M[i][-1]*100+M[-1][j]*10+M[i][0])
        T.append(t)
print(max(T))