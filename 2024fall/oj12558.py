direction=[(1,0),(-1,0),(0,1),(0,-1)]
def find(n,m,M):
    count=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if M[i][j]==1:
                for dx,dy in direction:
                    nx,ny=i+dx,j+dy
                    if M[nx][ny]==0:
                        count+=1
    return count
n,m=map(int,input().split())
M=[[0]*(m+2) for _ in range(n+2)]
for i in range(1,n+1):
    a=list(map(int,input().split()))
    for j in range(m):
        M[i][j+1]=a[j]
print(find(n,m,M))