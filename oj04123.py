directions=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
def backtrack(visited,n,m,x,y,count,total):
    if count==n*m:
        total[0]+=1
        return
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False:
            visited[nx][ny]=True
            backtrack(visited,n,m,nx,ny,count+1,total)
            visited[nx][ny]=False
T=int(input())
for _ in range(T):
    n,m,x,y=map(int,input().split())
    total=[0]
    visited=[[False]*m for _ in range(n)]
    visited[x][y]=True
    backtrack(visited,n,m,x,y,1,total)
    print(total[0])