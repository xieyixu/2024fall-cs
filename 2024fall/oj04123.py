directions=[(2,1),(1,2),(2,-1),(-1,2),(-2,1),(1,-2),(-2,-1),(-1,-2)]
def dfs(n,m,x,y,visited,count,total):
    if count==n*m:
        total[0]+=1
        return
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny]=True
            dfs(n,m,nx,ny,visited,count+1,total)
            visited[nx][ny]=False

T=int(input())
answer=[]
for _ in range(T):
    n,m,x,y=map(int,input().split())
    visited=[[False]*m for _ in range(n)]
    visited[x][y]=True
    total=[0]
    dfs(n,m,x,y,visited,1,total)
    answer.append(total[0])
for s in answer:
    print(s)