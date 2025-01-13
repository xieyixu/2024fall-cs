direction=[(1,0),(1,1),(0,1),(1,-1),(-1,1),(-1,0),(0,-1),(-1,-1)]
def dfs(grid,visited,i,j,N,M):
    stack=[(i,j)]
    visited[i][j]=True
    while stack:
        x,y=stack.pop()     #对于每一个点弹出并作检查，看其周围是否有水塘。
        for dx,dy in direction:
            nx,ny=x+dx,y+dy
            if (0<=nx<N) and (0<=ny<M) and not visited[nx][ny] and grid[nx][ny]=='W':
                visited[nx][ny]=True
                stack.append((nx,ny))
def count(grid,N,M):
    visited=[[False]*M for _ in range(N)]
    pond_count=0
    for i in range(N):
        for j in range(M):
            if grid[i][j]=='W' and not visited[i][j]:
                dfs(grid,visited,i,j,N,M)
                pond_count+=1
    return pond_count
N,M=map(int,input().split())
grid=[input().strip() for _ in range(N)]
print(count(grid,N,M))