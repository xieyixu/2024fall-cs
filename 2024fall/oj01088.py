C,R=map(int,input().split())
heights=[list(map(int,input().split())) for _ in range(C)]
directions=[(0,1),(0,-1),(1,0),(-1,0)]
dp=[[-1]*R for _ in range(C)]
def dfs(x,y):
    if dp[x][y]!=-1:
        return dp[x][y]
    max_length=0
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<C and 0<=ny<R and heights[nx][ny]<heights[x][y]:
            max_length=max(max_length,1+dfs(nx,ny))
    dp[x][y]=max_length
    return dp[x][y]

for i in range(C):
    for j in range(R):
        dp[i][j]=dfs(i,j)
max_count=0
for i in range(C):
    for j in range(R):
        max_count=max(max_count,dp[i][j])
print(max_count+1)