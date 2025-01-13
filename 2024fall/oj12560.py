def check(T,x,y):
    sum=T[x-1][y-1]+T[x-1][y]+T[x-1][y+1]+T[x][y-1]+T[x][y+1]+T[x+1][y-1]+T[x+1][y]+T[x+1][y+1]
    if T[x][y]==1:
        if sum<2 or sum>3:
            return 0
        else:
            return 1
    else:
        if sum==3:
            return 1
        else:
            return 0

n,m=map(int,input().split())
matrix=[[0]*(m+2) for _ in range(n+2)]
for x in range(1,n+1):
    row=list(map(int,input().split()))
    matrix[x][1:m+1]=row
M=[[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        M[i][j]=check(matrix,i+1,j+1)
for i in range(n):
    for j in range(m):
        print(M[i][j],end=' ')
    print('')