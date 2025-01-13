from collections import deque
directions=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(m,n,a,visited):
    stack=deque([(0,0,0)])
    visited[0][0]=True
    while stack:
        x,y,step=stack.popleft()
        if a[x][y]=='1':
            return step
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and a[nx][ny]!='2':
                visited[nx][ny]=True
                stack.append((nx,ny,step+1))
    return 'NO'

m,n=map(int,input().split())
a=[list(input().split()) for _ in range(m)]
visited=[[False]*n for _ in range(m)]
result=bfs(m,n,a,visited)
print(result)