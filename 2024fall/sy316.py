n,m=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]
directions=[(0,1),(0,-1),(1,0),(-1,0)]
visited=[[False]*m for _ in range(n)]
path=[]
current_sum = matrix[0][0]
current_path = [(0, 0)]
max_sum=float('-inf')

def dfs(x,y,current_sum,current_path):
    global path,max_sum
    if (x,y)==(n-1,m-1):
        if current_sum>max_sum:
            max_sum=current_sum
            path=current_path[:]
        return
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny]=True
            current_path.append((nx,ny))
            dfs(nx,ny,current_sum+matrix[nx][ny], current_path)
            current_path.pop()
            visited[nx][ny]=False
visited[0][0]=True
dfs(0,0,matrix[0][0],[(0,0)])
for x,y in path:
    print(f'{x+1} {y+1}')