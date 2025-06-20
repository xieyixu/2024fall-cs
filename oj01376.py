from collections import deque
def bfs(grid,start,end,direction):
    N,M=len(grid),len(grid[0])
    dir_map={'E':0,'S':1,'W':2,'N':3}
    start_dir=dir_map[direction]
    sr,sc,tr,tc=start[0],start[1],end[0],end[1]
    valid=[[False]*(M) for _ in range(N)]
    for i in range(1,N):
        for j in range(1,M):
            if grid[i-1][j-1]==0 and grid[i-1][j]==0 and grid[i][j-1]==0 and grid[i][j]==0:
                valid[i][j]=True
    if not valid[sr][sc] or not valid[tr][tc]:
        return -1
    dr=[0,1,0,-1]
    dc=[1,0,-1,0]
    visited=[[[False]*4 for _ in range(M)] for _ in range(N)]
    q=deque()
    q.append((sr,sc,start_dir,0))
    visited[sr][sc][start_dir]=True
    while q:
        r,c,d,steps=q.popleft()
        if r==tr and c==tc:
            return steps
        for nd in [(d+3)%4,(d+1)%4]:
            if not visited[r][c][nd]:
                visited[r][c][nd]=True
                q.append((r,c,nd,steps+1))
        for k in range(4):
            nr=r+dr[d]*k
            nc=c+dc[d]*k
            if nr<1 or nr>=N or nc<1 or nc>=M:
                break
            if not valid[nr][nc]:
                break
            if not visited[nr][nc][d]:
                visited[nr][nc][d]=True
                q.append((nr,nc,d,steps+1))
    return -1
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    grid=[list(map(int,input().split())) for _ in range(n)]
    sx,sy,ex,ey,direction=input().split()
    sx,sy,ex,ey=map(int,[sx,sy,ex,ey])
    direction=direction.upper()
    result=bfs(grid,(sx,sy),(ex,ey),direction[0])
    print(result)