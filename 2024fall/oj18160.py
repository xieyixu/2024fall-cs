directions=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
def dfs(i,j,visited,a,N,M):
    stack=[(i,j)]
    num=1
    visited[i][j]=True
    while stack:
        x,y=stack.pop()
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and a[nx][ny]=='W':
                visited[nx][ny]=True
                stack.append((nx,ny))
                num+=1
    return num

T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    a=[list(input().strip()) for _ in range(N)]
    visited=[[False]*M for _ in range(N)]
    s=[]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and a[i][j]=='W':
                s.append(dfs(i,j,visited, a, N, M))
    print(max(s) if s else 0)